from app import db

class WeatherData(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    datetime = db.Column(db.DateTime, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    windspeed = db.Column(db.Float, nullable=False)
    wind_direction = db.Column(db.String(20), nullable=False)
    weather_state = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<WeatherData id={self.id}, datetime={self.datetime}>'