import os
import cv2
import numpy as np

# Path to the parent folder containing checkpoint folders
parent_folder = '/Users/samarthjain/Downloads/processed_images_PPO'

# Specific checkpoint folder containing the 30 images
checkpoint_folder = '/Users/samarthjain/Downloads/processed_images_PPO/ckpt1'

# List all image names within the checkpoint folder
image_folder_path = os.path.join(parent_folder, checkpoint_folder)
image_names = os.listdir(image_folder_path)

# List of checkpoint folders (assuming their names are 'ckpt1' to 'ckpt8')
checkpoint_folders = ['ckpt1', 'ckpt2', 'ckpt3', 'ckpt4',
                      'ckpt5', 'ckpt6', 'ckpt7', 'ckpt8']

# Initialize a variable to store the width and height of the images
image_width = None
image_height = None

# Create a folder to save the output images
output_folder = '/Users/samarthjain/Downloads/30_images_4x4'
os.makedirs(output_folder, exist_ok=True)

# Iterate through each image name in the checkpoint folder
for image_name in image_names:
    # Initialize lists to store images for current image name
    row1_images = []
    
    row2_images = []

    # Iterate through each checkpoint folder
    for folder in checkpoint_folders:
        # Construct path to the image in the current checkpoint folder
        image_path = os.path.join(parent_folder, folder, image_name)

        # Check if the image file exists
        if os.path.exists(image_path):
            # Read the image
            image = cv2.imread(image_path)

            # Ensure all images have the same dimensions
            if image_width is None or image_height is None:
                image_height, image_width, _ = image.shape
            else:
                image = cv2.resize(image, (image_width, image_height))

            # Append the image to the respective row
            if len(row1_images) < 4:
                row1_images.append(image)
            else:
                row2_images.append(image)
        else:
            print(f"Image not found in {folder}")
            # Append a blank image
            row1_images.append(np.zeros((image_height, image_width, 3), dtype=np.uint8))  # Placeholder for blank image
            row2_images.append(np.zeros((image_height, image_width, 3), dtype=np.uint8))  # Placeholder for blank image

    # Stack images horizontally for each row
    row1_stacked = np.hstack(row1_images)
    row2_stacked = np.hstack(row2_images)

    # Stack rows vertically
    final_image = np.vstack((row1_stacked, row2_stacked))

    # Save the final stacked image as a separate file
    output_path = os.path.join(output_folder, f'stacked_{image_name}')
    cv2.imwrite(output_path, final_image, [cv2.IMWRITE_PNG_COMPRESSION, 0])

    print(f"Stacked image saved to {output_path}")

print("All 30 images saved successfully.")
