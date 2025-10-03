import os
import shutil
import random

# --- 1. DEFINE YOUR PATHS ---

# IMPORTANT: Update this with the path you copied from the Kaggle file explorer
# It will look something like '/kaggle/gcs/your_drive_name/path/to/your/dataset'
source_dir = 'train' # <--- CHANGE THIS

# This is where the new organized dataset will be created in your Kaggle environment
base_dest_dir = 'split_data'


# --- 2. CREATE THE NEW DIRECTORY STRUCTURE (This part remains the same) ---
train_dir = os.path.join(base_dest_dir, 'train')
test_dir = os.path.join(base_dest_dir, 'val') # Using 'val' for the test/validation set

os.makedirs(os.path.join(train_dir, 'Fire'), exist_ok=True)
os.makedirs(os.path.join(train_dir, 'No_Fire'), exist_ok=True)
os.makedirs(os.path.join(test_dir, 'Fire'), exist_ok=True)
os.makedirs(os.path.join(test_dir, 'No_Fire'), exist_ok=True)

print(f"Created new directory structure at: {base_dest_dir}")


# --- 3. SPLIT THE DATA (This part remains the same) ---
def split_class_data(class_name, split_ratio=0.8):
    class_source_path = os.path.join(source_dir, class_name)
    train_dest_path = os.path.join(train_dir, class_name)
    test_dest_path = os.path.join(test_dir, class_name)

    # Check if the source directory exists
    if not os.path.exists(class_source_path):
        print(f"ERROR: Source directory not found at '{class_source_path}'. Please check your 'source_dir' path.")
        return

    images = [f for f in os.listdir(class_source_path) if os.path.isfile(os.path.join(class_source_path, f))]
    random.shuffle(images)
    split_index = int(len(images) * split_ratio)
    train_images = images[:split_index]
    test_images = images[split_index:]

    for image in train_images:
        shutil.copy(os.path.join(class_source_path, image), train_dest_path)

    for image in test_images:
        shutil.copy(os.path.join(class_source_path, image), test_dest_path)

    print(f"Class '{class_name}':")
    print(f"  - Total images: {len(images)}")
    print(f"  - Copied to training: {len(train_images)}")
    print(f"  - Copied to testing: {len(test_images)}")

# Run the function for both of your classes
split_class_data('Fire')
split_class_data('No_Fire')

print("\nDataset splitting complete!")