# 
A simple Python utility that backups and organizes files and folders to another location locally.

# Features
- Configurable JSON file with source path and the backup folder path compatible with Windows and Linux. (not tested in MacOS)
- Extension based file sorting
- Multiple folders of interest to backup (FUTURE)
# Installation
## Requirements
- Python 3.14.X
- Standard library modules used:
	- shutil
	- os
	- pathlib
	- json
Clone the repo with:
`
```bash
git clone https://github.com/kernl-dev/tactical-tangerine.git
cd tactical-tangerine
python main.py
```
## Configuration
Inside the repo folder you can find the file `config.json`. Opening it, you should see something like:
```json
{
    "sourceFolder": "/path/to/source",
    "backupFolder": "/path/to/backup"
}
```
That's your config file. Make sure to put a valid path with permission to write, otherwise it's gonna rise a permission error.
# Usage
## JSON File
When running for the first time, the JSON file should be automatically created and asked for a path for each destination only once since the program checks if the file exists each time you run it. If the file exists it'll assume it holds a valid path. If you encounter any error with the config file, make sure to check if the quotes aren't empty. 

In case the config file is not automatically created, you can always create it manually as long as it's in the right format.

You can also choose a different folder to place the config file. For that, you're gonna have to go to the ```main.py``` file and look for the line that looks like this:
```python
mainFolder = Path('.')
```
Modify it to the desired path where you wish to hold your config and you're ready to go. Just a reminder, it checks each file until it finds one called ```config.json```, so be aware to avoid any conflicts with an existing file.
## File Sorting
Inside the main folder, there's a file called ```organizer.py```. There you can find the whole sorting logic, so if you happen to notice a certain extension you work with is not being properly sorted, you'll want to go the file and add your desired extension to the list.
# Known Limitations
- No GUI
- Currently overwrites files
- Few error handlers
- No version control
- No background running
# To-Do
- [ ] Multiple folders of interest
- [ ] Background running
- [ ] Version control
- [ ] Frequency control
