import fitz  
import os
def extract_images_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    img_count = 0  # Image counter
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # Load page
        image_list = page.get_images(full=True)  # Get all images on the page
        for img_index, img in enumerate(image_list):
            xref = img[0]  # The image's reference number
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]  # Get image data as bytes
            image_filename = f"image_{page_num + 1}_{img_count + 1}.png"  # Unique image filename
            img_count += 1
            image_path = image_filename
            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)
            print(f"Image saved as: {image_path}")
    print(f"Extraction completed. {img_count} ")
pdf_file_path = "Certificado de titulo en tramite.pdf"  
extract_images_from_pdf(pdf_file_path)
