from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fpdf import FPDF
from PIL import Image
from typing import List
import os

app = FastAPI()

def convert_images_to_pdf(image_paths, output_pdf_path):
    pdf = FPDF()
    for image_path in image_paths:
        image = Image.open(image_path)
        pdf.add_page()
        pdf.image(image_path, x=0, y=0, w=210, h=297)  # Adjust dimensions as needed
    pdf.output(output_pdf_path)

@app.post("/convert-to-pdf/")
async def convert_to_pdf(files: List[UploadFile] = File(...)):
    image_paths = []
    for file in files:
        image_path = f"temp_{file.filename}"
        with open(image_path, "wb") as f:
            f.write(await file.read())
        image_paths.append(image_path)

    output_pdf_path = "output.pdf"
    convert_images_to_pdf(image_paths, output_pdf_path)

    # Cleanup temporary image files
    for image_path in image_paths:
        os.remove(image_path)

    return FileResponse(output_pdf_path, media_type="application/pdf", filename=output_pdf_path)

# Run the application using the command below:
# uvicorn main:app --reload
