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