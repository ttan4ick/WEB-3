from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config["SECRET_KEY"] = "yandexlyceum_secret_key"


def main():
    db_session.global_init("db/mars_explorer.db")
    session = db_session.create_session()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Weir"
    user.name = "Andy"
    user.age = 25
    user.position = "scientist"
    user.speciality = "pilot"
    user.address = "module_2"
    user.email = "andy@mars.org"
    user.hashed_password = "andy"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Watny"
    user.name = "Mark"
    user.age = 19
    user.position = "scientist"
    user.speciality = "doctor"
    user.address = "module_3"
    user.email = "mark@mars.org"
    user.hashed_password = "mark"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Kapoor"
    user.name = "Venkat"
    user.age = 26
    user.position = "scientist"
    user.speciality = "builderr"
    user.address = "module_4"
    user.email = "venkat@mars.org"
    user.hashed_password = "venkat"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = "Sanders"
    user.name = "Teddy"
    user.age = 16
    user.position = "scientist"
    user.speciality = "biologist"
    user.address = "module_5"
    user.email = "teddy@mars.org"
    user.hashed_password = "teddy"
    user.set_password(user.hashed_password)
    session.add(user)

    user.set_password(user.hashed_password)
    session.add(user)
    session.commit()


if __name__ == "__main__":
    main()