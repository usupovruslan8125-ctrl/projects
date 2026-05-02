import datetime
from data import db_session
from data.jobs import Jobs


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    sess = db_session.create_session()

    job = Jobs()
    job.team_leader = 1
    job.job = "deployment of residential modules 1 and 2"
    job.work_size = 15
    job.collaborators = "2, 3"
    job.start_date = datetime.datetime.now()
    job.is_finished = False
    sess.add(job)
    sess.commit()
    print("Done")


if __name__ == "__main__":
    main()