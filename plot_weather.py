import pandas as pd
import matplotlib.pyplot as plt

# 🔍 Aseta tiedostonimi (vaihda tähän oikea nimi!)
excel_file = "weather_data.xlsx"

# 📂 Luetaan Excel-tiedosto
df = pd.read_excel(excel_file)

# 🔎 Tarkistetaan, mitkä sarakkeet on käytössä
print(df.head())

# 📊 Piirretään kaavio
plt.figure(figsize=(10,5))

# Oletetaan, että sarakkeet ovat nimettyinä näin Excelissä
plt.plot(df["Päivä"], df["Ilman keskilämpötila [°C]"], marker='o', linestyle='-', color='b', label="Keskilämpötila")
plt.plot(df["Päivä"], df["Ylin lämpötila [°C]"], marker='^', linestyle='--', color='r', label="Ylin lämpötila")
plt.plot(df["Päivä"], df["Alin lämpötila [°C]"], marker='v', linestyle='--', color='g', label="Alin lämpötila")

# 🎨 Muotoilu
plt.xlabel("Päivä")
plt.ylabel("Lämpötila (°C)")
plt.title(f"Säädata: {df['Havaintoasema'][0]} - {df['Kuukausi'][0]}/{df['Vuosi'][0]}")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.xticks(df["Päivä"])

# 📥 Tallennetaan kuva tiedostoksi
plt.savefig("weather_chart.png")

# 📤 Näytetään kaavio
plt.show()
