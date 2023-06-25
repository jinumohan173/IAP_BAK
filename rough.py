from flask import Flask, render_template, request, redirect
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy








app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # SQLite database file
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User(name='{self.name}', email='{self.email}', age={self.age})"



@app.route('/', methods=['GET', 'POST'])
def fill_details():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']

        # Create a new User object
        new_user = User(name=name, email=email, age=age)

        # Add the user to the session and commit to save in the database
        db.session.add(new_user)
        db.session.commit()

       # return redirect('/form2')

    return render_template('forms.html')



@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()



"""

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
        # Add your code here to process the data as needed

        # Redirect to the second form
       # return redirect('/forms2')

    return render_template('forms.html')


@app.route('/forms2', methods=['GET', 'POST'])
def additional_form():
    if request.method == 'POST':
        address = request.form['address']
        phone = request.form['phone']
        # You can add more fields as needed

        # Do something with the data (e.g., save it to a database)
        # Replace the following print statements with your desired functionality
        print("Form 2:")
        print("Address:", address)
        print("Phone:", phone)
        # Add your code here to process the data as needed

        return "Details submitted successfully!"

    return render_template('forms2.html')

    
"""

if __name__ == '__main__':
   
    app.run(debug=True)
