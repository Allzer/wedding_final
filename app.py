from flask import Flask, render_template, request
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route("/index")
@app.route('/')
def index():
    user_agent = request.user_agent.string
    if 'Mobile' in user_agent or 'Android' in user_agent or 'iPhone' in user_agent:
        return render_template('index.html')
    else:
        return render_template('index_desktop.html')

if __name__ == '__main__':
    app.run(debug=False)

