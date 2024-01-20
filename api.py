from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open an image file
image_path = "C:\\Users\\Aditi Shrivastava\\Desktop\\hack\\pic1.jpg"

# Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(image_path)

# Print the extracted text
print("Extracted Text:")
print(text)
