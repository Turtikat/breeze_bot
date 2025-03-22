import requests

url = "https://fmiodata-timeseries-convert.fmi.fi/Tohmajärvi_Kemie...xlsx"  # Kopioi robottikonsolista
response = requests.get(url)
with open("weather_data.xlsx", "wb") as f:
    f.write(response.content)

print("✅ Excel ladattu onnistuneesti!")
