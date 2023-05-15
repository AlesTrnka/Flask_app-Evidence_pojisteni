from flask import Flask, render_template, url_for, redirect, flash
from formulare import RegistracniFormular, VyhledavaciFormular, EditujFormular
from evidence import Evidence, evidence
import os
import sqlite3

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a1c586mmd85'
app.config["DATABASE"] = os.path.abspath(os.path.dirname(__file__)) + "\\databaze.db"
evidence.vytvor_tabulku()


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title='Evidence pojištění')

@app.route('/add', methods = ["GET", "POST"])
def registruj():
    form = RegistracniFormular()
    if form.validate_on_submit():
        jmeno = form.jmeno.data
        prijmeni = form.prijmeni.data
        vek = form.vek.data
        email = form.email.data
        telefon = form.telefon.data
        ulice = form.ulice.data
        mesto = form.mesto.data
        psc = form.psc.data
        evidence.pridej(jmeno, prijmeni, vek, email, telefon, ulice, mesto, psc)
        flash(f"Pojištěný {form.jmeno.data} {form.prijmeni.data} byl zaevidován do databáze", 'success')
        return redirect(url_for('index'))
    return render_template('registrace.html', form=form, title='Registrace')

@app.route('/find', methods = ["GET", "POST"])
def vyhledej():
    form = VyhledavaciFormular()
    if form.validate_on_submit():
        jmeno = form.jmeno.data
        prijmeni = form.prijmeni.data
        if evidence.vyhledej(jmeno, prijmeni) == []:
            flash(f'Zadané jméno nebylo nalezeno v databázi','danger')
            return render_template('vyhledani.html', form=form, title='Vyhledání pojištěného')
        else:
            vysledek = evidence.vyhledej(jmeno, prijmeni)
            flash(f'Zadané jméno bylo nalezeno v databázi', 'success')
            return render_template('vyhledani.html', form=form, title='Vyhledání pojištěného', vysledek=vysledek)
    return render_template('vyhledani.html', form=form, title='Vyhledání pojištěného')

@app.route('/edit', methods = ["GET", "POST"])
def edituj():
    form = EditujFormular()
    if form.validate_on_submit():
        jmeno = form.jmeno.data
        prijmeni = form.prijmeni.data
        udaj = form.udaj.data
        hodnota= form.hodnota.data
        if evidence.vyhledej(jmeno, prijmeni) == []:
            flash('Zadané jméno nebylo nalezeno v databázi', 'danger')
            return render_template('editace.html', form=form, title='Editace pojištěného')
        else:
            evidence.edituj(jmeno, prijmeni, udaj, hodnota)
            vysledek = evidence.vyhledej(jmeno, prijmeni)
            flash(f"Údaj pojištěného byl aktualizován", 'success')
            return render_template('editace.html', form=form, title='Editace pojištěného',vysledek=vysledek)
    return render_template('editace.html', form=form, title='Editace pojištěného')

@app.route('/o_aplikaci')
def o_aplikaci():
    return render_template('o_aplikaci.html', title=f'O aplikaci')

@app.route('/autor')
def autor():
    return render_template('autor.html', title=f'Autor aplikace')


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
