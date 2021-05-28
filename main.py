from models import DataBaseAssistant, DataBaseWrapper, Requset
from routers import BasicRoots
from flask import Flask
from flask_restful import Api
from utils import is_first_launch, MusicPlayer, inspect_request, download_music

db_worker = DataBaseAssistant()
db_worker.create_tables([Requset])

app = Flask(__name__)
api = Api(app)

api.add_resource(BasicRoots, '/')

if is_first_launch() == False:
    # mp = MusicPlayer()
    # db_wrapper = DataBaseWrapper(Requset)
    # inspect_request(db_wrapper, mp)
    app.run(debug=True)
else:
    print("Add spotify tokens to .env!")
