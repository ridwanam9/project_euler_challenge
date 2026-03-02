# 0 = Senin, 1 = Selasa, ..., 6 = Minggu
day_of_week = 0  # 1 Jan 1900 adalah Senin

count = 0

for year in range(1900, 2001):
    
    for month in range(1, 13):
        
        # Hitung hanya jika tahun >= 1901
        if year >= 1901 and day_of_week == 6:
            count += 1
        
        # Tentukan jumlah hari dalam bulan
        if month in [4, 6, 9, 11]:  # April, Juni, Sept, Nov
            days = 30
        elif month == 2:  # Februari
            # Cek tahun kabisat
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                days = 29
            else:
                days = 28
        else:
            days = 31
        
        # Geser hari ke tanggal 1 bulan berikutnya
        day_of_week = (day_of_week + days) % 7

print(count)