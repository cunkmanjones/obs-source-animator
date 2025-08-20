import obspython as obs
import time
from math import sin, cos, pi


class Easing:
    _easingFunctions = {
        "linear": {
            "function": lambda t: t,
            "display": "Linear"
        },
        "easeInSine": {
            "function": lambda t: -cos(t * pi / 2) + 1,
            "display": "Sine In"
        },
        "easeOutSine": {
            "function": lambda t: sin(t * pi / 2),
            "display": "Sine Out"
        },
        "easeInOutSine": {
            "function": lambda t: -(cos(pi * t) - 1) / 2,
            "display": "Sine In/Out"
        },
        "easeInQuad": {
            "function": lambda t: t * t,
            "display": "Quad In"
        },
        "easeOutQuad": {
            "function": lambda t: t * (2 - t),
            "display": "Quad Out"
        },
        "easeInOutQuad": {
            "function": lambda t: 2 * t * t if t < 0.5 else -1 + (4 - 2 * t) * t,
            "display": "Quad In/Out"
        },
        "easeInCubic": {
            "function": lambda t: t * t * t,
            "display": "Cubic In"
        },
        "easeOutCubic": {
            "function": lambda t: (t - 1) * (t - 1) * (t - 1) + 1,
            "display": "Cubic Out"
        },
        "easeInOutCubic": {
            "function": lambda t: 4 * t * t * t if t < 0.5 else 1 - (-2 * t + 2) ** 3 / 2,
            "display": "Cubic In/Out" ###
        },
        "easeInQuart": {
            "function": lambda t: t * t * t * t,
            "display": "Quart In"
        },
        "easeOutQuart": {
            "function": lambda t: 1 - (t - 1) * (t - 1) * (t - 1) * (t - 1),
            "display": "Quart Out"
        },
        "easeInOutQuart": {
            "function": lambda t: 8 * t * t * t * t if t < 0.5 else 1 - (-2 * t + 2) ** 4 / 2,
            "display": "Quart In/Out" ###
        },
        "easeInQuint": {
            "function": lambda t: t * t * t * t * t,
            "display": "Quint In"
        },
        "easeOutQuint": {
            "function": lambda t: (t - 1) * (t - 1) * (t - 1) * (t - 1) * (t - 1) + 1,
            "display": "Quint Out"
        },
        "easeInOutQuint": {
            "function": lambda t: 16 * t * t * t * t * t if t < 0.5 else (t - 1) * (t - 1) * (t - 1) * (t - 1) * (t - 1) + 1,
            "display": "Quint In/Out" ###
        },
        "easeInExpo": {
            "function": lambda t: 0 if t == 0 else 2 ** (10 * (t - 1)),
            "display": "Expo In"
        },
        "easeOutExpo": {
            "function": lambda t: 1 if t == 1 else 1 - 2 ** (-10 * t),
            "display": "Expo Out"
        },
        "easeInOutExpo": {
            "function": lambda t: 0 if t == 0 else 1 if t == 1 else (2 ** (10 * (t - 1)) - 1) / 1023,
            "display": "Expo In/Out" ###
        },
        "easeInCirc": {
            "function": lambda t: 1 - (1 - t * t) ** 0.5,
            "display": "Circ In"
        },
        "easeOutCirc": {
            "function": lambda t: (1 - (1 - t * t) ** 0.5),
            "display": "Circ Out"
        },
        "easeInOutCirc": {
            "function": lambda t: 0.5 * (1 - (1 - 4 * t * (1 - t)) ** 0.5) if t < 0.5 else 0.5 * (1 + (1 - 4 * (1 - t) * t) ** 0.5),
            "display": "Circ In/Out"
        },
        "easeInBack": {
            "function": lambda t: 2.70158 * t * t * t - 1.70158 * t * t,
            "display": "Back In"
        },
        "easeOutBack": {
            "function": lambda t: 1 + 2.70158 * (t - 1) * (t - 1) * (t - 1) + 1.70158 * (t - 1) * (t - 1),
            "display": "Back Out"
        },
        "easeInOutBack": {
            "function": lambda t: 0.5 * (2.70158 * t * t * t - 1.70158 * t * t) if t < 0.5 else 0.5 * (1 + 2.70158 * (t - 1) * (t - 1) * (t - 1) + 1.70158 * (t - 1) * (t - 1)),
            "display": "Back In/Out" ###
        },
        "easeInElastic": {
            "function": lambda t: 0 if t == 0 else 1 if t == 1 else -2 ** (10 * (t - 1)) * sin((t - 1.1) * (2 * pi) / 0.4),
            "display": "Elastic In"
        },
        "easeOutElastic": {
            "function": lambda t: 1 if t == 1 else 2 ** (-10 * t) * sin((t - 0.1) * (2 * pi) / 0.4),
            "display": "Elastic Out" ###
        },
        "easeInOutElastic": {
            "function": lambda t: 0 if t == 0 else 1 if t == 1 else (2 ** (10 * (t - 1)) - 1) * sin((t - 0.1) * (2 * pi) / 0.4),
            "display": "Elastic In/Out" ###
        }
    }
    
    @classmethod
    def get_function(self, name):
        return self._easingFunctions.get(name, self._easingFunctions["linear"])["function"] # Default to linear if 'name' not found
    
    @classmethod
    def get_choices(self):
        return [(data["display"], name) for name, data in self._easingFunctions.items()]

class Lists:
    def __init__(self) -> None:
        self.scenes       = []
        self.sources      = []
        self.currentScene = ""

    def refresh_scenes(self) -> list:
        self.scenes = []
        scenes = obs.obs_frontend_get_scenes()

        for scene in scenes:
            name = obs.obs_source_get_name(scene)
            self.scenes.append(name)

        obs.source_list_release(scenes)
        return self.scenes

    def refresh_sources(self, sceneName) -> list:
        self.sources = []
        self.currentScene = sceneName
        scene = obs.obs_get_source_by_name(sceneName)

        if not scene:
            return self.sources
            
        sceneSources = obs.obs_scene_enum_items(obs.obs_scene_from_source(scene))
        if sceneSources:
            for element in sceneSources:
                source = obs.obs_sceneitem_get_source(element)
                name = obs.obs_source_get_name(source)
                self.sources.append(name)
            obs.sceneitem_list_release(sceneSources)
        
        obs.obs_source_release(scene)
        return self.sources

class Animation:
    ANCHOR_TOP_LEFT     = "topLeft"
    ANCHOR_TOP_RIGHT    = "topRight"
    ANCHOR_BOTTOM_LEFT  = "bottomleft"
    ANCHOR_BOTTOM_RIGHT = "bottomright"
    ANCHOR_CENTER       = "center"
    
    def __init__(self) -> None:
        self._properties()
        self._states()
        self._trackers()
        self.listClass = Lists()
        
    def _properties(self) -> None:
        self.sourceName     = ""
        self.sceneName      = ""
        self.duration       = 1.0
        self.easingFunction = ""
        self.anchorPoint    = self.ANCHOR_TOP_LEFT
        self.hotkeyId       = None
        
    def _states(self) -> None:
        self.isAnimating   = False
        self.isExpanded    = False
        self.hotkeyPressed = False
        self.animationId   = 0
        self.startTime     = 0
        self.lastFrameTime = 0
        
    def _trackers(self) -> None:
        self.originalWidth, self.originalHeight           = 0, 0
        self.startWidth, self.startHeight                 = 0, 0
        self.scaledWidth, self.scaledHeight               = 0, 0
        self.targetWidth, self.targetHeight               = 0, 0
        self.currentTargetWidth, self.currentTargetHeight = 0, 0
        self.maintainPosition                             = obs.vec2()

    def _maintain_position(self, source, width, height) -> None:
        pos = obs.vec2()
        obs.obs_sceneitem_get_pos(source, pos)
        
        if self.anchorPoint == self.ANCHOR_TOP_LEFT:
            self.maintainPosition.x, self.maintainPosition.y = pos.x, pos.y
            return

        anchorHandlers = {
            self.ANCHOR_CENTER: lambda: (
                pos.x + width / 2,
                pos.y + height / 2
            ),
            self.ANCHOR_TOP_RIGHT: lambda: (
                pos.x + width,
                pos.y
            ),
            self.ANCHOR_BOTTOM_LEFT: lambda: (
                pos.x,
                pos.y + height
            ),
            self.ANCHOR_BOTTOM_RIGHT: lambda: (
                pos.x + width,
                pos.y + height
            )
        }
        
        self.maintainPosition.x, self.maintainPosition.y = anchorHandlers[self.anchorPoint]()

    def _anchor_position(self, source, width, height) -> None:
        pos = obs.vec2()

        if self.anchorPoint == self.ANCHOR_TOP_LEFT:
            pos.x, pos.y = self.maintainPosition.x, self.maintainPosition.y
            obs.obs_sceneitem_set_pos(source, pos)
            return

        anchorHandlers = {
            self.ANCHOR_CENTER: lambda: (
                self.maintainPosition.x - width / 2,
                self.maintainPosition.y - height / 2
            ),
            self.ANCHOR_TOP_RIGHT: lambda: (
                self.maintainPosition.x - width,
                self.maintainPosition.y
            ),
            self.ANCHOR_BOTTOM_LEFT: lambda: (
                self.maintainPosition.x,
                self.maintainPosition.y - height
            ),
            self.ANCHOR_BOTTOM_RIGHT: lambda: (
                self.maintainPosition.x - width,
                self.maintainPosition.y - height
            )
        }
        
        pos.x, pos.y = anchorHandlers[self.anchorPoint]()
        obs.obs_sceneitem_set_pos(source, pos)

    def _get_source_from_scene(self):
        sourceRelease = obs.obs_get_source_by_name(self.sceneName)
        if not sourceRelease:
            return None, None
            
        sceneContext = obs.obs_scene_from_source(sourceRelease)
        if not sceneContext:
            obs.obs_source_release(sourceRelease)
            return None, None
            
        source = obs.obs_scene_find_source(sceneContext, self.sourceName)
        return source, sourceRelease

    def _animate(self) -> None:
        if not self.isAnimating:
            return

        currentId   = self.animationId
        currentTime = time.time()
        elapsed     = currentTime - self.startTime
        progress    = min(elapsed / self.duration, 1.0)

        if currentTime - self.lastFrameTime < 0.016: # Skip frames for lag issues
            return
        self.lastFrameTime = currentTime

        easing = Easing.get_function(self.easingFunction)
        easeProgress = easing(progress)
        
        source, sourceRelease = self._get_source_from_scene()
        if not source:
            self.stop_animation()
            return
        
        width = round(self.startWidth + (self.currentTargetWidth - self.startWidth) * easeProgress, 2)
        height = round(self.startHeight + (self.currentTargetHeight - self.startHeight) * easeProgress, 2)

        scale = obs.vec2()
        scale.x, scale.y = width / self.originalWidth, height / self.originalHeight
        obs.obs_sceneitem_set_scale(source, scale)

        self._anchor_position(source, width, height)

        obs.obs_source_release(sourceRelease)

        if progress >= 1.0 or currentId != self.animationId:
            self.isExpanded = not self.isExpanded
            self.stop_animation()

    def stop_animation(self) -> None:
        if self.isAnimating:
            obs.timer_remove(self._animate)
            self.isAnimating = False
            self.hotkeyPressed = False

    def _get_source_dimensions(self) -> bool:
        source = obs.obs_get_source_by_name(self.sourceName)
        if not source:
            return False
            
        self.originalWidth, self.originalHeight = obs.obs_source_get_width(source), obs.obs_source_get_height(source)
        obs.obs_source_release(source)
        return True

    def _setup_animation_targets(self, source) -> None:
        scale = obs.vec2()
        obs.obs_sceneitem_get_scale(source, scale)
        
        self.startWidth, self.startHeight = round(self.originalWidth * scale.x, 2), round(self.originalHeight * scale.y, 2) # Current Size pulled on each use
        
        self._maintain_position(source, self.startWidth, self.startHeight)

        if self.isExpanded:
            self.currentTargetWidth, self.currentTargetHeight = self.scaledWidth, self.scaledHeight
        else:
            self.currentTargetWidth, self.currentTargetHeight = self.targetWidth, self.targetHeight

    def _toggle_animation(self) -> None:
        if self.isAnimating:
            return
            
        self.stop_animation()
        self.animationId += 1
        
        if not self.sourceName or not self.sceneName:
            return

        if not self._get_source_dimensions():
            return

        source, sourceRelease = self._get_source_from_scene()
        if not source:
            return

        self._setup_animation_targets(source)
        obs.obs_source_release(sourceRelease)

        self.startTime = time.time()
        self.lastFrameTime = self.startTime
        self.isAnimating = True
        self.hotkeyPressed = True
        
        obs.timer_add(self._animate, 16)

    def hotkey_callback(self, pressed) -> None:
        if pressed and not self.hotkeyPressed: # Only trigger when finished
            self._toggle_animation()

animClass = Animation()

def on_scene_selected(props, prop, settings):
    scene = obs.obs_data_get_string(settings, "scene")
    if scene:
        animClass.sceneName = scene
    animClass.listClass.refresh_sources(scene)
    
    source = obs.obs_properties_get(props, "source")
    obs.obs_property_list_clear(source)
    for element in animClass.listClass.sources:
        obs.obs_property_list_add_string(source, element, element)
    
    return True

def on_source_selected(props, prop, settings):
    sourceName = obs.obs_data_get_string(settings, "source")
    sourceObject = obs.obs_get_source_by_name(sourceName)
    if (not sourceObject and sourceName != animClass.sourceName) or animClass.listClass.sources == []:
        return True
    
    #if sourceObject and sourceName == animClass.sourceName and animClass.listClass.sources != []: # Exclude empty scenes
    width, height = obs.obs_source_get_width(sourceObject), obs.obs_source_get_height(sourceObject)
    animClass.originalWidth, animClass.originalHeight = width, height
    print(f"{sourceName}: {width}px x {height}px") # OBS_TEXT_INFO workaround for older verions of OBS < v28
        
    scale = obs.vec2()
    source, sourceRelease = animClass._get_source_from_scene()
    obs.obs_sceneitem_get_scale(source, scale)
    animClass.scaledWidth, animClass.scaledHeight = animClass.originalWidth * scale.x, animClass.originalHeight * scale.y # Checks if the source is scaled
    obs.obs_source_release(sourceRelease)

    return True

def script_properties():
    props = obs.obs_properties_create()
    
    scenes = animClass.listClass.refresh_scenes()
    sceneDropdown = obs.obs_properties_add_list(
        props,
        "scene",
        "Scene",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING
    )
    for element in scenes:
        obs.obs_property_list_add_string(sceneDropdown, element, element)
    
    sourceDropdown = obs.obs_properties_add_list(
        props,
        "source",
        "Source",
        obs.OBS_COMBO_TYPE_LIST,
        obs.OBS_COMBO_FORMAT_STRING
    )
    
    obs.obs_property_set_modified_callback(sceneDropdown, on_scene_selected)
    obs.obs_property_set_modified_callback(sourceDropdown, on_source_selected)
    
    if animClass.sceneName:
        animClass.listClass.refresh_sources(animClass.sceneName)
        for source in animClass.listClass.sources:
            obs.obs_property_list_add_string(sourceDropdown, source, source)
    
    obs.obs_properties_add_int(props, "target_width", "Target Width", 1, 4096, 1)
    obs.obs_properties_add_int(props, "target_height", "Target Height", 1, 4096, 1)
    obs.obs_properties_add_float(props, "duration", "Duration (seconds)", 0.1, 10.0, 0.1)
    
    easingDropdown = obs.obs_properties_add_list(
        props, "easing", "Easing Function", 
        obs.OBS_COMBO_TYPE_LIST, 
        obs.OBS_COMBO_FORMAT_STRING
    )
    for displayName, internalName in Easing.get_choices():
        obs.obs_property_list_add_string(easingDropdown, displayName, internalName)
    
    anchorDropdown = obs.obs_properties_add_list(
        props, "anchor_point", "Anchor Point", 
        obs.OBS_COMBO_TYPE_LIST, 
        obs.OBS_COMBO_FORMAT_STRING
    )
    anchors = [
        ("Top Left", Animation.ANCHOR_TOP_LEFT),
        ("Top Right", Animation.ANCHOR_TOP_RIGHT),
        ("Bottom Left", Animation.ANCHOR_BOTTOM_LEFT),
        ("Bottom Right", Animation.ANCHOR_BOTTOM_RIGHT),
        ("Center", Animation.ANCHOR_CENTER)
    ]
    for name, val in anchors:
        obs.obs_property_list_add_string(anchorDropdown, name, val)
    
    return props

def script_defaults(settings) -> None:
    obs.obs_data_set_default_string(settings, "scene", "")
    obs.obs_data_set_default_string(settings, "source", "")
    obs.obs_data_set_default_int(settings, "target_width", 1)
    obs.obs_data_set_default_int(settings, "target_height", 1)
    obs.obs_data_set_default_double(settings, "duration", 1.00)
    obs.obs_data_set_default_string(settings, "easing", "easeOutQuad")
    obs.obs_data_set_default_string(settings, "anchor_point", Animation.ANCHOR_TOP_LEFT)

def script_update(settings) -> None:
    animClass.sceneName, animClass.sourceName = obs.obs_data_get_string(settings, "scene"), obs.obs_data_get_string(settings, "source")

    if animClass.sceneName != animClass.listClass.currentScene:
        animClass.listClass.refresh_sources(animClass.sceneName)
    
    animClass.targetWidth = obs.obs_data_get_int(settings, "target_width")
    animClass.targetHeight = obs.obs_data_get_int(settings, "target_height")
    animClass.duration = obs.obs_data_get_double(settings, "duration")
    animClass.easingFunction = obs.obs_data_get_string(settings, "easing")
    animClass.anchorPoint = obs.obs_data_get_string(settings, "anchor_point")

def script_description() -> str:
    return """<center><h2>Source Size Animator</h2></center>
    
    <p>Select your Scene to update your Sources, then select which Source to animate.<p>
    <p>Apply a Hotkey in settings to toggle between the original and target sizes of the Source.</p>
    <p><strong>Warning:</strong> Please use a Crop/Pad Filter on your Source instead of Alt-Cropping! 
    If you are unsure what size your source is (cropped or not), you can check the Script Log after selecting your Source.</p>
    
    <h3><a href="https://easings.net/">Easings.net</a></h3>"""

def script_load(settings) -> None:
    if not settings:
        return
    
    animClass.sceneName = obs.obs_data_get_string(settings, "scene") 
    if animClass.sceneName:
        animClass.listClass.refresh_sources(animClass.sceneName)
    animClass.sourceName = obs.obs_data_get_string(settings, "source")

    hotkeyId = obs.obs_hotkey_register_frontend(
        "source_size_animation_toggle", 
        "Source Size Animation Toggle", 
        lambda *args: animClass.hotkey_callback(*args)
    )
    animClass.hotkeyId = hotkeyId
    
    hotkeyStorage = obs.obs_data_get_array(settings, "source_size_animation_toggle_hotkey")
    if hotkeyStorage:
        obs.obs_hotkey_load(hotkeyId, hotkeyStorage)
        obs.obs_data_array_release(hotkeyStorage)

def script_save(settings) -> None:
    if animClass.hotkeyId:
        hotkeyStorage = obs.obs_hotkey_save(animClass.hotkeyId)
        obs.obs_data_set_array(settings, "source_size_animation_toggle_hotkey", hotkeyStorage)
        obs.obs_data_array_release(hotkeyStorage)

def script_unload() -> None:
    if animClass.isAnimating:
        animClass.stop_animation()

    if animClass.hotkeyId:
        obs.obs_hotkey_unregister(animClass.hotkeyId)
