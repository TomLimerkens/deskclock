from datetime import datetime
from dateutil import tz
import pytz

from_zone = tz.gettz('UTC')
to_zone = tz.gettz('Europe/Brussels')

utctime = datetime.strptime('2024-03-04 10:44:00', '%Y-%m-%d %H:%M:%S')

#replace timezone for utctime to make sure it is in utc
utctime = utctime.replace(tzinfo=from_zone)

#brussels time
brusselstime = utctime.astimezone(to_zone)

print(f'UTCTime ={utctime} : BRU time = {brusselstime}')

print('-----')

print(f'LocalTime = {datetime.now()}')
print(f'UTC Time ={datetime.utcnow()}')
print(f'UTC via timezone = {datetime.now(tz.UTC)}')
print(f'BRU time via TZ = {datetime.now().astimezone(to_zone)}')
print('-----')
#with cached time
tz_utc = tz.gettz('UTC')
tz_BRU = tz.gettz('Europe/Brussels')
tz_SFO = tz.gettz('America/San Francisco')

#get utc time
tmptime = datetime.now().astimezone(tz_utc)
print(f'timevariable {tmptime}')

print('-----')
tmptime.replace(tzinfo=tz_utc)
print(f'UTC Time = {tmptime}')
print(f'BRU Time = {tmptime.astimezone(tz_BRU)}')
print(f'SFO Time = {tmptime.astimezone(tz_SFO)}')

#conclusion : if you go directly from "datetime.utcnow()" it generates the wrong timezone data.
print('-----')
utctime = datetime.utcnow()
print(f'dateutcnow ={utctime}')
print(f'from utc UTC Time = {utctime}')
print(f'from utc BRU Time = {utctime.astimezone(tz_BRU)}')
print(f'from utc SFO Time = {utctime.astimezone(tz_SFO)}')

#Wrong way of using timestamps > dont use UTCNOW (for now), it does not contain the timezone info, and therefore, is wrong when converting timezones with it.
print('-----')
utctime = datetime.utcnow()
#try to set timezone to make sure TZ data is correct >> Doesnt work either
utctime.replace(tzinfo=pytz.UTC)
print(f'dateutcnow2 ={utctime}')
print(f'from utc2 UTC Time = {utctime}')
print(f'from utc2 BRU Time = {utctime.astimezone(tz_BRU)}')
print(f'from utc2 SFO Time = {utctime.astimezone(tz_SFO)}')
