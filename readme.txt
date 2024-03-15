Python 3.12.2 is needed
AutoDarkMode Version:
Commit cf7a0fe
App/Service 10.4.1.1
Updater 3.1.4
Shell 1.3.3.0
.Net 7.0.5
Windows 22631.3296
For different configuration I don't know if it works

Enable Scripts in AutoDarkMode: Scripts --> Enable Custom Scripts ON
copy/paste all the files in C:/Users/$SER_NAME$/AppData/Roaming/AutoDarkMode
If you have already other scripts don't overwrite the file scripts.yaml, in case copy/paste the content of my scripts.yaml into your scripts.yaml
If you don't have any custom scripts overwrite without any issue
TO EDIT:
1)scripts.yaml: set the right paths changing the username
2)tb_dark.py: open it with a text editor and edit the paths of dark_setting_source with the path where is currently the file darksettings.json; change also the destination_folder with the location of the setting file for TranslucentTB
2)tb_light.py: open it with a text editor and edit the paths of light_setting_source with the path where is currently the file darksettings.json; change also the destination_folder with the location of the setting file for TranslucentTB
3)darksettings.json and lightsettings.json contain my favourite presets to be switched you can edit as you prefer
