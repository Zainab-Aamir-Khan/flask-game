from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>My life is filled with colors!! yayee!!!!!</h1>"

if __name__ == '__main__':
    app.run(debug =True)