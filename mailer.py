# Import smtplib for the actual sending function
import smtplib
import configparser
config = configparser.ConfigParser()
config.read('confg.ini')

# Import the email modules we'll need
from email.message import EmailMessage

"""
Google does not allow smtp requests "allow less secure apps" need to be enabbled. 
https://support.google.com/accounts/answer/6010255

https://www.google.com/settings/security/lesssecureapps
"""

#account = 'Makespace_gmail'
#account = 'gmail'
account = 'wardhills.net'

user = config[account]['user']
password = config[account]['password']
server = config[account]['server']
port = config[account]['port_TLS']

# The body of the email is the content of the text file.
textfile = 'mail_body.txt'

sender = 'ward@albion-innovations.com'
receiver = 'ward@wardhills.net'


def make_msg(textfile, sender, receiver):
    # Open the plain text file whose name is in textfile for reading.
    with open(textfile) as fp:
        # Create a text/plain message
        msg = EmailMessage()
        msg.set_content(fp.read())

    msg['Subject'] = f'The contents of {textfile}'
    msg['From'] = sender
    msg['To'] = receiver
    return msg

def send_msg(msg,user,password, server, port):
    print('msg :',msg)
    # Send the message via our own SMTP server.
    s = smtplib.SMTP(server, port)
    # Handshake with server
    s.ehlo()
    s.starttls()
    s.login(user,password)
    s.send_message(msg)
    s.quit()


if __name__ == '__main__':
    msg = make_msg(textfile, sender, receiver)
    send_msg(msg,user,password, server, port)


