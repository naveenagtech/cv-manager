import os
# from tkinter import Image
from pdf2image import convert_from_path
from docx2pdf import convert

CONVERTED_DIR = os.path.join(os.getcwd(), "uploads", "converted")

# def doc_to_img(file_path):
#     # Convert the DOC / DOCX file to PDF
#     pdf_path = doc_to_pdf(file_path)

#     # Returns the list of Images converted from DOC / DOCX
#     return pdf_to_img(pdf_path)


def doc_to_pdf(file_path):
    converted_pdf_file_path = CONVERTED_DIR + "\\converted.pdf"
    convert(file_path, converted_pdf_file_path)
    print("Converte PDF path:: " + converted_pdf_file_path)
    return converted_pdf_file_path


def doc_pdf_to_img(file_path):
    # If file is DOC / DOCX then converting it to PDF
    if file_path.endswith(".doc") or file_path.endswith(".docx"):
        print("It's a DOC File...")
        file_path = doc_to_pdf(file_path)
    
    # Store the image in a folder with candidate name
    image_saving_folder_name = file_path.split("\\")[-1].split(".")[0]
    print("Image Saving Folder Name:: " + image_saving_folder_name)


    # Store Pdf with convert_from_path function
    images = convert_from_path(file_path, 500, CONVERTED_DIR + "\\" + image_saving_folder_name)

    # Save the Images
    for i in range(len(images)):
        images[i].save("page" + str(i) + ".jpg", "JPEG")
    # images[0].save("page5.jpg", 'JPEG')

    # Returns the name of folder where the PDF converted images are stored
    return CONVERTED_DIR + "\\" + image_saving_folder_name
    