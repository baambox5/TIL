import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('PASSWORD : ')

msg = EmailMessage()
msg['Subject'] = '권고사직서'
msg['From'] = 'bkkohyes@naver.com'
people = input()
#for someone in people:
msg['To'] = 'bkkohyes@gmail.com'
msg.set_content('다음과 같은 사유로 부득이하게')

ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
ssafy.login('bkkohyes', password)
ssafy.send_message(msg)

print('이메일 전송 완료!')