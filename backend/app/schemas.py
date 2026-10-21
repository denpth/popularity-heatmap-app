from pydantic import BaseModel
class Forecast(BaseModel):
    ts:str
    p50:int
    p90:int
