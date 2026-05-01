from data import db_session
from data.users import User
from data.jobs import Jobs


def main():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()

    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"
    db_sess.add(user)

    user2 = User()
    user2.surname = "Weir"
    user2.name = "Andy"
    user2.age = 35
    user2.position = "biologist"
    user2.speciality = "botany"
    user2.address = "module_1"
    user2.email = "andy@mars.org"
    user2.hashed_password = "andy"
    db_sess.add(user2)

    user3 = User()
    user3.surname = "Bean"
    user3.name = "Sean"
    user3.age = 40
    user3.position = "pilot"
    user3.speciality = "navigation"
    user3.address = "module_1"
    user3.email = "sean@mars.org"
    user3.hashed_password = "sean"
    db_sess.add(user3)

    user4 = User()
    user4.surname = "Kapur"
    user4.name = "Venkata"
    user4.age = 28
    user4.position = "engineer"
    user4.speciality = "mechanics"
    user4.address = "module_2"
    user4.email = "venkata@mars.org"
    user4.hashed_password = "venkata"
    db_sess.add(user4)

    db_sess.commit()

    job = Jobs()
    job.team_leader = 1
    job.job = "deployment of residential modules 1 and 2"
    job.work_size = 15
    job.collaborators = "2, 3"
    job.is_finished = False
    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    main()