from flask import Flask, render_template, request, redirect
from flask import Flask, render_template, request, redirect
from flask import Flask, render_template, Response

from flask import Flask, render_template, Response, send_file

import sqlite3
import subprocess
import cv2
import io

app = Flask(__name__)


camera = cv2.VideoCapture(0)

@app.route('/open_camera')
def open_camera():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

   


def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')





@app.route('/capture_image', methods=['POST'])
def capture_image():
    _, frame = camera.read()
    ret, buffer = cv2.imencode('.jpg', frame)
    image_data = buffer.tobytes()
    return send_file(
        io.BytesIO(image_data),
        mimetype='image/jpeg',
        as_attachment=True,
        attachment_filename='captured_image.jpg'
    )


@app.route('/', methods=['GET', 'POST'])
def fill_details():
    if request.method == 'POST':        
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        # You can add more fields as needed
        # Do something with the data (e.g., save it to a database)
        # Replace the following print statements with your desired functionality
        print("Form 1:")
        print("Name:", name)
        print("Email:", email)
        print("Age:", age)
        data_list = [name,email,age]
        insert_data_to_DB(data_list)
    return render_template('forms.html')


def insert_data_to_DB(data_list):
        # Create a SQLite database and establish a connection
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        # Insert data into the table
        insert_data_query = '''
                                INSERT INTO users (name, email,age) VALUES (?,?, ?)
                            '''
        user_data = [(data_list[0], data_list[1],data_list[2])]
        cursor.executemany(insert_data_query, user_data)
        # Add your code here to process the data as needed
        # Commit the changes to the database
        conn.commit()
        Read_data_from_DB()

def Read_data_from_DB():
    # Create a SQLite database and establish a connection
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # Insert data into the table
     # Read data from the table
    select_data_query = '''
    SELECT * FROM users
    '''
    cursor.execute(select_data_query)

    # Fetch all the rows as a list of tuples
    rows = cursor.fetchall()

    # Print the data
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, email: {row[2]},Age:{row[3]}")

    # Close the cursor and the database connection
    cursor.close()
    conn.close()
     



if __name__ == '__main__':
   
    app.run(debug=True)
    
