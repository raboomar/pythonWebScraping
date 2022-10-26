from twilio.rest import Client
import config


def createClient():
    account_sid = config.account_sid
    auth_token = config.auth_token
    client = Client(account_sid, auth_token)
    return client


def sendText(message):
    client = createClient()
    message = client.messages.create(
        body=message,
        from_=config.from_number,
        to=config.to_number
    )
