from app import app
from app.models import WeatherData
import time
import logging
import colorlog
import os
import msvcrt
app.app_context().push()

class ClearingStreamHandler(logging.StreamHandler):
    def emit(self, record):
        os.system('cls')
        super().emit(record)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(message)s',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)


console_handler = ClearingStreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


while True:
    if msvcrt.kbhit():
        key = msvcrt.getch().decode()
        if key == '\r':
            break
    currentQuerry = WeatherData.query.all()
    logger.warning(f'Total of db entries: {len(currentQuerry)} \nLatest added element to db: {currentQuerry[-1:]}')
    print('\nPress ENTER to exit')
    time.sleep(3)