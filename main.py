from fastapi import FastAPI, UploadFile, File
from fpdf import FPDF
from PIL import Image
from io import BytesIO
from starlette.responses import Response

app = FastAPI()

@app.post("/convert_images_to_pdf")
async def convert_images_to_pdf(images: list[UploadFile] = File(...)):
    pdf = FPDF()
    for image in images:
        image_data = await image.read()
        image_pil = Image.open(BytesIO(image_data))
        pdf.add_page()
        pdf.image(BytesIO(image_data), x=0, y=0, w=210, h=297)  # Adjust dimensions as needed
    pdf_buffer = BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)
    return Response(pdf_buffer.read(), media_type="application/pdf", headers={"Content-Disposition": f"attachment; filename=converted_images.pdf"})
