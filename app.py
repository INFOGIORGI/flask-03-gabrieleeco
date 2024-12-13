from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", titolo="Home")

@app.route("/dettagli")
def detail():
    prodotti = (("Laptop", "5", "€599"), ("Tablet", "3", "€450"), ("Smartphone", "2", "€800"), ("TV", "8", "€700"))
    return render_template("detail.html", titolo="Dettagli", prodotti=prodotti)

@app.route("/scaffale")
def scaffale():
    return render_template("dettagliScaffale.html", titolo="Scaffale")

app.run()
