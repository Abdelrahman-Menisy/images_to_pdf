from fpdf import FPDF
from PIL import Image

def convert_images_to_pdf(image_paths, output_pdf_path):
    pdf = FPDF()
    for image_path in image_paths:
        image = Image.open(image_path)
        pdf.add_page()
        pdf.image(image_path, x = 0, y = 0, w = 210, h = 297)  # Adjust dimensions as needed
    pdf.output(output_pdf_path)

# Example usage
image_paths = ["f12b6bc4e99d57f11d3d281dcf11ea13.jpg", "be65b446-4d20-4786-ac01-e2c512d293b9.jpeg",'d2b5f2fb-52d5-4fba-92e1-703e5cf1ae51.png']
convert_images_to_pdf(image_paths, "output.pdf")
