import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("jaishwarya675@gmail.com", "vijaysurya")
 
msg = "hi"
server.sendmail("jaishwarya675@gmail.com", "aishwarya17ec@gmail.com", msg)
server.quit()
