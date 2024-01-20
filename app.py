from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/extract_text', methods=['POST'])
def extract_text():
    return render_template('index.html')
    data = request.get_json()
    image_data = data.get('image')

    # Implement text extraction logic here
    # This is a placeholder statement
    extracted_text = "Hello, this is extracted text from the image."

    return jsonify({'text': extracted_text})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
