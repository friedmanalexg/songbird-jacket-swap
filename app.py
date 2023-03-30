from flask import Flask
app = Flask(__name__)

print("Hello World!")


@app.route('/')
def index():
    return 'hello world!'


@app.route('/about')
def about():
    return 'this is a flask app i am writing for fun and profit'


if __name__ == '__main__':
    app.run()
