from twilio.rest import Client

AccountSID = 'AC19460e393ee78da313b92a2156b487e1'
AuthToken = '59a42b278c17f1426bcdb01bc9d5a036'

client = Client(AccountSID, AuthToken)

from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+919000017580'

client.messages.create(body='TestMessage',
                       from_ = from_whatsapp_number,
                       to=to_whatsapp_number)
