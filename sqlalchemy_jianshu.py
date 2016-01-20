from sqlalchemy import create_engine
engine = create_engine("mysql://root:wangfei@localhost:3306/testdb?charset=utf8",encoding="utf-8", echo=True)

print engine
print type(engine)

print engine.execute("SELECT * FROM  Writers")