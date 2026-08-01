import os
import shutil

# Specify the directory you want to organize
target_dir = r"c:\Users\short\Desktop\file"

# Dictionary mapping extensions to folder names
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Code": [".py", ".html", ".css", ".js"]
}

def organize_files():
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)
        
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue
            
        file_ext = os.path.splitext(filename)[1].lower()
        
        moved = False
        for folder_name, exts in folders.items():
            if file_ext in exts:
                folder_path = os.path.join(target_dir, folder_name)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved: {filename} -> {folder_name}")
                moved = True
                break
                
        if not moved:
            other_path = os.path.join(target_dir, "Others")
            os.makedirs(other_path, exist_ok=True)
            shutil.move(file_path, os.path.join(other_path, filename))
            print(f"Moved: {filename} -> Others")

if __name__ == "__main__":
    organize_files()
    print("Organization Complete!")