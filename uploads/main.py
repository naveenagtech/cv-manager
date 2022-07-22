# import module
from pdf2image import convert_from_path, convert_from_bytes


# Store Pdf with convert_from_path function
images = convert_from_path('sample-pdf-download-10-mb.pdf',500)

# for i in range(len(images)):

    # Save pages as images in the pdf
    # images[i].save('page'+ str(i) +'.jpg', 'JPEG')
# images[0].save("page.jpg", 'JPEG')

images = convert_from_bytes(open('sample.pdf', 'rb').read())
images[0].save("page.jpg", 'JPEG')