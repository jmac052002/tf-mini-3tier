import os
import shutil
# Replace this with the folder you want to organize
target_folder = "C:/Users/jmac0/Downloads" 

#Dictionary to hold file extensions and their corresponding folder names
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp"]
}
def organize(folder):
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        _, ext = os.path.splitext(file_name)

        # Find the right category
        found = False
        for category, extensions in file_types.items():
            if ext.lower() in extensions:
                category_folder = os.path.join(folder, category)
                os.makedirs(category_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(category_folder, file_name))
                print(f"Moved {file_name} to {category}/")
                found = True
                break

        if not found:
            other_folder = os.path.join(folder, 'Others')
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, file_name))
            print(f"Moved {file_name} to Others/")
if __name__ == "__main__":
    organize(target_folder)
