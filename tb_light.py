import os
import shutil

def main():
    light_settings_source = "C:/Users/udeep/AppData/Roaming/AutoDarkMode/lightsettings.json"
    destination_folder = "C:/Users/udeep/AppData/Local/Packages/28017CharlesMilette.TranslucentTB_v826wp6bftszj/RoamingState"
    destination_path = os.path.join(destination_folder, "settings.json")

    try:
        shutil.copy2(light_settings_source, destination_path)
        print("File lightsettings.json copiato e sovrascritto con successo.")

    except FileNotFoundError:
        print("Impossibile trovare il file lightsettings.json.")
    except PermissionError:
        print("Permessi insufficienti per eseguire l'operazione.")

if __name__ == "__main__":
    main()
