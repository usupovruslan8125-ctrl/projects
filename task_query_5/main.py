from data import db_session
from data.jobs import Jobs

db_name = input()
db_session.global_init(db_name)
db_sess = db_session.create_session()
for job in db_sess.query(Jobs).filter(Jobs.work_size < 20, not Jobs.is_finished):
    print(job)