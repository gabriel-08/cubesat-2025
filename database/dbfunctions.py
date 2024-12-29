import sqlite3


def create():
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

    conn.close()


def write(data):
    conn = sqlite3.connect('coords.db')
    cursor = conn.cursor();
    val = str(data[0]) + ", " + str(data[1]) + ", " + str(data[2]) + ", " + str(data[3]) + ", " + str(data[4]) + \
          ", " + str(data[5]) + ", " + str(data[6]) + ", " + str(data[7]) + ", " + str(data[8]) + ", " + str(data[9]) \
          + ", " + str(data[10])
    cursor.execute(f'''INSERT INTO coordinates VALUES({val}); ''')
    conn.close()


def get_filter(tllat, tllong, brlat, brlong):
    conn = sqlite3.connect("coords.db")
    cursor = conn.cursor()
    rows = cursor.execute('''SELECT * FROM coordinates WHERE Top_Left_Lat = ''' + str(tllat) +
                          ''' AND Top_Left_Long = ''' + str(tllong) + ''' AND Bot_Right_Lat = ''' + str(brlat) +
                          ''' AND Bot_Right_Long = ''' + str(brlong) + ''';''')
    for i in rows:
        print(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + " " + str(i[3]) + " " + str(i[4]) + " " + str(i[5])
              + "\n")
    conn.close()


def get():
    conn = sqlite3.connect("coords.db")
    cursor = conn.cursor()
    rows = cursor.execute('''SELECT * FROM coordinates''')
    for i in rows:
        print(str(i[0]) + " " + str(i[1]) + " " + str(i[2]) + " " + str(i[3]) + " " + str(i[4]) + " " + str(i[5])
              + "\n")
    conn.close()


create()

filenames = [[22.65, 113.82, 21.98, 114.54, 1, 2020, 11, 26, 11, 59, 23],
             [37.57, -122.29, 37.14, -121.51, 0, 2020, 11, 26, 11, 59, 23],
             [34.19, -118.53, 33.72, -117.91, 1, 2020, 11, 26, 11, 59, 56],
             [42.15, -106.24, 41.01, -104.08, 0, 2020, 11, 26, 11, 59, 23]]

for place in filenames:
    write(place)

get_filter(22.65, 113.82, 21.98, 114.54)
get()
