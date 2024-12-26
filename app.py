from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/FAQ")
def faq():
    return render_template("FAQ.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/products")
def products():
    return render_template("products.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
