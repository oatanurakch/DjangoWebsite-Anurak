import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendthai(sendto, subj, detail):

	myemail = 'anurakch.django@gmail.com'
	mypassword = 'anrpnd310363'
	receiver = sendto

	msg = MIMEMultipart('alternative')
	msg['Subject'] = subj
	msg['From'] = 'AI-LINK Co.'
	msg['To'] = receiver
	text = detail

	part1 = MIMEText(text, 'plain')
	msg.attach(part1)

	s = smtplib.SMTP('smtp.gmail.com:587')
	s.ehlo()
	s.starttls()

	s.login(myemail, mypassword)
	s.sendmail(myemail, receiver.split(','), msg.as_string())
	s.quit()


###########Start sending#############
subject = 'ทดสอบระบบการส่ง E-Mail'

msg = '''Welcome to AI-Link
ขอบคุณที่ไว้วางใจสั่งซื้อสินค้าของบริษัทเรา
เราจะพัฒนาสินค้าให้ดียิ่ง ๆ ขึ้นไป
'''

sendthai('oatty6106164@gmail.com', subject, msg)