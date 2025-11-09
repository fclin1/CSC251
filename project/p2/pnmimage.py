"""
Author: Frank Lin
Email: fclin@ncsu.edu
Class: CSC 251 Fall 2025
Program: Project 2 - Image Blending and Processing
Purpose: Defines PNMimage and PPMimage classes
Bugs: None
Acknowledgements: Used Claude to help with load_P3_image()
"""


class PNMimage:
    """Superclass for P2 and P3 Netpbm images"""
    
    def __init__(self, type="", comment="", width=0, height=0, max_color=0):
        self.type = type
        self.comment = comment
        self.width = width
        self.height = height
        self.max_color = max_color
        self.pixels = []
    
    def output_image(self, filename):
        """Write the image data to a file"""
        with open(filename, 'w') as f:
            f.write(f"{self.type}\n")
            f.write(f"{self.comment}\n")
            f.write(f"{self.width} {self.height}\n")
            f.write(f"{self.max_color}\n")
            
            for pixel_value in self.pixels:
                f.write(f"{pixel_value}\n")
    
    def __str__(self):
        result = f"{self.comment}\n"
        result += f"Type: {self.type}\n"
        result += f"Width: {self.width} Height: {self.height}"
        return result


class PPMimage(PNMimage):
    """Subclass for P3 color images"""
    
    def __init__(self):
        super().__init__()
    
    def load_P3_image(self):
        """Load a P3 image file - keeps asking until we get a valid one"""
        file_loaded = False
        
        while not file_loaded:
            try:
                filename = input("Enter input filename for image: ")
                file = open(filename, 'r')
                lines = file.readlines()
                file.close()
                
                # Parse the header: type, dimensions, max color, and comment
                header_parts = []
                i = 0
                
                while len(header_parts) < 3 and i < len(lines):
                    line = lines[i].strip()
                    
                    if line.startswith('#'):
                        self.comment = line
                    elif line:  # not empty
                        header_parts.append(line)
                    
                    i += 1
                
                # Check if it's a P3 file
                self.type = header_parts[0]
                if self.type != "P3":
                    print("This file is not in PPM P3 format.")
                    continue
                
                # Dimensions and max color
                dims = header_parts[1].split()
                self.width = int(dims[0])
                self.height = int(dims[1])
                self.max_color = int(header_parts[2])
                
                # Pixel values
                self.pixels = []
                for line in lines[i:]:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        self.pixels.append(int(line))
                
                file_loaded = True
                
            except FileNotFoundError:
                print(f"[Errno 2] No such file or directory: '{filename}'")
                print("Enter input filename again: ", end="")
            except (ValueError, IndexError):
                print("This file is not in PPM P3 format.")
                print("Enter input filename again: ", end="")
    
    def convert_to_BW(self):
        """Convert color image to grayscale"""
        bw_img = PNMimage()
        bw_img.type = "P2"
        bw_img.comment = self.comment + ", converted to grayscale"
        bw_img.width = self.width
        bw_img.height = self.height
        bw_img.max_color = self.max_color
        
        # Convert RGB triplets to grayscale values
        for i in range(0, len(self.pixels), 3):
            r = self.pixels[i]
            g = self.pixels[i + 1]
            b = self.pixels[i + 2]
            
            gray_value = int(0.30 * r + 0.60 * g + 0.10 * b)
            bw_img.pixels.append(gray_value)
        
        return bw_img
    
    def convert_to_sepia(self):
        """Convert color image to sepia tones"""
        sepia_img = PPMimage()
        sepia_img.type = "P3"
        sepia_img.comment = self.comment + ", converted to sepia"
        sepia_img.width = self.width
        sepia_img.height = self.height
        sepia_img.max_color = self.max_color
        
        # Process each pixel's RGB values
        for i in range(0, len(self.pixels), 3):
            r = self.pixels[i]
            g = self.pixels[i + 1]
            b = self.pixels[i + 2]
            
            # Apply sepia formulas
            new_r = int(0.393 * r + 0.769 * g + 0.189 * b)
            new_g = int(0.349 * r + 0.686 * g + 0.168 * b)
            new_b = int(0.272 * r + 0.534 * g + 0.131 * b)
            
            # Cut off at 255
            if new_r > 255:
                new_r = 255
            if new_g > 255:
                new_g = 255
            if new_b > 255:
                new_b = 255
            
            sepia_img.pixels.append(new_r)
            sepia_img.pixels.append(new_g)
            sepia_img.pixels.append(new_b)
        
        return sepia_img