from pydantic import BaseModel

class PredictSchema(BaseModel):
    feature1: float
    feature2: float
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "feature1": 3.14,
                    "feature2": 3.14
                }
            ]
        }
    }

class ModelResponseSchema(BaseModel):
    id: str
    response: float
    date: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id":"1",
                    "response": 3.14,
                    "date":  "2023-12-13T01:30:00.000-05:00"
                }
            ]
        }
    }