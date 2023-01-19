import imaplib
from imap_tools import MailBox, AND
import re
import analyze

# Read the email address and password from the file
with open('id.txt', 'r') as f:
	lines = f.readlines()
	email = lines[0].strip().split(':')[1]
	pwd = lines[1].strip().split(':')[1]
	apikey = lines[2].strip().split(':')[1]

# Extract the domain from the email address
domain = email.split('@')[1]

# Define the IMAP server address
imap_server_addr = ""
if domain == "outlook.fr":
	imap_server_addr = "imap-mail.outlook.com"
else:
	# Use a default server address, or use DNS to lookup the server address
	imap_server_addr = "imap." + domain

# Get date, subject and body len of all emails from INBOX folder
"""
with MailBox(imap_server_addr).login(email, pwd) as mailbox:
	for msg in mailbox.fetch():
		print(f"\n    Le {msg.date} \n\t{msg.subject}\n    {msg.text}")
"""