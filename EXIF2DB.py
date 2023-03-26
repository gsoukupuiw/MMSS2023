
import requests
import exifread
from io import BytesIO
import sqlite3
from sqlite3 import Error
from geopy import Point

# URL of the photo on the website
url = 'https://github.com/ianare/exif-samples/blob/master/jpg/gps/DSCN0010.jpg?raw=true'

# Download the photo and read the EXIF data
response = requests.get(url)
tags = exifread.process_file(BytesIO(response.content))

# Extract the GPS coordinates if available
if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
    latitude_ref = tags['GPS GPSLatitudeRef'].values
    latitude = tags['GPS GPSLatitude'].values
    longitude_ref = tags['GPS GPSLongitudeRef'].values
    longitude = tags['GPS GPSLongitude'].values

    # Convert the GPS coordinates to decimal degrees
    latitude = float(latitude[0].num) / float(latitude[0].den) + \
        float(latitude[1].num) / (float(latitude[1].den) * 60) + \
        float(latitude[2].num) / (float(latitude[2].den) * 3600)
    if latitude_ref == 'S':
        latitude = -latitude

    longitude = float(longitude[0].num) / float(longitude[0].den) + \
        float(longitude[1].num) / (float(longitude[1].den) * 60) + \
        float(longitude[2].num) / (float(longitude[2].den) * 3600)
    if longitude_ref == 'W':
        longitude = -longitude

    # Display the GPS coordinates
    print('Latitude: {}'.format(latitude))
    print('Longitude: {}'.format(longitude))
        # Save the URL, latitude, and longitude to a SQLite database
    try:
        conn = sqlite3.connect('photos.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS photos
                     (url text, latitude real, longitude real)''')
        c.execute("INSERT INTO photos VALUES (?, ?, ?)", (url, latitude, longitude))
        conn.commit()
        conn.close()
        print('Photo location saved to database.')
    except Error as e:
        print('Error saving photo location to database:', e)

else:
    print('GPS coordinates not found in photo EXIF data.')

    # Display the contents of the database
def display_database():
    try:
       conn = sqlite3.connect('photos.db')
       c = conn.cursor()
       c.execute('SELECT * FROM photos')
       rows = c.fetchall()
       for row in rows:
          print(row)
       conn.close()
    except Error as e:
       print('Error displaying database:', e)

display_database()
