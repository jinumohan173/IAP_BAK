from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/open_camera')
def open_camera():
    os.system('start microsoft.windows.camera:')
    return 'Camera opened!'

if __name__ == '__main__':
    app.run(debug=True)
