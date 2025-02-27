from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, include_uppercase, include_digits, include_special_chars):
    char_set = string.ascii_lowercase
    if include_uppercase:
        char_set += string.ascii_uppercase
    if include_digits:
        char_set += string.digits
    if include_special_chars:
        char_set += string.punctuation
    
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        length = int(request.form['length'])
        include_uppercase = 'uppercase' in request.form
        include_digits = 'digits' in request.form
        include_special_chars = 'special' in request.form
        password = generate_password(length, include_uppercase, include_digits, include_special_chars)
    
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
