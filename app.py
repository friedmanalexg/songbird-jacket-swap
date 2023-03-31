from flask import Flask, render_template
app = Flask(__name__)

print("Hello World!")


@app.route('/')
def index():
    return 'credibleDEV Test'

if __name__ == '__main__':
    app.run()
