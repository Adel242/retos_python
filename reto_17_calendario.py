# Importar la librería calendar. Imprimir el calendario del mes actual.

from datetime import datetime
import calendar

month = datetime.now().month
year = datetime.now().year
calend = calendar.TextCalendar(calendar.SUNDAY)
calend.prmonth(year, month)


