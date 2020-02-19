import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path #for reading files into a string of text

#read html file
html = Template(Path('email-template.html').read_text())

#email object
email = EmailMessage()
email['from'] = 'Mail Sender'
email['to'] = 'jobo4481@gmail.com'
email['subject'] = 'Send mail with Python'

email.set_content(html.substitute({'name': 'James Jobo'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() #say hello to server
    smtp.starttls() #enable encrpytion
    smtp.login('msender235@gmail.com', 'S!9my@Lx6#')
    smtp.send_message(email)
    smtp.quit()
    print('Finish sending :)')
