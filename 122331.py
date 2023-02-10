import datetime
from datetime import datetime, timedelta
import time

current_date = datetime.today()
current_date_string = current_date.strftime('%m/%d/%Y')
future_date_1 = datetime.today() + timedelta(days=10)
future_date_2 = future_date_1.strftime('%m/%d/%Y')
print(future_date_1)
print(future_date_2)
print(current_date_string)  # проверяем формат получения текущей даты