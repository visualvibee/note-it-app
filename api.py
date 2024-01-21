from PIL import Image
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open an image file
image_path = r"C:\Users\Aditi Shrivastava\Desktop\hack\pic1.jpg"

try:
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(Image.open(image_path))

    # Print the extracted text
    print("Extracted Text:")
    print(text)

except Exception as e:
    print("Error:", e)
