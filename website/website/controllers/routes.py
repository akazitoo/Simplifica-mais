from flask import render_template, request, redirect, url_for,  flash
from website import app, db

from website.models.tables import Traffic
from website.models.forms import MainForm, AuthForm
from website.controllers.utils import insert_data


@app.route("/", methods=["GET"])
def index():

    if 'section' in request.args and 'url_route' in request.args:
        section = request.args.get("section")
        url_route = request.args.get("url_route")

        insert_data = Traffic(section, url_route)
        db.session.add(insert_data)
        db.session.commit()

    return render_template("index.html")


@app.route("/formulario/", methods=["GET", "POST"])
def form_page():

    form = MainForm()

    if form.validate_on_submit():

        city = form.county.data
        gender = form.gender.data
        initials = form.lgbtqia_plus.data

        city = city.replace("ã", "a")
        gender = gender.replace("ê", "e")
        
        return redirect(url_for("result", municipio=city, genero=gender, sigla=initials))

    return render_template("formulario.html", form=form)


@app.route("/formulario/resultado/", methods=["GET","POST"])
def result():

    city = request.args.get("municipio")
    gender = request.args.get("genero")
    initials = request.args.get("sigla")

    city = city.replace("ã", "a").replace(" ", "")
    gender = gender.replace("ê", "e").replace(" ", "")

    male_words = ["homemtransgenero", "homem", "masculino"]
    female_words = ["mulhertransgenero", "mulher", "feminino"]

    is_female = gender.lower() in female_words
    is_male = gender.lower() in male_words
    is_trans = initials.lower() == "t"

    print(city.lower())

    if city.lower() == "recife":

        if is_male and is_trans:
            insert_data(city, gender, initials)
            return render_template("Hospital_da_Mulher.html")

        if is_female and is_trans:
            insert_data(city, gender, initials)
            return render_template("Patricia_Gomes.html")

        if is_female:
            insert_data(city, gender, initials)
            return render_template("Hospital_da_Mulher.html")


        return render_template("Patricia_Gomes.html")

    if city.lower() == "camaragibe":
        insert_data(city, gender, initials)
        return render_template("Darlen_Gasparelle.html")

    if city.lower() == "jaboatao":
        insert_data(city, gender, initials)
        return render_template("Jaboatao.html")

    
    flash("Infelizmente não possui um ambulatório no seu municipio.")
    return redirect(url_for("form_page"))
        

@app.route("/autenticacao/", methods=["GET","POST"])
def authentication():

    form = AuthForm()

    if form.validate_on_submit():
        cpf = form.cpf.data
        return redirect(url_for("forwarding", cpf=cpf))

    return render_template("autenticacao.html", form=form)


@app.route("/verificado/encaminhamento/", methods=["GET","POST"])
def forwarding():
    return render_template("encaminhamento.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
