db_name = input()
global_init(db_name)
db_sess = create_session()
db_sess.query(User).filter(User.address == "module_1", User.age < 21).update(
    {"address": "module_3"}
)
db_sess.commit()
for user in db_sess.query(User).filter(User.address == "module_3"):
    print(user)