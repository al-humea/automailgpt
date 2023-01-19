import imaplib, email

with open("./id.txt", "r") as r:
	lines = r.readlines()
	email = lines[0].split(":")[1]
	pwd = lines[1].split(":")[1]
	imap_url = "imap." + email.split("@")[1]

con = imaplib.IMAP4_SSL(imap_url)
con.login(email, pwd)