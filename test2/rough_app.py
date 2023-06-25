from flask import Flask, render_template, request
import cv2
import os

app = Flask(__name__)

image_path = None



def Encrypted_generated_id(generated_id):
    print("Encrypted_generated_id function ")









def capture_image():
    # Initialize the video capture
    video_capture = cv2.VideoCapture(0)
    
    # Read frame from the webcam
    success, frame = video_capture.read()
    
    if success:
        # Save the captured frame as an image file
        image_path = 'static/captured_image.jpg'
        cv2.imwrite(image_path, frame)
        
        # Release the video capture
        video_capture.release()
        
        return image_path
    
    # If the capture was unsuccessful, return None
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    global image_path  # Declare image_path as a global variable
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'capture':
            # If the "Capture Image" button is clicked, capture an image
            image_path = capture_image()
            print("shitttt of imahe ")
            
        elif action == 'submit':
            # If the "Submit Form" button is clicked, retrieve the form data
            name = request.form.get('name')
            age = request.form.get('age')
            gender = request.form.get('gender')
            arrival_date = request.form.get('arrival_date')
            goats = request.form.get('goats')
            aadhar_id = request.form.get('aadhar_id')            
            relationship_id = request.form.get('relationship_id')
            relationship = request.form.get('relationship')
            generated_id = request.form.get('generated_id')
            
            # Print the captured data
            print(f"Name: {name}")
            print(f"Age: {age}")
            print(f"Gender: {gender}")
            print(f"Arrival Date: {arrival_date}")
            print(f"Number of Goats: {goats}")
            print(f"Aadhar ID: {aadhar_id}")
            print(f"Generated ID: {generated_id}")
            print(f"Relationship ID: {relationship_id}")
            print(f"Relationship: {relationship}")
            
            # Set image_path to None to prevent the image from being displayed
            image_path = 'static/captured_image.jpg'
          
    else:
        # If the page is loaded initially, set image_path to None
        #image_path = None
       # image_path = 'static/captured_image.jpg'
        
        generated_id = request.form.get('generated_id')
        Encrypted_generated_id(generated_id)
    
    return render_template('index.html', image_path=image_path)

if __name__ == '__main__':
    # Remove the previously captured image if it exists
    #os.remove('static/captured_image.jpg')
    
    # Run the Flask application
    app.run(debug=True)


<!DOCTYPE html>
<html>
<head>
    <title>BAKARWAL Analysis</title>

    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">



    <style>
        .captured-image {
            width: 320px;
            height: 240px;
            position: absolute;
            top: 20px;
            left: 20px;
        }
    </style>
</head>
<body>
    <h1>BAKARWAL Analysis</h1>
    
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        
        <label for="age">Age:</label>
        <input type="number" id="age" name="age" required><br>
        
        <label for="gender">Gender:</label>
        <select id="gender" name="gender" required>
            <option value="">-- Select Gender --</option>
            <option value="male">Male</option>
            <option value="female">Female</option>
        </select><br>
        
        <label for="arrival_date">Arrival Date:</label>
        <input type="date" id="arrival_date" name="arrival_date" required><br>
        
        <label for="goats">Number of Goats:</label>
        <input type="number" id="goats" name="goats" required><br>
        
        <label for="aadhar_id">Aadhar ID:</label>
        <input type="text" id="aadhar_id" name="aadhar_id" required><br>
        
    
        <label for="relationship_id">Relationship ID:</label>
        <input type="text" id="relationship_id" name="relationship_id" required><br>
        
        <label for="relationship">Relationship:</label>
        <input type="text" id="relationship" name="relationship" required><br>
        
        <label for="generated_id">Generated ID:</label>
        <input type="text" id="generated_id" name="generated_id" required><br>
        <button type="submit" name="action" value="generated_id">Generate ID </button>
        
   
    
    {% if image_path %}
        <img src="{{ image_path }}" class="captured-image">
    {% else %}
        <p>No image captured</p>
    {% endif %}


    <button type="submit" name="action" value="capture">Capture Image</button>
    <button type="submit" name="action" value="submit">Submit Form</button>

   
    
</form>


    <script>

document.querySelector('form').addEventListener('submit', function(event) {
            event.preventDefault();
            
            var action = event.submitter.value;
            
            if (action === 'submit') {
                var form = event.target;
                var formData = new FormData(form);
                var formValues = {};
                
                for (var pair of formData.entries()) {
                    formValues[pair[0]] = pair[1];
                }
                
                console.log('Form Data:', formValues);
            }



    </script>
</body>
</html>
