import os
from asposepdf import Document, Image, Rectangle

# Set the input and output file paths
input_file = 'input.pdf'
output_file = 'output.pdf'
image_file = 'image.jpg'

# Load the input PDF document
document = Document(input_file)

# Load the image
image = Image()
image.File = image_file

# Create a new page in the PDF document
page = document.Pages.Add()

# Set the position and size of the image on the page
image.Rectangle = Rectangle(20, 730, 120, 830)

# Add the image to the page
page.Paragraphs.Add(image)

# Save the modified PDF document
document.Save(output_file)

print(f"PDF created: {output_file}")
