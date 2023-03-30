from flask import Flask
app = Flask(__name__)

print("Hello World!")


@app.route('/')
def index():
    return 'hello world!'


if __name__ == '__main__':
    app.run()
