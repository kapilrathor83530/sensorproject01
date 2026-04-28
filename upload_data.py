from pymongo.mongo_client import MongoClient
import pandas as pd 
import json
# url information 
url = "mongodb+srv://Kapil:147369@cluster0.i0jvwri.mongodb.net/?appName=Cluster0"
# create a new client and connect to server 
client = MongoClient(url)
# create a database name and collection name 
DATABASE_NAME = "kapilskills"
COLLECTION_NAME = "waferfault"
df = pd.read_csv("E:\projects\sensorproject\src\notebooks\wafer_23012020_041211.csv")
df.head()
df = df.drop("Unnamed: 0" ,axis = 1)
json_record = list(json.loads(df.T.to_json()).values())
type(json_record)
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)