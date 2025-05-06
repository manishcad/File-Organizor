import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return
    
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        
        if os.path.isfile(file_path):
            file_extension = file.split('.')[-1].lower()
            if file_extension == file:
                file_extension = "Unknown"  # Handle files with no extension
            
            folder_path = os.path.join(directory, file_extension.upper())
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            shutil.move(file_path, os.path.join(folder_path, file))
            print(f"Moved '{file}' to '{folder_path}'")

if __name__ == "__main__":
    folder_to_organize = input("Enter the directory to organize: ")
    organize_files(folder_to_organize)
