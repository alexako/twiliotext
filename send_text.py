from twilio.rest import TwilioRestClient
import config
import sys


class TwilioText():
    def __init__(self):
        ACCOUNT_SID = config.ACCOUNT_SID
        AUTH_TOKEN = config.AUTH_TOKEN

        try:
            client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
            self.client = client
            print "Authentication successful"
        except:
            print "Error: Authentication unsuccessful"
            exit

    def send_text(self, message="Test message"):
        try:
            self.client.messages.create(
                    to = '+639175863509',
                    from_ = '+19283633688',
                    body = message
            )
            print "Message sent successfully"
        except:
            print "Error: Message not sent"


if __name__ == '__main__':

    if len(sys.argv) > 1:
        message = sys.argv[1]
    else:
        message = raw_input("Enter message: ")

    t = TwilioText()
    t.send_text(message)
