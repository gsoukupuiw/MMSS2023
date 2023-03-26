from github import Github
import requests
import exifread
from io import BytesIO
import sqlite3
from sqlite3 import Error
from geopy import Point
import urllib
import urllib3
from urllib.parse import urljoin

def githubstuff():
    # Replace the username, repository name and access token with your own values
    username = "gsoukupuiw"
    repository_name = "MMSS2023"
    access_token = "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"

    # Authenticate with the GitHub API using an access token
    g = Github(access_token)

    # Get the user or organization that owns the repository
    user = g.get_user(username)

    # Get the repository by its name
    repo = user.get_repo(repository_name)

    # Get the contents of a specific file in the repository
    file_contents = repo.get_contents("Images")

    # Get the first item in the list (which is the only item)
    file_content = file_contents

    # Print the content of the file
    #print(file_content)
    return file_contents

def uhhidk(url):
    # URL of the photo on the website
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
    #display_database()




def remove_duplicates(db_file, unique_column):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # get the name of the table from the database file
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table_name = c.fetchone()[0]

    # select all rows and their unique values in the specified column
    c.execute(f'SELECT *, COUNT({unique_column}) FROM {table_name} GROUP BY {unique_column} HAVING COUNT({unique_column}) > 1')
    rows = c.fetchall()

    # loop through the rows with duplicate values and delete all but the first one
    for row in rows:
        c.execute(f"DELETE FROM {table_name} WHERE rowid > ? AND {unique_column} = ?", (row[0], row[-2]))

    conn.commit()
    conn.close()


def doAthing():
    remove_duplicates('photos.db','url')
    masterurl = "https://github.com/gsoukupuiw/MMSS2023/blob/master/Images"
    file_contents = githubstuff()
    i = 0
    for item in file_contents:
        print(file_contents[i].path)
        holdurl = urljoin(masterurl,file_contents[i].path)
        passurl = urljoin(holdurl,'?raw=true')
        print(passurl)
        uhhidk(passurl)
        i+=1

