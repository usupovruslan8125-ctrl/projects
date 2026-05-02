db_name = input()
global_init(db_name)
db_sess = create_session()
for job in db_sess.query(Jobs).filter(Jobs.work_size < 20, Jobs.is_finished == False):
    print(job)