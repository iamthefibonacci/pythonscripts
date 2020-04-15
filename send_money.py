"""Send money and receive a text script using Twilio"""

from twilio.rest import Client

balance = 3000

""" Get the Account ID and AUTH TOKEN from Twilion. Use this link to get free $10. www.twilio.com/referral/nXOWyq"""
client = Client("ACxxxxxxxxxxxxxxxxxxxxxxxx", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

receiver = input("Please enter the name of the receiver: ")
toSend = float(input("Enter amount to send "))

print("Do you want to send", toSend)
choice = input("Enter Y or N ")
if choice == "Y" or "y":
    send = balance - toSend
    print("Sending ", toSend, " to ", receiver, "has been successful. ")
    message = client.messages \
        .create(
            body="You have received " + str(toSend) + " from NAME",
            from_='+1xxxxxxxx',
            to='+27xxxxxxx',

        )

elif choice == "N" or "n":
    print("You are not send money")
    exitNow = input("Do you want to exit now? Press Y or N ")
    if exitNow == "Y" or "y":
        exit()
    elif exitNow == "N" or "n":
        print("Enter a proper value to send ")
else:
    exit()





