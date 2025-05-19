from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello from Flask! <a href='/about'>Click me!</a></h1>"


@app.route('/about')
def about():
    return "А че если по русски"


if __name__ == "__main__":
    app.run(debug=True)
