from enum import Enum
from pydantic import BaseModel

from app.tools.weather_tool import City, WeatherData, WeatherCondition

class HeatRiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TravelRequest(BaseModel):
    destination: City
    departure_date: str
    return_date: str | None = None
    passengers: int = 1

    child_age: int | None = None
    child_heat_sensitive: bool | None = None

class WeatherAssessment(BaseModel):
    destination: City
    average_temperature: float
    weather_condition: WeatherCondition
    heat_risk_level: HeatRiskLevel

class TravelPlan(BaseModel):
    final_destination: City
    was_modified: bool
    explanation: str

class HeatAssessment(BaseModel): # הערכת סיכוני חום
    heat_risk_level: HeatRiskLevel

def assess_heat(temperature: float) -> HeatAssessment:
    if temperature >= 35:
        return HeatAssessment(heat_risk_level=HeatRiskLevel.HIGH)
    elif 25 <= temperature < 35:
        return HeatAssessment(heat_risk_level=HeatRiskLevel.MEDIUM)
    else:
        return HeatAssessment(heat_risk_level=HeatRiskLevel.LOW)
    
def assess_weather(weatherdata: WeatherData) -> WeatherAssessment:
    heat = assess_heat(weatherdata.temperature)

    return WeatherAssessment(
        destination=weatherdata.destination,
        average_temperature=weatherdata.temperature,
        weather_condition=weatherdata.weather_condition,
        heat_risk_level=heat.heat_risk_level)
    