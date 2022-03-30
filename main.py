import pymongo
from fastapi import FastAPI


uri = "mongodb://saasmongodb:9UlcfXu1mJIVUsucZ4aKkp043hUYG0C8ZXFlBfpPx0nIVrT3sFgEY0uX56cbIJfM6ycvCMjtfqs05FgY5LWSRg==@saasmongodb.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@saasmongodb@"
myclient = pymongo.MongoClient(uri)
mydb = myclient["saas"]
mycol = mydb["filter"]

app = FastAPI()


@app.get("/filter")
def read_root():
    return {'data':[x['domain'] for x in mycol.find({},{ "_id": 0 })]}
