import pandas as pd
import extract

data = extract.data

df = pd.json_normalize(data)

columns_to_keep = [
    "latitude",
    "longitude",
    "timezone",
    "current_weather.temperature",
    "current_weather.windspeed",
    "current_weather.winddirection",
    "current_weather.weathercode"
]



df=df[columns_to_keep]
print(df.head())

df = df.rename(columns={
    "current_weather.temperature": "temperature",
    "current_weather.windspeed": "windspeed",
    "current_weather.winddirection": "winddirection",
    "current_weather.weathercode": "weathercode"
})

print(df.columns)