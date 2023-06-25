# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 11:32:12 2023

@author: sunum
"""


from fpdf import FPDF

# Create FPDF object
pdf = FPDF()

# Add a page
pdf.add_page()

# Set the font
pdf.set_font("Arial", size=15)

# Add text
pdf.cell(200, 10, txt="GeeksforGeeks", ln=1, align='C')
pdf.cell(200, 10, txt="A Computer Science portal for geeks.", ln=2, align='C')

# Add image
pdf.image("D:/sdpro/IAP/IAP/test2/guitar_cordd.jpg", x=10, y=50, w=100, h=100)  # Replace "path/to/image.jpg" with the actual image path

# Save the PDF
pdf.output("output.pdf")
