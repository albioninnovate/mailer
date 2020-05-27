import mailer
import configparser
config = configparser.ConfigParser()
config.read('confg.ini')

account = 'wardhills.net'

user = config[account]['user']
password = config[account]['password']
server = config[account]['server']
port = config[account]['port_TLS']
sender = 'ward@albion-innovations.com'
receiver = 'ward@wardhills.net'
textfile = "test_file.txt"


msg = mailer.make_msg(textfile,sender,receiver)
mailer.send_msg(msg,user,password, server, port)