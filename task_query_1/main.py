db_name = input()
global_init(db_name)
db_sess = create_session()
for user in db_sess.query(User).filter(User.address == "module_1"):
    print(user)