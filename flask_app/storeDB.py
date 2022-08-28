import sqlite3
import pandas as pd

PATH = '.'


#get csv
df = pd.read_csv(f"{PATH}/spotify_music.csv", index_col = 0)

#split into 2 dataframes
dropCol = ['artist','album','track_number', 'name']
analytics = df.drop(columns = dropCol).drop(columns = 'uri')
info = df[dropCol]
info.insert(loc=0, column='id', value=df['id'])

#connector, cursor
conn = sqlite3.connect(f"{PATH}/spotify.db")
c = conn.cursor()

#create table : info
c.execute("""CREATE TABLE IF NOT EXISTS info(
	id TEXT PRIMARY KEY,
	artist TEXT NOT NULL,
	album TEXT NOT NULL,
	track_number INT,
    name TEXT
);""")

# #create table : analytics
c.execute("""CREATE TABLE IF NOT EXISTS analytics(
	id TEXT PRIMARY KEY,
	acousticness FLOAT NOT NULL,
	danceability FLOAT NOT NULL,
	energy FLOAT NOT NULL,
	instrumentalness FLOAT NOT NULL,
	liveness FLOAT NOT NULL,
	loudness FLOAT NOT NULL,
	speechiness FLOAT NOT NULL,
	tempo FLOAT NOT NULL,
	valence FLOAT NOT NULL,
	popularity INT NOT NULL,

	FOREIGN KEY (id)
		REFERENCES info (id)
		ON DELETE CASCADE 
        ON UPDATE NO ACTION
);""")


#insert data : info
query_i = "INSERT INTO info VALUES (?,?,?,?,?)"
values_i = info.values.tolist()
c.executemany(query_i, values_i)
conn.commit()

#insert data : analytics
query_a = "INSERT INTO analytics VALUES (?,?,?,?,?,?,?,?,?,?,?)"
values_a = analytics.values.tolist()
c.executemany(query_a, values_a)
conn.commit()

#end connection
conn.close()