import os
import shutil

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".webm"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".rtf", ".odt"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
    "Executables": [".exe", ".msi", ".bat", ".sh", ".apk", ".dmg", ".pkg", ".deb"],
    "Code": [".py", ".js", ".java", ".c", ".cpp", ".cs", ".html", ".css", ".php", ".rb", ".go", ".ts"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2"],
    "Design": [".psd", ".ai", ".xd", ".fig", ".sketch", ".indd"],
    "Ebooks": [".epub", ".mobi", ".azw", ".azw3", ".cbz", ".cbr"],
    "Spreadsheets": [".csv", ".xls", ".xlsx", ".ods"],
    "Others": []
}

def make_folders():
    for category, ext in file_types.items():
        folder_name = category
        os.makedirs(folder_name, exist_ok=True)

def check_existence(filename,folder):
    directory = os.listdir(folder)
    files=[]
    for f in directory:
        file_path=os.path.join(folder,f)
        if os.path.isfile(file_path):
            files.append(f)
    for f in files:
        if filename==f:
            return True
    return False

def rename(filename, folder):
    file, ext = os.path.splitext(filename)
    count = 1
    new_name = filename
    while check_existence(new_name, folder):
        new_name=f"{file}_{count}{ext}"
        count+=1
    return new_name


def move_files():
    for file in os.listdir():
        if os.path.isfile(file):
            extension = os.path.splitext(file)[1].lower()
            moved = False
            for category, ext in file_types.items():
                if extension in ext:
                    file_name_to_use = rename(file, category)
                    shutil.move(file, os.path.join(category, file_name_to_use))
                    moved = True
                    break
            if not moved:
                file_name_to_use = rename(file, "Others")
                shutil.move(file, os.path.join("Others", file_name_to_use))
        
make_folders()
move_files()
