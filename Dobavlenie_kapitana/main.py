from data import db_session
from data.users import User


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    sess = db_session.create_session()

    # Капитан Ridley Scott
    captain = User()
    captain.surname = "Scott"
    captain.name = "Ridley"
    captain.age = 21
    captain.position = "captain"
    captain.speciality = "research engineer"
    captain.address = "module_1"
    captain.email = "scott_chief@mars.org"
    sess.add(captain)

    # Колонист 1
    c1 = User()
    c1.surname = "Weir"
    c1.name = "Andy"
    c1.age = 30
    c1.position = "engineer"
    c1.speciality = "biologist"
    c1.address = "module_2"
    c1.email = "weir_andy@mars.org"
    sess.add(c1)

    # Колонист 2
    c2 = User()
    c2.surname = "Bean"
    c2.name = "Sean"
    c2.age = 25
    c2.position = "pilot"
    c2.speciality = "navigation"
    c2.address = "module_1"
    c2.email = "bean_sean@mars.org"
    sess.add(c2)

    # Колонист 3
    c3 = User()
    c3.surname = "Lee"
    c3.name = "Sara"
    c3.age = 28
    c3.position = "doctor"
    c3.speciality = "surgery"
    c3.address = "module_3"
    c3.email = "lee_sara@mars.org"
    sess.add(c3)

    sess.commit()
    print("Done")


if __name__ == "__main__":
    main()