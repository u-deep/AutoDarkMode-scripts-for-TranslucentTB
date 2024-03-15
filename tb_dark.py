import os
import shutil

def main():
    dark_settings_source = "C:/Users/udeep/AppData/Roaming/AutoDarkMode/darksettings.json"
    destination_folder = "C:/Users/udeep/AppData/Local/Packages/28017CharlesMilette.TranslucentTB_v826wp6bftszj/RoamingState"
    destination_path = os.path.join(destination_folder, "settings.json")

    try:
        shutil.copy2(dark_settings_source, destination_path)
        print("File darksettings.json copiato e sovrascritto con successo.")

    except FileNotFoundError:
        print("Impossibile trovare il file darksettings.json.")
    except PermissionError:
        print("Permessi insufficienti per eseguire l'operazione.")

if __name__ == "__main__":
    main()