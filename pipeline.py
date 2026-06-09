import requests 
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
def extract():
    print("Extracting data...")
    url= "https://jsonplaceholder.typicode.com/users"
    response=requests.get(url)
    data=response.json()
    return pd.DataFrame(data)
def transform(df):
    print ("Transforming data...")
    df=df[['id','name','email','phone']]
    df=df.rename(columns={'id':'user_id'})
    df['email']=df['email'].str.lower()
    df['loaded_at']=datetime.utcnow().isoformat()
    return df
def load(df):
    print("Loading data...")
    engine=create_engine("sqlite:///pipeline.db")
    df.to_sql("users",engine, if_exists="replace",index=False)
    print(f"Loaded {len(df)}rows!")
def run():
    raw=extract()
    clean=transform(raw)
    load(clean)
    print("Pipeline complete!")
run()
