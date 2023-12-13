from api.schemas.schema import PredictSchema, ModelResponseSchema
from datetime import datetime
from fastapi import APIRouter
from joblib import load
from numpy import array
from uuid import uuid4
import logging as logger

model_router = APIRouter()

@model_router.post("",
            description="This route predict a value using a Linear Regression model from two float values", 
            name="model predict",
            responses={"200": {"model": ModelResponseSchema}},)
async def predict(obj: PredictSchema):    
    try: 
        logger.info("[start] starting model prediction")   
        clf = load("model/modelo.joblib")
        features = array([obj.feature1, obj.feature2]).reshape(1, -1)
        response = clf.predict(features)
        response = round(response[0], 5)
        id=f'{uuid4()}'
        date=datetime.now().isoformat()
        logger.info(f"id={id}, response={response}, date={date}")       
        logger.info("[end] finishing model prediction successfully")       
        return ModelResponseSchema(id=id, response=response, date=date)
    except Exception as error:
        logger.error(f"[error] error in model prediction | error: {error.__cause__}") 
        return{"error": "Server error"}
