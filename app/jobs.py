from app import app, db
from app.models import WeatherData
from datetime import datetime
import random
import celery

windDirections = ['E','SE','S','SW','W','NW','N','NE']
weatherStates = ['Clear', 'Cloudy', 'Fog', 'Rain', 'Snow', 'Storm', 'Thunder', 'Smog']

@celery.task
def DbPush():
    currentDateTime = datetime.utcnow()
    currentTemperature = random.randint(-20, 30)
    currentHumidity = random.randint(0,100)
    currentWindspeed = random.randint(0,12)
    currentWindDirection = windDirections[random.randint(0,7)]
    currentWeatherState = weatherStates[random.randint(0,7)]
    dataPacket = WeatherData(datetime = currentDateTime,
                             temperature = currentTemperature,
                             humidity = currentHumidity,
                             windspeed = currentWindspeed,
                             wind_direction = currentWindDirection,
                             weather_state = currentWeatherState)
    with app.app_context():
        db.session.add(dataPacket)
        output = db.session.commit()
    return output
