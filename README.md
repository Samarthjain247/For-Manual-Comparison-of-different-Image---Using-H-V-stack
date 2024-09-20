# For-Manual-Comparison-of-different-Image---Using-H-V-stack

Image Reading and Resizing: It reads images from different folders and ensures all images are resized to the same dimensions for consistency.
Image Stacking: The code organizes images into two rows (4 images per row), then horizontally stacks them within each row and vertically stacks the two rows.
Image Placeholder: If an image is missing from a checkpoint folder, it adds a blank image as a placeholder to maintain layout structure.
Saving Stacked Images: Each processed and stacked image is saved as a separate output file in a designated folder.
       When it can be use:
Comparative Visualization
Batch Image Processing
