from flask import Flask, render_template, request  # Import necessary modules from Flask

# Import Controller class from pynput.keyboard module
from pynput.keyboard import Key, Controller

# Initialize Flask app
app = Flask(__name__)

# Initialize keyboard controller
keyboard = Controller()

# Define route for the homepage
@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

# Define route for typing text
@app.route('/type-text', methods=['POST'])
def type_text():
    # Get the text from the form
    text = request.form['text']
    
    # Check if the text is a special command
    if text == '{BACKSPACE}':
        # Simulate pressing and releasing the backspace key
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
    elif text == '{ENTER}':
        # Simulate pressing and releasing the enter key
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    else:
        # Type the received text
        keyboard.type(text)
    
    # Return success message
    return 'Text typed successfully'

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
