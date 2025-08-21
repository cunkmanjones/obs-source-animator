<h3 align="center">
  <img src="https://github.com/cunkmanjones/obs-easing-python/blob/main/.github/source-animator-logo.png">
</h3>

# General Info
A Python Script that allows the use of easing functions to animate the size of a Scene. A different anchor point can also be chosen.
> [!WARNING]
> This script was created using **Python 3.6.8 64-bit** & **OBS v27.2.4 64-bit** and has **<ins>NOT</ins>** been tested with other verions. 

# Installation
## Preparation
Make sure your [OBS](https://obsproject.com/) and [Python](https://www.python.org/) Installations are the same Architecture. *(32-bit or 64-bit)*<br/>
OBS Versions < 28 will require Python 3.6.8 or Lower<br/>
OBS Versions >= 28 can use anything between 3.6.x and 3.11<br/>
Download and move the script into OBS's script folder. *(i.e ..\\..\obs-studio\data\obs-plugins\frontend-tools\scripts)*<br/>
## Enabling Python in OBS
Open OBS and access the scripting menu via Tools -> Scripts.<br/>
Next, click on **Python Settings** and set the path to your installed version of Python. *(i.e ..\\..\Python\Python36)*<br/>
From here, select **Scripts** and click the &#xFF0B; at the bottom to select the Python script.<br/>
If the script settings load, then you're all set!

# Troublshooting
## Incompatible Version of Python
If settings do not appear after attempting to load the script, it could be that your version of OBS is incompatible with your installation of Python.<br/>
Try loading one of the example scripts that OBS provides within the default directory.<br/> 
If settings still do not appear, double check to make sure both OBS and Python are either 32-bit or 64-bit, and that your Python and OBS versions are compatible.<br/> 
## Untested Versions
The script was created using OBS 27.2.4 64-bit and Python 3.6.8, and may not work as intended on different versions.<br/>
I tried my best to use the basics of the OBS API as to ensure it would be forward compatible, but I can't test for everything.<br/>

# License
- [**BSL-1.0 License**](https://github.com/cunkmanjones/obs-easing-python/blob/main/LICENSE.txt)
