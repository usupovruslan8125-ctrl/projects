from data import db_session
from data.jobs import Jobs

db_name = input()
db_session.global_init(db_name)
db_sess = db_session.create_session()
jobs = db_sess.query(Jobs).all()
max_collaborators = 0
for job in jobs:
    if job.collaborators:
        count = len(job.collaborators.split(","))
        if count > max_collaborators:
            max_collaborators = count
for job in jobs:
    if job.collaborators and len(job.collaborators.split(",")) == max_collaborators:
        print(f"{job.user.surname} {job.user.name}")