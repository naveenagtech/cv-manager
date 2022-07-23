import cv2
import pytesseract
from cv_manager.common import find_email, find_name, find_phone, find_skills
from cv_manager.converter import pdf_to_img


def get_text_from_img(file_path):
    """
        This function will take file path as a param and will return text data
        file_path: Path of the PDF file
        Created by: Sumit Saurav
    """
    
    def ocr_core(img):
        text = pytesseract.image_to_string(img)
        return text

    # Get Grayscale image
    def get_grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Noise Removal
    def remove_noise(image):
        return cv2.medianBlur(image, 5)

    # Thresholding
    def thresholding(image):
        return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\sumit.saurav\AppData\Local\Tesseract-OCR\tesseract.exe'

    images = pdf_to_img(file_path)
    text_content = ""

    for img in images:
        img.save('page.jpg', 'JPEG')

        # Retrieve text from each Images
        img = cv2.imread('page.jpg')
        img = get_grayscale(img)
        img = thresholding(img)
        img = remove_noise(img)
        text_content += ocr_core(img)

    return text_content


def get_data_from_doc(file_path):
    """
        Returns the response in below format
        text_content: Text data extracted from doc file with the help of get_text_from_file function
        {
            "name": "Name",
            "email": "Email",
            "phone": "Phone",
            "skills": ["skill1", "skill2"]
        }

        Created by: Sumit Saurav
    """
    text_content = get_text_from_img(file_path)

    extracted_data = {
        "name": find_name(text_content),
        "email": find_email(text_content),
        "phone": find_phone(text_content),
        "skills": find_skills(text_content)
    }

    return extracted_data