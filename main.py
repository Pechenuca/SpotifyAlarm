from models import DataBaseAssistant, Requset
from routers import BasicRoots
from flask import Flask
from flask_restful import Api
from utils import is_first_launch, MusicPlayer, start_thread

db_worker = DataBaseAssistant()
db_worker.create_tables([Requset])

app = Flask(__name__)
api = Api(app)

api.add_resource(BasicRoots, '/')

if is_first_launch() == False:
    #mp = MusicPlayer()
    app.run(debug=True)
else:
    print("Add spotify tokens to .env!")
