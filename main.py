from pathlib import Path
import os   # I'm gonna use this to navigate because I don't know how to use pathlib :)
import shutil
import json
from organizer import filesOrganizer
import datetime

configFile = 'config.json'
config = Path(configFile)
userPaths = {'sourceFolder': '',
             'backupFolder' : ''}
mainFolder = Path('.')
versionFolderName = datetime.datetime.now().strftime('%Y-%m-%d')

#   Writing config file
def writeConfig():
    with open(configFile, 'w') as file:
        json.dump(userPaths, file, indent=4)
    print(f"Configuration saved to {configFile}")

def copyFiles(source, dest):
    for root, dirs, files in os.walk(source):
        for file in files:
            source_file = os.path.join(root, file)

            # Preserve folder structure
            relative_path = os.path.relpath(root, source)
            target_dir = os.path.join(dest, relative_path)

            os.makedirs(target_dir, exist_ok=True)

            dest_file = os.path.join(target_dir, file)
            shutil.copy2(source_file, dest_file)

def versionBackup(backup, version_dest):
    backup = os.path.abspath(backup)
    version_dest = os.path.abspath(version_dest)

    for item in os.listdir(backup):
        source_path = os.path.join(backup, item)

        # Skip other version folders (date-formatted ones)
        if os.path.isdir(source_path):
            # crude but effective: skip folders that look like YYYY-MM-DD
            if len(item) == 10 and item[4] == '-' and item[7] == '-':
                continue

        dest_path = os.path.join(version_dest, item)

        if os.path.isdir(source_path):
            shutil.copytree(source_path, dest_path, dirs_exist_ok=True)
        else:
            shutil.copy2(source_path, dest_path)

#   Checking if config file exists
if config.exists():
    with open("config.json", 'r') as f:
        userPaths = json.load(f)
elif not config.exists():
    source = input('Source folder path: ')
    dest = input('Backup folder path: ')
    userPaths['sourceFolder'] = source
    userPaths['backupFolder'] = dest
    writeConfig()
else:
    print("idk what's happening, sorry")

backup_folder = Path(userPaths['backupFolder'])
versionFolder = backup_folder / versionFolderName

# Check if backup already has files (previous run)
if backup_folder.exists() and any(backup_folder.iterdir()):
    print("Duplicates found. Creating version backup.")
    versionFolder.mkdir(parents=True, exist_ok=True)
    versionBackup(userPaths['backupFolder'], versionFolder)
else:
    print("No duplicates were found.")


copyFiles(userPaths['sourceFolder'], userPaths['backupFolder'])
        
print("All files were copied")
print("Organizing files")

filesOrganizer(backup_folder)

print("Files organized")