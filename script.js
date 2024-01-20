function extractText() {
    const input = document.getElementById('imageInput');
    const resultContainer = document.getElementById('result');

    const file = input.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const img = new Image();
            img.src = e.target.result;

            img.onload = function () {
                // Use API here to extract text from the image
                // Placeholder Endpoint
                // Replace 'YOUR_OCR_API_ENDPOINT' with the actual endpoint
                const ocrApiEndpoint = 'YOUR_OCR_API_ENDPOINT';

                // Send image data to the backend
                fetch(ocrApiEndpoint, {
                    method: 'POST',
                    body: JSON.stringify({ image: e.target.result }),
                    headers: {
                        'Content-Type': 'application/json',
                    },
                })
                .then(response => response.json())
                .then(data => {
                    resultContainer.textContent = data.text;
                })
                .catch(error => {
                    console.error('Error:', error);
                    resultContainer.textContent = 'Error extracting text.';
                });
            };
        };
        reader.readAsDataURL(file);
    } else {
        resultContainer.textContent = 'Please select an image.';
    }
}
function downloadText(text) {
    const blob = new Blob([text], { type: 'text/plain' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'extracted_text.txt';
    a.style.display = 'none'; // Hide the anchor element
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}
