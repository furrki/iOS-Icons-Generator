# iOS Icon Generator
I developed that tool in order to generate my resized icons for iOS Applications at once! With help of this application, you can generate every needed sizes of AppIcon or Icons for Toolbars/Tabbars (32 x 32).

This application was developed for iOS 12 and Swift 4.2 (But the outputs can be used in past versions too).

# Installation
```
git clone https://github.com/furrki/iOS-Icons-Generator
cd iOS-Icons-Generator
pip install -r requirements.txt
```
# Usage
If you want to generate AppIcons:
```
python main.py -i [Image File Path]
```

Else if you want to generate icons for Tabbars/Toolbars etc.
```
python main.py -i [Image File Path] -t i -n [Icon Name]
```

# ScreenShots 
**AppIcon**<br /><br />
![Alt text](screenshots/ss1.PNG?raw=true "Main Screen")
__________________________________________________________
**Normal Icon**<br /><br />
![Alt text](screenshots/ss2.PNG?raw=true "Main Screen 2")

# Author
furrki
