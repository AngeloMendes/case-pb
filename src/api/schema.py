from pydantic import BaseModel

class PredictSchema(BaseModel):
    feature1: float
    feature2: float
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "feature1": "3.14",
                    "feature2": "3.14"                    
                }
            ]
        }
    }

class ModelResponseSchema(BaseModel):
    response: list

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "response": [3.14]
                }
            ]
        }
    }