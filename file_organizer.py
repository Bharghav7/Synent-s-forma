import os
import shutil

# Folder to organize
source_folder = r"C:\Users\BHARGHAV\OneDrive\Desktop\TEST FILES"

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"]
}

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isfile(file_path):
        moved = False

        for folder, extensions in file_types.items():
            if any(filename.lower().endswith(ext) for ext in extensions):

                target_folder = os.path.join(source_folder, folder)
                os.makedirs(target_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(target_folder, filename)
                )

                print(f"Moved {filename} to {folder}")
                moved = True
                break

        if not moved:
            other_folder = os.path.join(source_folder, "Others")
            os.makedirs(other_folder, exist_ok=True)

            shutil.move(
                file_path,
                os.path.join(other_folder, filename)
            )

            print(f"Moved {filename} to Others")

print("File organization completed!")