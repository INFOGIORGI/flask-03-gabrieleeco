from flask import Flask, render_template

app = Flask(__name__)
prodotti = (("Laptop", "5", "€599"), ("Tablet", "3", "€450"), ("Smartphone", "2", "€800"), ("TV", "8", "€700"))

@app.route("/")
def home():
    return render_template("home.html", titolo="Home")

@app.route("/dettagli")
def detail():
    return render_template("detail.html", titolo="Dettagli", prodotti=prodotti)

@app.route("/scaffale/<numScaffale>")
def scaffale(numScaffale):
    list = []
    for t in prodotti:
        if t[1] == numScaffale:
            list.append(t)
        
    return render_template("dettagliScaffale.html", titolo="Scaffale " + numScaffale, numScaffale=numScaffale, prodotti = list)

app.run()
