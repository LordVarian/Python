import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('username', 'password')
conn.sendmail('sender', 'receiver', 'message')
conn.quit()