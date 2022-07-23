from pdf2image import convert_from_path
from docx2pdf import convert



def doc_to_img(file_path):
    # Convert the DOC / DOCX file to PDF
    pdf_path = doc_to_pdf(file_path)

    # Returns the list of Images converted from DOC / DOCX
    return pdf_to_img(pdf_path)


def doc_to_pdf(file_path):
    convert(file_path, 'converted.pdf')
    return "converted.pdf"


def pdf_to_img(file_path):
    # Store Pdf with convert_from_path function
    images = convert_from_path(file_path, 500)

    # Save the Images
    # images[0].save("page5.jpg", 'JPEG')

    # Returns the list of Images converted from DOC / DOCX
    return images
    