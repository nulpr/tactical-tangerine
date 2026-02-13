from pathlib import Path
import os   # I'm gonna use this to navigate because I don't know how to use pathlib :)
import shutil
import json
from organizer import filesOrganizer

configFile = 'config.json'
config = Path(configFile)
userPaths = {'sourceFolder': '',
             'backupFolder' : ''}
mainFolder = Path('.')

#   Writing config file
def writeConfig():
    with open(configFile, 'w') as file:
        json.dump(userPaths, file, indent=4)
    print(f"Configuration saved to {configFile}")

#   Checking if config file exists
for i in mainFolder.iterdir():
    if config.exists():
        with open("config.json", 'r') as f:
            userPaths = json.load(f)
        break
    elif not config.exists():
        source = input('Source folder path: ')
        dest = input('Backup folder path: ')
        userPaths['sourceFolder'] = source
        userPaths['backupFolder'] = dest
        writeConfig()
        break
    else:
        print("idk what's happening, sorry")

os.chdir(userPaths['sourceFolder'])

backup_folder = Path(userPaths['backupFolder'])

for root, dirs, files in os.walk(userPaths['sourceFolder']):
    for file in files:
        source_file = os.path.join(root, file)

        # Preserve folder structure
        relative_path = os.path.relpath(root, userPaths['sourceFolder'])
        target_dir = os.path.join(userPaths['backupFolder'], relative_path)

        os.makedirs(target_dir, exist_ok=True)

        dest_file = os.path.join(target_dir, file)
        shutil.copy2(source_file, dest_file)
        
print("All files were copied")
print("Organizing files")

os.chdir(backup_folder)
filesOrganizer(backup_folder)

print("Files organized")