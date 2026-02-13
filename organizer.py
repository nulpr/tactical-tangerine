def filesOrganizer(path):
    import os
    import shutil

    def move_files_by_category(files, extensions, folder_name):
        matching_files = [
            f for f in files
            if any(f.lower().endswith(ext) for ext in extensions)
        ]
        
        if matching_files:
            for file in matching_files:
                ext = file.split('.')[-1].lower()
            
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
            
            for file in matching_files:
                source_path = os.path.join(os.curdir, file)
                dest_path = os.path.join(folder_name, file)
                shutil.move(source_path, dest_path)

    file_categories = {
        'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'svg', 'webp'],
        'Documents': ['pdf', 'doc', 'docx', 'txt', 'odt', 'rtf', 'xls', 'xlsx', 'ppt', 'pptx', 'csv', 'epub', 'html'],
        'Compressed': ['zip', 'rar', '7z', 'tar', 'gz', 'tar.gz', 'bz2', 'xz', 'deb', 'tar.xz', 'tgz', 'iso'],
        'Executables': ['exe', 'msi', 'bat', 'apk', 'xapk'],
        'Audio': ['mp3', 'wav', 'aac', 'flac'],
        'Video': ['mp4', 'mkv', 'avi', 'mov'],
    }

    while True:
        directory = path
        
        if not os.path.isdir(directory):
            print('Directory is not a folder.')
            continue
        
        os.chdir(directory)
        files_in_dir = os.listdir()
        
        for category, extensions in file_categories.items():
            move_files_by_category(files_in_dir, extensions, category)
        
        break
