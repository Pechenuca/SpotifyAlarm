from models import DataBaseAssistant, Requset
from routers import BasicRoots
from flask import Flask
from flask_restful import Api

db_worker = DataBaseAssistant()
db_worker.create_tables([Requset])

app = Flask(__name__)
api = Api(app)

api.add_resource(BasicRoots, '/')
app.run(debug=True)

# from datetime import datetime
# db_wrapper = DataBaseWrapper(Requset)
# db_wrapper.insert(alarm_time=datetime.now(), playlist="123", is_worked=False)