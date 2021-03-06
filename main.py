from models import DataBaseAssistant, DataBaseWrapper, Requset
from routers import BasicRoots, MusicController
from flask import Flask
from flask_restful import Api
from utils import *

db_worker = DataBaseAssistant()
db_worker.create_tables([Requset])

app = Flask(__name__)
api = Api(app)

if is_first_launch() == False:
    
    mp = MusicPlayer()
    db_wrapper = DataBaseWrapper(Requset)
    api.add_resource(BasicRoots, '/')
    api.add_resource(MusicController, '/alarm')
    start_thread(inspect_request, False, db_wrapper, mp,)
    app.run(debug=True)
else:
    print("Add spotify tokens to .env!")
