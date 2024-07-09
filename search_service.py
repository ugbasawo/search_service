from flask import Flask

app = Flask(__name__)

@app.route('/search')
def search():
    return "You can make your search here"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
