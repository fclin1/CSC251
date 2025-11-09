"""
Author: Frank Lin
Email: fclin@ncsu.edu
Class: CSC 251 Fall 2025
Program: Project 2 - Image Blending and Processing
Purpose: Main program
Bugs: None
Acknowledgements: Used Claude to help with blend_P3_images()
"""

from pnmimage import PNMimage, PPMimage


def blend_P3_images(img1, img2):
    """Blend two color images together based on user's percentage"""
    
    # Ask user what percentage of the first image they want
    got_valid_weight = False
    while not got_valid_weight:
        try:
            weight1 = float(input("Enter blending weight of first image as a percent (0-100): "))
            if weight1 >= 0 and weight1 <= 100:
                got_valid_weight = True
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("That's not a valid number. Try again.")
    
    weight2 = 100 - weight1
    
    # Figure out what size the blended image should be
    new_width = min(img1.width, img2.width)
    new_height = min(img1.height, img2.height)
    
    # Create the new blended image
    blended = PPMimage()
    blended.type = "P3"
    blended.comment = f"# blended image {weight1}%/{weight2}%"
    blended.width = new_width
    blended.height = new_height
    blended.max_color = 255
    
    # Blend the pixels
    total_values = new_width * new_height * 3
    
    for i in range(total_values):
        val1 = img1.pixels[i]
        val2 = img2.pixels[i]
        
        blended_val = int((weight1 / 100) * val1 + (weight2 / 100) * val2)
        blended.pixels.append(blended_val)
    
    return blended


def main():
    # Load two P3 images
    image1 = PPMimage()
    image1.load_P3_image()
    
    image2 = PPMimage()
    image2.load_P3_image()
    
    # Blend them together
    blended_img = blend_P3_images(image1, image2)
    
    # Ask what they want to do with the blended image
    print("\nImage processing options:")
    print("1: Convert to grayscale")
    print("2: Convert to sepia")
    print("3: No further processing")
    
    option = input("Enter processing option: ")
    
    # Process based on their choice
    if option == '1':
        final_img = blended_img.convert_to_BW()
        extension = ".pgm"
        description = "grayscale"
    elif option == '2':
        final_img = blended_img.convert_to_sepia()
        extension = ".ppm"
        description = "sepia"
    else:
        final_img = blended_img
        extension = ".ppm"
        description = "color"
    
    # Get output filename and validate extension
    valid_filename = False
    while not valid_filename:
        output_file = input("Enter output filename: ")
        if output_file.endswith(extension):
            valid_filename = True
        else:
            print(f"Filename must end with {extension}")
    
    # Save the image and output
    final_img.output_image(output_file)
    
    print(f"\nOutput file for {description} blended image: {output_file}")
    print(final_img)


if __name__ == "__main__":
    main()