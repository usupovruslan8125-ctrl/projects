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
result = []
for job in jobs:
    if job.collaborators and len(job.collaborators.split(",")) == max_collaborators:
        team_leader = db_sess.query(User).filter(User.id == job.team_leader).first()
        result.append(f"{team_leader.surname} {team_leader.name}")
result.sort()
for name in result:
    print(name)
