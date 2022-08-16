import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("app2022-a58d3-firebase-adminsdk-cstfx-ecff887237.json")
firebase_admin.initialize_app(cred)

dir = db.reference()
dir.update({'자동차':['기아','현대','벤츠']}) 