from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import pandas as pd

# 🔹 Määritetään tiedostot
excel_file = "weather_data.xlsx"
pdf_file = "weather_report.pdf"
image_file = "weather_chart.png"

# 🔍 Luetaan Excel-tiedosto
df = pd.read_excel(excel_file)

# 📄 Luodaan PDF-tiedosto
c = canvas.Canvas(pdf_file, pagesize=A4)
width, height = A4

# 📝 Otsikko
c.setFont("Helvetica-Bold", 16)
c.drawString(50, height - 50, f"Säähavaintoraportti: {df['Havaintoasema'][0]}")
c.setFont("Helvetica", 12)
c.drawString(50, height - 70, f"Päivämäärä: {df['Päivä'][0]}.{df['Kuukausi'][0]}.{df['Vuosi'][0]}")

# 📊 Lisätään kaavio
chart = ImageReader(image_file)
c.drawImage(chart, 50, height - 350, width=500, height=250)

# 📋 Lisätään havaintotiedot
c.setFont("Helvetica", 10)
c.drawString(50, height - 370, f"Keskilämpötila: {df['Ilman keskilämpötila [°C]'][0]} °C")
c.drawString(50, height - 390, f"Ylin lämpötila: {df['Ylin lämpötila [°C]'][0]} °C")
c.drawString(50, height - 410, f"Alin lämpötila: {df['Alin lämpötila [°C]'][0]} °C")
c.drawString(50, height - 430, f"Sademäärä: {df['Sademäärä [mm]'][0]} mm")
c.drawString(50, height - 450, f"Lumensyvyys: {df['Lumensyvyys [cm]'][0]} cm")

# 📌 Tallennetaan PDF
c.save()

print(f"✅ PDF-raportti luotu: {pdf_file}")
