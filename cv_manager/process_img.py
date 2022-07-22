import cv2
import pytesseract


from cv_manager.common import find_email, find_name, find_phone, find_skills


def get_text_from_image(file_path):
    """
        This function will take file path as a param and will return text data
        file_path: Path of the doc file
        Created by: Naveen Singh
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
    img = cv2.imread('page2.jpg')
    img = get_grayscale(img)
    img = thresholding(img)
    img = remove_noise(img)


    print(ocr_core(img))


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

        Created by: Naveen Singh
    """
    text_content = get_text_from_file(file_path)

    extracted_data = {
        "name": find_name(text_content),
        "email": find_email(text_content),
        "phone": find_phone(text_content),
        "skills": find_skills(text_content)
    }
    return extracted_data