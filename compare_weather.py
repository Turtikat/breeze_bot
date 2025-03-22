import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

# 🔹 Asetetaan tiedostonimi
excel_file = "downloads/weather_data.xlsx"
pdf_file = "weather_comparison.pdf"

# 📂 Tarkistetaan, että tiedosto on ladattu
if not os.path.exists(excel_file):
    print("❌ Excel-tiedostoa ei löydy!")
    exit()

# 📊 Luetaan Excel-tiedosto
df = pd.read_excel(excel_file)

# 🔍 Haetaan kuukauden sadesumma ja keskilämpötila
sadesumma = df["Sademäärä [mm]"].sum()
keskilampo = df["Ilman keskilämpötila [°C]"].mean()

# 🔍 Haetaan edellisen vuoden vastaavat arvot
prev_year_excel = "downloads/weather_data_last_year.xlsx"  # HUOM: Varmista, että tämä on ladattu aiemmin
if os.path.exists(prev_year_excel):
    df_last_year = pd.read_excel(prev_year_excel)
    sadesumma_last_year = df_last_year["Sademäärä [mm]"].sum()
    keskilampo_last_year = df_last_year["Ilman keskilämpötila [°C]"].mean()
else:
    sadesumma_last_year = None
    keskilampo_last_year = None

# 📝 Luodaan PDF-raportti
c = canvas.Canvas(pdf_file, pagesize=A4)
width, height = A4

c.setFont("Helvetica-Bold", 16)
c.drawString(50, height - 50, "Kuukausittainen säävertailu")

c.setFont("Helvetica", 12)
c.drawString(50, height - 80, f"Kuukausi: {df['Kuukausi'][0]}/{df['Vuosi'][0]}")
c.drawString(50, height - 100, f"Sadesumma: {sadesumma:.1f} mm")
c.drawString(50, height - 120, f"Keskilämpötila: {keskilampo:.1f} °C")

if sadesumma_last_year is not None and keskilampo_last_year is not None:
    sadesumma_diff = sadesumma - sadesumma_last_year
    keskilampo_diff = keskilampo - keskilampo_last_year

    c.drawString(50, height - 140, f"Edellinen vuosi: {sadesumma_last_year:.1f} mm, {keskilampo_last_year:.1f} °C")
    c.drawString(50, height - 160, f"Erotus: {sadesumma_diff:+.1f} mm, {keskilampo_diff:+.1f} °C")

c.save()
print(f"✅ PDF-raportti luotu: {pdf_file}")
