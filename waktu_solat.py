# from skyfield.api import load

# # Create a timescale and ask the current time.
# ts = load.timescale()
# t = ts.now()

# # Load the JPL ephemeris DE421 (covers 1900-2050).
# planets = load('de421.bsp')
# earth, mars = planets['earth'], planets['mars']

# # What's the position of Mars, viewed from Earth?
# astrometric = earth.at(t).observe(mars)
# ra, dec, distance = astrometric.radec()

# print(ra)
# print(dec)
# print(distance)
import datetime as dt
import math

#Merubah angka desimal menjadi format HMS (08:30:20)
def decimal_to_hms(decimal_hours):
    hours = int(decimal_hours)
    total_seconds = round(decimal_hours * 3600)
    minutes = (total_seconds // 60) % 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
#Merubah angka desimal menjadi format HM (08:30)
def decimal_to_hm(decimal_hours):
    hours = int(decimal_hours)
    total_seconds = round(decimal_hours * 3600)
    minutes = (total_seconds // 60) % 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}"
#Merubah angka desimal menjadi format DMS (110°20'30.20")
def decimal_to_dms(decimal_degrees):
    degrees = int(decimal_degrees)
    minutes = int((decimal_degrees - degrees) * 60)
    seconds = ((decimal_degrees - degrees) * 60 - minutes) * 60
    return f"{degrees}°{abs(minutes)}'{abs(seconds):.2f}\""
#Membulatkan nilai menit ke atas
def pembulatan_menit(nilai):
    jam = int(nilai)
    menit = math.ceil((nilai - jam) * 60)
    return jam + menit/60;
#Mengambil nilai desimal dari waktu dalam objek datetime
def time_to_decimal(dt: dt.datetime):
  time = dt.time()
  split = str(time).split(':')
  return int(split[0]) + int(split[1])/60 + float(split[2])/3600
#Mengambil tanggal bulan dan tahun dalam string berformat tgl-bln-thn
def get_tgl(tgl):
    split = tgl.split('-');
    return int(split[0]),int(split[1]),int(split[2])
#Mengambil tanggal bulan dan tahun dalam string berformat bln-thn
def get_bln_thn(tgl):
    split = tgl.split('-');
    return int(split[0]),int(split[1])
#Merubah format DMS menjadi angka dalam bentuk desimal
def dms_to_decimal(dms_str):
    dms_str = dms_str.replace("''", "\"")
    dms_str = dms_str.strip()
    deg_index = dms_str.find("°")
    min_index = dms_str.find("'")
    sec_index = dms_str.find("\"")

    if deg_index == -1 or min_index == -1 or sec_index == -1:
        return float(dms_str)
    degrees = abs(float(dms_str[:deg_index]))
    minutes = float(dms_str[deg_index+1:min_index])
    seconds = float(dms_str[min_index+1:sec_index])
    hasil = degrees + (minutes / 60) + (seconds / 3600)
    if dms_str[0] == '-':
        hasil *= -1
    return hasil 
# batasssss####
### Waktu Transit Matahari ### 
from skyfield import almanac
from skyfield.api import load, wgs84
import datetime as dt
latitude = -7 #>>>lintang kota semarang
longitude = 110.4 #>>>bujur kota semarang
timezone = dt.timezone(dt.timedelta(hours=7)) #>>>> selisih waktu dari grenwict
eph = load('de421.bsp')
ts = load.timescale() #>>> ini yang akan menghasilkan waktu nantik
t = ts.utc(2025,4,3) #>>>tanggal waktu nya 
earth, sun = eph['earth'], eph['sun']
location = earth + wgs84.latlon(latitude, longitude)
transit = almanac.find_transits(location, sun, t,t+1)
MP = transit.astimezone(timezone)[0] #untuk menyesuaikan zona waktu kita 
print(MP)

#Menghitung Deklinasi matahari 
t = ts.from_datetime(MP)
astrometric = earth.at(t).observe(sun).apparent()
ra, dec, distance = astrometric.radec()
print(ra,dec)

#menghitung sudut waktu matahari 
from math import sin, cos, tan, acos, atan, degrees, radians
 
hasar = degrees(atan(1/(tan(radians(abs(dec.degrees-latitude)))+1)))
hmangrib = -1
hisya = -18
hsubuh = -20
hduha = 4.5
toasar = degrees(acos(sin(radians(hasar))/cos(radians(latitude))/cos(dec.radians)-tan(radians(latitude))*tan(dec.radians)))#rumus sudut waktu python version
tomaghrib = degrees(acos(sin(radians(hmangrib))/cos(radians(latitude))/cos(dec.radians)-tan(radians(latitude))*tan(dec.radians)))#rumus sudut waktu python version
toisya = degrees(acos(sin(radians(hisya))/cos(radians(latitude))/cos(dec.radians)-tan(radians(latitude))*tan(dec.radians)))#rumus sudut waktu python version
tosubuh = degrees(acos(sin(radians(hsubuh))/cos(radians(latitude))/cos(dec.radians)-tan(radians(latitude))*tan(dec.radians)))#rumus sudut waktu python version
toduha = degrees(acos(sin(radians(hduha))/cos(radians(latitude))/cos(dec.radians)-tan(radians(latitude))*tan(dec.radians)))#rumus sudut waktu python version
mp = time_to_decimal(MP)

### MENGHITUNG AWAL WAKTU SOLAT ###
ihtiyat = 2/60
dzuhur = pembulatan_menit(mp + ihtiyat)
asar = pembulatan_menit(mp + toasar/15 + ihtiyat)
maghrib = pembulatan_menit(mp + tomaghrib/15 + ihtiyat)
isya = pembulatan_menit(mp + toisya/15 + ihtiyat)
subuh = pembulatan_menit(mp - tosubuh/15 + ihtiyat)
imsak = pembulatan_menit(subuh -10/60)
terbit = mp - tomaghrib/15 - ihtiyat
duha = pembulatan_menit(mp - toduha/15 + ihtiyat)

print("Jadwal Waktu Salat",MP.strftime("%A, %d %B %Y"))
print("Imsak =",decimal_to_hm(imsak))
print("Subuh =",decimal_to_hm(subuh))
print("Terbit =",decimal_to_hm(terbit))
print("Duha =",decimal_to_hm(duha))
print("Dzuhur =",decimal_to_hm(dzuhur))
print("Ashar =",decimal_to_hm(asar))
print("Maghrib =",decimal_to_hm(maghrib))
print("Isya =",decimal_to_hm(isya))
