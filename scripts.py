import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askdirectory

def organize_files_by_extension(directory):
    file_types = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'documents': ['.txt', '.pdf', '.docx', '.xlsx', '.pptx'],
        'videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'audios': ['.mp3', '.wav', '.flac'],
        'archives': ['.zip', '.tar', '.rar', '.gz'],
        'others': []
    }

    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(filename)[1].lower()
        target_folder = 'others'
        for category, extensions in file_types.items():
            if file_extension in extensions:
                target_folder = category
                break

        category_folder = os.path.join(directory, target_folder)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        target_file_path = os.path.join(category_folder, filename)
        shutil.move(file_path, target_file_path)
        print(f"Moved: {filename} -> {target_folder}/")
Tk().withdraw()
directory_path = askdirectory(title="Select the directory to organize")
organize_files_by_extension(directory_path)