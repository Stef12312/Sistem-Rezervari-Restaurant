
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "proiect_restaurant"

# Initializam 10 mese libere
mese = {i: None for i in range(1, 11)}


# Pagina principala
@app.route("/")
def index():
    return render_template("index.html", mese=mese)


# Rezervarea unei mese
@app.route("/rezerva", methods=["POST"])
def rezerva():
    nume = request.form.get("nume", "").strip()
    nr_masa = request.form.get("masa", type=int)

    if not nume:
        flash("Introdu numele clientului!", "eroare")

    elif nr_masa not in mese:
        flash("Numarul mesei este invalid!", "eroare")

    elif mese[nr_masa] is not None:
        flash("Aceasta masa este deja rezervata!", "eroare")

    else:
        mese[nr_masa] = nume
        flash(
            f"Masa {nr_masa} a fost rezervata de {nume}!",
            "succes"
        )

    return redirect("/")


# Anularea unei rezervari
@app.route("/anuleaza/<int:nr_masa>", methods=["POST"])
def anuleaza(nr_masa):

    if nr_masa not in mese:
        flash("Masa nu exista!", "eroare")

    elif mese[nr_masa] is None:
        flash("Masa este deja libera!", "eroare")

    else:
        mese[nr_masa] = None
        flash(
            f"Rezervarea pentru masa {nr_masa} a fost anulata!",
            "succes"
        )

    return redirect("/")


# Pornirea aplicatiei
if __name__ == "__main__":
    app.run(debug=True)
