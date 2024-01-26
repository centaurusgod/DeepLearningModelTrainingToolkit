import os

def rename_images_in_subfolders(data_folder):
    for folder_name in os.listdir(data_folder):
        folder_path = os.path.join(data_folder, folder_name)

        # Check if it's a directory
        if os.path.isdir(folder_path):
            # Get a list of all files in the subfolder
            files_in_folder = os.listdir(folder_path)

            # Filter only the image files (you may customize the extension list)
            image_files = [f for f in files_in_folder if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

            # Rename each image file
            for i, file_name in enumerate(image_files, start=1):
                # Create the new name by combining the folder name, a space, and the index
                new_name = f"{folder_name} {i}"

                # Build the full paths for the old and new names
                old_path = os.path.join(folder_path, file_name)
                new_path = os.path.join(folder_path, f"{new_name}{os.path.splitext(file_name)[1]}")

                # Rename the file
                os.rename(old_path, new_path)

                print(f"Renamed: {os.path.join(folder_name, file_name)} -> {os.path.join(folder_name, new_name)}")

# Example usage: place the script in the root folder containing the 'data' folder
data_folder = 'data'  # Change this to the actual data folder name if needed

rename_images_in_subfolders(data_folder)
