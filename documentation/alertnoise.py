#Libraries necessary to send email using python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders


#Email of the Raspberry Pi
raspaddress = "teamgalaxynoise@gmail.com"

#User's Email address
useraddress = "zjabneel@gmail.com"

#Structure of the email
msg = MIMEMultipart()
msg['From'] = raspaddress
msg['To'] = useraddress
msg['Subject'] = "Aegis Alert Message"


def alert1(vidName):
    body1 = "Movement detected in the room \n"
    filename = vidName+"video.mp4"
    openAtt = "/home/pi/Desktop/Final Presentation/"+filename
    attachment = open(openAtt, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    return body1

def alert2():
    body2 = "Termperature Change Alert \n"
    return body2

def alert3():
    body3 = "Smoke Detected \n"
    return body3

def sendAlert(vidName):    
    body = alert1(vidName) 
    msg.attach(MIMEText(body, 'plain'))
    #Parameters for GMail Server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # Security function needed to connect to the Gmail server to protect the password.
    server.starttls()
    #Password of Raspberry Pi's Email
    server.login(raspaddress, "P@$$W0RD")
    #Sending the email
    text = msg.as_string()
    server.sendmail(raspaddress, useraddress, text)
    server.quit()
