import smtplib
import os
from email.message import EmailMessage

# 📩 Aseta vastaanottajan sähköposti
receiver_email = "katja.turtiainen@student.laurea.fi"
sender_email = "katjaturtiainen3@gmail.com"  # ⚠️ VAIHDA TÄMÄ OMAAN LÄHETTÄJÄSÄHKÖPOSTIISI
password = "uixn edsg amdr sisw"  # ⚠️ VAIHDA OMAAN SÄHKÖPOSTISALASANAASI

# 📨 Luo sähköposti
msg = EmailMessage()
msg["Subject"] = "Säähavaintoraportti"
msg["From"] = sender_email
msg["To"] = receiver_email
msg.set_content("Hei,\n\nTässä on tuorein säähavaintoraportti PDF-muodossa.\n\nTerveisin,\nAutomaattinen säärobotti")

# 📎 Liitetään PDF mukaan
pdf_path = "weather_report.pdf"
with open(pdf_path, "rb") as pdf_file:
    msg.add_attachment(pdf_file.read(), maintype="application", subtype="pdf", filename=os.path.basename(pdf_path))

# 📬 Lähetetään sähköposti
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.send_message(msg)
    print("✅ Sähköposti lähetetty!")
except Exception as e:
    print(f"❌ Virhe sähköpostin lähetyksessä: {e}")
