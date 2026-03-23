# Tactical Tangerine 🍊

A lightweight Python utility for backing up and organizing files to another local destination, with extension-based sorting and simple JSON configuration.

> ⚠️ **Warning:** Bugs may still exist. Always keep important data backed up in a secure, separate location. The author is not responsible for lost or overwritten files — use at your own risk.

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [File Sorting](#file-sorting)
- [Known Limitations](#known-limitations)
- [To-Do](#to-do)

---

## Features

- Simple JSON-based configuration with support for **Windows** and **Linux** paths *(macOS untested)*
- Extension-based automatic file sorting
- Automatic config file generation on first run

---

## Requirements

- Python 3.14+
- Standard library only — no external dependencies:
  - `shutil`
  - `os`
  - `pathlib`
  - `json`

---

## Installation

Clone the repository and run the script:

```bash
git clone https://github.com/nulpr/tactical-tangerine.git
cd tactical-tangerine
python main.py
```

---

## Configuration

Tactical Tangerine uses a `config.json` file to define the source and backup folder paths.

### Automatic setup

On the first run, the program will automatically create `config.json` and prompt you to enter the required paths. On subsequent runs, it will detect the existing file and use it directly.

> If you encounter errors related to the config file, check that the path values are not empty strings.

### Manual setup

If the config file is not created automatically, you can create it manually. It must follow this format:

```json
{
  "sourceFolder": "/path/to/source",
  "backupFolder": "/path/to/backup"
}
```

Make sure the paths point to locations where you have **write permissions**, otherwise a permission error will be raised.

### Path format by OS

| OS      | Separator | Example                        |
|---------|-----------|--------------------------------|
| Linux   | `/`       | `/home/user/documents`         |
| Windows | `\\`      | `C:\\Users\\user\\documents`   |

### Custom config location

By default, the config file is expected in the current working directory. To change this, open `main.py` and modify the following line:

```python
mainFolder = Path('.')
```

Replace `Path('.')` with your desired directory path. Note that the program scans for a file named exactly `config.json`, so avoid naming conflicts with existing files in that location.

---

## Usage

After configuring your paths, simply run:

```bash
python main.py
```

The program will copy and organize files from your source folder into the backup folder.

---

## File Sorting

File sorting logic is defined in `organizer.py`. Files are categorized and moved into subfolders based on their extension.

If an extension you work with is not being sorted correctly, open `organizer.py` and add the extension to the appropriate list.

---

## Known Limitations

- No GUI
- Limited error handling
- No background or scheduled running

---

## To-Do

- [ ] Multiple source folders support
- [ ] Background running / scheduled backups
- [ ] Frequency control
- [x] Version control