from app import app, db
from app.models import WeatherData
import time

app.app_context().push()


while True:
    currentQuerry = WeatherData.query.all()
    print(currentQuerry)
    time.sleep(5)