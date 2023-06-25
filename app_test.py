from flask import Flask, render_template, request
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    # Access the captured image file
    image_file = request.files['image']

    # Save the image to disk
    image_path = 'captured_image.jpg'
    image_file.save(image_path)

    # Process the captured image (e.g., display it or perform further operations)
    # For this example, we'll simply display the image on the webpage
    return render_template('capture.html', image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)
