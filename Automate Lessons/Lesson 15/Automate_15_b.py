import imapclient
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('username', 'password')
conn.select('INBOX', readonly=True)
UIDs = conn.search(['SINCE 20-Aug-2015'])
rawMessage = conn.fetch(UIDs[0], ['BODY[]','FLAGS'])
import pyzmail
message = pyzmail.PyzMessage.factory(rawMessage[0][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('bcc')
print(message.text_part)
print(message.html_part)
message.text_part.get_payload().decode('utf-8')
print(message.text_part.charset)
conn.list_folders()
conn.select_folder('INBOX',readonly=False)
UIDs = conn.search(['SINCE 20-Aug-2015'])
conn.delete_messages(UIDs[1])
conn.logout()