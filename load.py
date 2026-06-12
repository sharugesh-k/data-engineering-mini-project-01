import psycopg2
import Transform

df = Transform.df

conn = psycopg2.connect(
    host="localhost",
    database="weather_db",
    user="postgres",
    password="sharugesh"
)

print("Connected!")

cursor = conn.cursor()
print("Cursor created!")

for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO weather_data
        (latitude, longitude, timezone, temperature,
         windspeed, winddirection, weathercode)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            row["latitude"],
            row["longitude"],
            row["timezone"],
            row["temperature"],
            row["windspeed"],
            row["winddirection"],
            row["weathercode"]
        )
    )

conn.commit()

