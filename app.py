from flask import Flask, render_template
from config import SECRET_KEY


app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html', title='Главная страница')

if __name__ == '__main__':
    app.run(debug=True)
