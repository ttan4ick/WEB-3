from data.jobs import Jobs
from flask import Flask, render_template, request
from data import db_session
from data.users import User

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


@app.route("/")
def index():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    users = session.query(User).all()
    names = {name.id: (name.surname, name.name) for name in users}
    return render_template("index.html", jobs=jobs, names=names)


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template(
            "register.html", title="Регистрация", password_error=False
        )
    elif request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        retry_password = request.form["retry_password"]
        surname = request.form["surname"]
        name = request.form["name"]
        age = request.form["age"]
        position = request.form["position"]
        speciality = request.form["speciality"]
        address = request.form["address"]
        if password == retry_password:
            session = db_session.create_session()
            user = User()
            user.email = email
            user.set_password(password)
            user.surname = surname
            user.name = name
            user.age = int(age)
            user.position = position
            user.speciality = speciality
            user.address = address
            session.add(user)
            session.commit()
            return "Форма отправлена"
        return render_template(
            "register.html", title="Регистрация", password_error=True
        )


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run(port=8080, host="127.0.0.1")


if __name__ == "__main__":
    main()