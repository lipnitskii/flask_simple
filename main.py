from flask import Flask, render_template
import conf

app = Flask(__name__)

SECRET_KEY = conf.SECRET_KEY

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=conf.DEBUG)
    