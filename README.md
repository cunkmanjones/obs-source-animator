<h3 align="center">
  <img src="https://github.com/cunkmanjones/obs-easing-python/blob/main/.github/source-animator-logo.png">
</h3>

# General Info
A Python Script that allows the use of easing functions and anchor points to animate the size of a Source. 
> [!WARNING]
> This script was created using **Python 3.6.8** & **OBS v27.2.4 (64-bit)** and has **<ins>NOT</ins>** been tested with other verions. 

# Installation
## Preparation
Make sure your [OBS](https://obsproject.com/) and [Python](https://www.python.org/) Installations are the same Architecture[^1]. *(32-bit or 64-bit)*<br/>
- OBS Versions < v28 will require Python 3.6.8 or Lower.<br/>
- OBS Versions >= v28 can use anything between 3.6.x and 3.11[^2].<br/>

Download and move the script into OBS's script folder. *(i.e ..\\..\obs-studio\data\obs-plugins\frontend-tools\scripts)*<br/>

## Enabling Python in OBS
1. **Open OBS** and access the scripting menu via **Tools -> Scripts**.<br/>
2. Next, click on **Python Settings** and set the path to your installed version of Python. *(i.e ..\\..\Python\Python36)*<br/>
3. From here, select **Scripts** and click the &#xFF0B; at the bottom to select the Python script.<br/>

If script settings load, then you're all set!

# Troublshooting
## Loading Errors
### Incompatible Version of Python
Settings will always appear for Python Scripts that load correctly. If you do not see settings, the issue may be that your OBS and Python installations are incompatible. Please refer to the **Preparation** section.<br/>
You may also want to try loading one of the example scripts OBS provides within the script directory.<br/>
If an example script loads but this script does not, please create an [Issue](https://github.com/cunkmanjones/obs-easing-python/issues) with your installed versions of OBS and Python and the Architectures.
### Untested Versions
The script was created using 64-bit OBS v27.2.4 and Python 3.6.8, and may not work as intended on different versions.<br/>
I tried my best to ensure forward compatibility by using the basics of the OBS API bindings, but I can't test for everything.<br/>
## Usage Errors
### Source Size is Wrong
*ALT-Cropping* will **NOT** work as intended, please use a *Crop/Pad Filter* to crop your source.<br/>
Resizing your source *(i.e Tranform, Crop/Pad Filter, Select & Drag, etc)* after selecting it within the script will cause stored value errors. Please select a different scene or source within the script settings and then return to your original selection. Always check the *Script Log* to see if the correct values are shown.<br/>
### Not all Source Types have been tested!
Source Types such as *Image* & *Game Capture* work as intended, but please keep in mind that not every source type has been tested. 

# License
- [**BSL-1.0 License**](https://github.com/cunkmanjones/obs-easing-python/blob/main/LICENSE.txt)

[^1]: OBS Python/Lua Scripting - 1st Note https://docs.obsproject.com/scripting
[^2]: Python support to use the Py3 stable ABI - 28.0 https://github.com/obsproject/obs-studio/pull/6706
