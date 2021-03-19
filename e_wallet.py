import random
import twilio
import os
from twilio.rest import Client

account_sid = '*****'
auth_token = '*****'
client = Client(account_sid, auth_token)


class E_wallet:
    balance = 10000

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def sent(self, balance, amount):
        return balance - self.amount

    def balance(self, balance, amount):
        return f'Your balance is {balance - amount}'


user_amount = float(input("enter amount: "))
user1 = E_wallet("tendai", user_amount)
tendai_salary = user1.balance(balance=10000, amount=user_amount)
user_name = user1.name
user_balance = user1.balance

client.messages.create(
    to="+270000000",
    from_="+18154585706",
    body=f"hi {user_name}, Your salary is {user_balance} and your net salary is {tendai_salary}"
)
