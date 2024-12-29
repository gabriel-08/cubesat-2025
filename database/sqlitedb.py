import sqlite3

conn = sqlite3.connect('coords.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE coordinates(
    Top_Left_Lat REAL,
    Top_Left_long REAL,
    Bot_Right_Lat REAL,
    Bot_Right_long REAL,
    Lights INTEGER,
    Year INTEGER,
    Month INTEGER,
    Day INTEGER,
    Hour INTEGER,
    Minute INTEGER,
    Second INTEGER); ''')
filenames = [[22.65, 113.82, 21.98, 114.54, 1, 2020, 11, 26, 11, 59, 23],
             [37.57, -122.29, 37.14, -121.51, 0, 2020, 11, 26, 11, 59, 23],
             [34.19, -118.53, 33.72, -117.91, 1, 2020, 11, 26, 11, 59, 56],
             [42.15, -106.24, 41.01, -104.08, 0, 2020, 11, 26, 11, 59, 23]]

for place in filenames:
    val = str(place[0]) + ", " + str(place[1]) + ", " + str(place[2]) + ", " + str(place[3]) + ", " + str(place[4]) + \
          ", " + str(place[5]) + ", " + str(place[6]) + ", " + str(place[7]) + ", " + str(place[8]) + ", " + str(
        place[9]) \
          + ", " + str(place[10])
    cursor.execute(f'''INSERT INTO coordinates VALUES({val}); ''')

rows = cursor.execute('''SELECT * FROM coordinates WHERE Top_Left_Lat = ''' + str(22.65) +
                           ''' AND Top_Left_Long = ''' + str(113.82) + ''' AND Bot_Right_Lat = ''' + str(21.98) +
                           ''' AND Bot_Right_Long = ''' + str(114.54) + ''';''')
for i in rows:
    print(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + " " + str(i[3]) + " " + str(i[4]) + " " + str(i[5]) + "\n")
