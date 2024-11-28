from flask import Flask, render_template_string
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Инструменты</title>
        <style>
            body { font-family: Arial, sans-serif; }
            .tool { margin-bottom: 20px; }
            .hidden { display: none; }
        </style>
    </head>
    <body>
        <h1>Добро пожаловать на мой сайт инструментов!</h1>
        
        <div class="tool" id="coinFlip">
            <h2>Бросок монетки</h2>
            <button onclick="flipCoin()">Бросить монетку</button>
            <p id="coinResult"></p>
        </div>
        
        <div class="tool" id="passwordGenerator">
            <h2>Генератор паролей</h2>
            <button onclick="generatePassword()">Сгенерировать пароль</button>
            <p id="passwordResult"></p>
        </div>
        
        <div class="tool" id="randomImage">
            <h2>Случайная картинка</h2>
            <button onclick="showRandomImage()">Показать случайную картинку</button>
            <div id="imageContainer"></div>
        </div>

        <script>
            function flipCoin() {
                fetch('/flip_coin')
                    .then(response => response.text())
                    .then(result => {
                        document.getElementById('coinResult').textContent = result;
                    });
            }
            
            function generatePassword() {
                fetch('/generate_password')
                    .then(response => response.text())
                    .then(password => {
                        document.getElementById('passwordResult').textContent = password;
                    });
            }
            
            function showRandomImage() {
                fetch('/random_image')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('imageContainer').innerHTML = '<img src="' + data.image + '" alt="Random Image">';
                    });
            }
        </script>
    </body>
    </html>
    ''')

@app.route('/flip_coin')
def flip_coin():
    result = 'Орел' if random.random() < 0.5 else 'Решка'
    return result

@app.route('/generate_password')
def generate_password():
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    password = ''.join(random.choice(chars) for _ in range(10))
    return password

@app.route('/random_image')
def random_image():
    images = [
        'image1.jpg',
        'image2.jpg',
        'image3.jpg'
    ]
    random_image = random.choice(images)
    return {'image': random_image}

if __name__ == '__main__':
    app.run(debug=True)
