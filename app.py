from flask import Flask


app = Flask(__name__)

@app.route('/api/user/')
def hello():
    return "Hello user"


if __name__ == '__main__':
    app.run(Debug=True)



