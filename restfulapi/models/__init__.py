from flask_sqlalchemy import SQLAlchemy

#connection_string = "mysql+mysqlconnector://sat2appmob:sat2app@localhost:3306/sat2appmob"
#print("===> Ready to get database connection ...", connection_string)
#engine = db.create_engine(connection_string, echo=True)
#print(engine, "[ OK ]")
db = SQLAlchemy()
