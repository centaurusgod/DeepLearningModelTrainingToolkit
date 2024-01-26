import os
import shutil
import random

def split_data(input_folder, output_folder, train_ratio=0.9, val_ratio=0.05, test_ratio=0.05):
    # Create output folders if they don't exist
    for folder in ['train', 'val', 'test']:
        os.makedirs(os.path.join(output_folder, folder), exist_ok=True)

    # Iterate over each class folder in the input data folder
    for class_folder in os.listdir(input_folder):
        class_path = os.path.join(input_folder, class_folder)

        if os.path.isdir(class_path):
            # Create class folders in train, val, and test
            for split_folder in ['train', 'val', 'test']:
                os.makedirs(os.path.join(output_folder, split_folder, class_folder), exist_ok=True)

            # Get list of files in the class folder
            files = [os.path.join(class_path, file) for file in os.listdir(class_path)]
            num_files = len(files)

            # Calculate the number of files for each split
            num_train = int(num_files * train_ratio)
            num_val = int(num_files * val_ratio)
            num_test = int(num_files * test_ratio)

            # Randomly shuffle the list of files
            random.shuffle(files)

            # Move files to train folder
            for file in files[:num_train]:
                dest_path = os.path.join(output_folder, 'train', class_folder, os.path.basename(file))
                shutil.move(file, dest_path)

            # Move files to val folder
            for file in files[num_train:num_train + num_val]:
                dest_path = os.path.join(output_folder, 'val', class_folder, os.path.basename(file))
                shutil.move(file, dest_path)

            # Move files to test folder
            for file in files[num_train + num_val:num_train + num_val + num_test]:
                dest_path = os.path.join(output_folder, 'test', class_folder, os.path.basename(file))
                shutil.move(file, dest_path)

if __name__ == "__main__":
    input_folder = 'data'  # Change this to the name of your data folder
    output_folder = '.'  # Output folders will be created in the same directory as the script

    split_data(input_folder, output_folder)
