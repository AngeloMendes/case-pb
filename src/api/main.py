from typing import Union
from joblib import load
from schemas.schema import PredictSchema, ModelResponseSchema
from fastapi import FastAPI
from numpy import array
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/predict",             
            description="This route predict a value using a Linear Regression model from two float values", 
            name="model predict",
            responses={"200": {"model": ModelResponseSchema}},)
async def predict(obj: PredictSchema):
    #clf = load("../model/modelo.joblib")
    clf = load("/home/angelo/Desktop/case-pb/model/modelo.joblib")
    p=array([obj.feature1, obj.feature2]).reshape(1, -1)
    r = clf.predict(p)
    return ModelResponseSchema(response=r)