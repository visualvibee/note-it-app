from flask import Flask, render_template, request
from PIL import Image
import pytesseract
import re
import webbrowser

app = Flask(__name__)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def detect_and_open_link(text):
    # Regular expression to find URLs in the text
    url_pattern = re.compile(r'https?://\S+|www\.\S+')

    # Find all URLs in the text
    urls = re.findall(url_pattern, text)

    if urls:
        for url in urls:
            print(f"Opening link: {url}")
            webbrowser.open(url)
    else:
        print("No links found in the text.")

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    
    if 'image' in request.files:
        image = request.files['image']
        img = Image.open(image)
        img.save('./static/image.png')
        text = pytesseract.image_to_string(img)
        detect_and_open_link(text)
        return render_template('result.html', text=text)
    return 'No image uploaded!'

# New route to handle creating a new note
@app.route('/create_note', methods=['POST'])
def create_note():
    text = request.form.get('text')
    # Implement logic to save the text as a new note (e.g., store in a database)
    return 'New note created successfully!'

if __name__ == '__main__':
    app.run(debug=True)
