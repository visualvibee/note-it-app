from flask import Flask, render_template, request
from PIL import Image
import pytesseract

app = Flask(__name__)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' in request.files:
        image = request.files['image']
        img = Image.open(image)
        text = pytesseract.image_to_string(img)
        return render_template('result.html', text=text)
    return 'No image uploaded!'

if __name__ == '__main__':
    app.run(debug=True)
