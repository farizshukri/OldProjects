from PIL import Image, ImageDraw
import os

# Function to generate and save an image
def generate_image(width, height, color, output_dir, filename):
    # Create a new image with the specified color
    image = Image.new("RGB", (width, height), color)
    
    # Save the image to the output directory
    image.save(os.path.join(output_dir, filename))
    
    print(f"Image saved: {filename}")

def main():
    # Define parameters for the image
    width = 800
    height = 600
    color = (255, 0, 0)  # Red color, in RGB format
    output_directory = 'generated_images'
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    # Generate and save the image
    generate_image(width, height, color, output_directory, 'red_image.png')

if __name__ == "__main__":
    main()
