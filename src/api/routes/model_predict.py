from joblib import load
from api.schemas.schema import PredictSchema, ModelResponseSchema
from numpy import array
from fastapi import APIRouter


model_router = APIRouter()

@model_router.post("",
            description="This route predict a value using a Linear Regression model from two float values", 
            name="model predict",
            responses={"200": {"model": ModelResponseSchema}},)
async def predict(obj: PredictSchema):
    #clf = load("../model/modelo.joblib")
    clf = load("/home/angelo/Desktop/case-pb/model/modelo.joblib")
    features = array([obj.feature1, obj.feature2]).reshape(1, -1)
    response = clf.predict(features)
    return ModelResponseSchema(response=response)