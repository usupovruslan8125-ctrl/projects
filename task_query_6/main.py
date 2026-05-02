from db_session import global_init, create_session
from jobs import Jobs
from users import User

db_name = input()
global_init(db_name)
db_sess = create_session()
jobs = db_sess.query(Jobs).all()
max_collaborators = 0
for job in jobs:
    if job.collaborators:
        count = len(job.collaborators.split(","))
        if count > max_collaborators:
            max_collaborators = count
for job in jobs:
    if job.collaborators and len(job.collaborators.split(",")) == max_collaborators:
        team_leader = db_sess.query(User).filter(User.id == job.team_leader).first()
        print(f"{team_leader.surname} {team_leader.name}")