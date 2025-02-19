from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>My life is filled with colors!! yayee!!!!!</h1>"

@app.route("/about")
def about():
    return "<h1>This is an about us page</h1>"

@app.route("/contact")
def contact():
    return "<h1>This is a contact us page</h1>"

@app.route("/product")
def product():
    return "<h1>This is a product page</h1>"

if __name__ == '__main__':
    app.run(debug =True)