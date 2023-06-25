from flask import Flask, render_template, request
import cv2
import os
import base64


from flask import Flask, render_template, request, redirect
from flask import Flask, render_template, request, redirect
from flask import Flask, render_template, Response

from flask import Flask, render_template, Response, send_file

import sqlite3
import subprocess
import cv2
import io
from fpdf import FPDF

# Create FPDF object
pdf = FPDF()
app = Flask(__name__)

#image_path = None

image_path_directory = 'static/captured_image.jpg'

def  Generate_pdf_file(image_path,user_data):
    i=0
    # Add a page
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt="INDIAN ARMY", ln=1, align='C')
    pdf.image(image_path, x=100, y=30, w=50, h=50) 
    table_list = ["name : ","age : ","gender : ","arrival_date : ","goats : ","aadhar_id : ","relationship_id : ","relationship : "]
    
    print("length of userdata ",len(user_data))
    
    for data in user_data:
        pdf.cell(200, 10, txt=table_list[i]+str(data), ln=i+2, align='L')
        i=i+1
        print("i--> ",i,data)
    
    pdf.output("out.pdf")
    print("**************************************************")
    



@app.route('/save_image', methods=['POST'])
def save_image():
    image = request.files['image']
    if image:
        image.save('static/captured_image.jpg')
        return 'Image saved successfully'
    else:
        return 'No image received'

def insert_data_to_DB(data_list):
        # Create a SQLite database and establish a connection
        conn = sqlite3.connect('bakarwal_database.db')
        cursor = conn.cursor()
        # Insert data into the table
        # Insert data into the table
        insert_data_query = '''
        INSERT INTO information (name,age,gender,arrival_date,goats,aadhar_id,relationship_id,relationship) VALUES (?,?,?,?,?,?,?,?)
         '''
                          
        user_data = [(data_list[0], data_list[1],data_list[2],data_list[3],data_list[4],data_list[5],data_list[6],data_list[7])]
        
        print("user data ",user_data)
        print("image path ",image_path_directory)
        for data in user_data:
            print("data--> " ,data)
        
        
        cursor.executemany(insert_data_query, user_data)
        # Add your code here to process the data as needed
        # Commit the changes to the database
        conn.commit()
        Generate_pdf_file(image_path_directory,data_list)
      #  Read_data_from_DB()
      

def Read_data_from_DB():
    # Create a SQLite database and establish a connection
    conn = sqlite3.connect('bakarwal_database.db')
    cursor = conn.cursor()
    # Insert data into the table
     # Read data from the table
     # Read data from the table
    select_data_query = '''
     SELECT * FROM information
     '''
    cursor.execute(select_data_query)

    # Fetch all the rows as a list of tuples
    rows = cursor.fetchall()

    # Print the data
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, age: {row[2]},gender:{row[3]},arrival_date: {row[4]}, goats: {row[5]}, aadhar_id: {row[6]},relationship_id:{row[7]},relationship:{row[8]}")

   

    # Close the cursor and the database connection
    cursor.close()
    conn.close()








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
   # global image_path  # Declare image_path as a global variable
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'capture':
            # If the "Capture Image" button is clicked, capture an image
            image_path = capture_image()
            
            # Render the template with the captured image
            return render_template('index.html', image_path=image_path)
        
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
            data_list = [name,age,gender,arrival_date,goats,aadhar_id,relationship_id,relationship]
            
            # Print the captured data
            print(f"Name: {name}")
            print(f"Age: {age}")
            print(f"Gender: {gender}")
            print(f"Arrival Date: {arrival_date}")
            print(f"Number of Goats: {goats}")
            print(f"Aadhar ID: {aadhar_id}")
            print(f"Relationship ID: {relationship_id}")
            print(f"Relationship: {relationship}")
            
            # Perform any additional processing or storage of the form data
            
            # Set image_path to None to prevent the image from being displayed
            
           # print("image path ",image_path)
            
            insert_data_to_DB(data_list)
            image_path = None
    
    else:
        # If the page is loaded initially, set image_path to None
        image_path = None
    
    return render_template('index.html', image_path=image_path)


if __name__ == '__main__':
    # Remove the previously captured image if it exists
    if os.path.exists('static/captured_image.jpg'):
        os.remove('static/captured_image.jpg')
    
    # Run the Flask application
    app.run(debug=True)