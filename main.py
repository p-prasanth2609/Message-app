from abc import ABC, abstractmethod
import re

class MessagingService(ABC):
    @abstractmethod
    def send_message(self):
        pass

class SMSMessagingService(MessagingService):
    def send_message(self, message, number):
        print(f"Message was successfully sent to {number}")

class EmailMessagingService(MessagingService):
    def send_message(self, message, email):
        print(f"Message was successfully sent to {email}")

class WhatsAppMessagingService(MessagingService):
    def send_message(self, message, number):
        print(f"Message was successfully sent to {number}")

class Validate:
    def is_valid_number(self, num):
        pattern = "^[6-9]\d{9}$"
        return re.match(pattern, num)

    def is_valid_email(self, email):
        pattern = r'[^@]+@[^@]+\.[a-z]+'
        return re.match(pattern, email)

if __name__ == '__main__':
    obj1 = SMSMessagingService()
    obj2 = EmailMessagingService()
    obj3 = WhatsAppMessagingService()
    validate = Validate()
    while True:
        print("Enter 1 to Send SMS")
        print("Enter 2 to Send Email")
        print("Enter 3 to Send WhatsApp")
        print("Enter 4 to quit")
        x = int(input("ENTER: "))

        if x == 4:
            print("Thank You!")
            quit()

        if x == 1:
            number = input("Enter number: ")
            if validate.is_valid_number(number):
                message = input("Enter Message to send: ")
                obj1.send_message(message, number)
            else:
                print("Invalid Number")

        if x == 2:
            email = input("Enter Email ID: ")
            if validate.is_valid_email(email):
                message = input("Enter the Message (Not more than 300 words): ")
                obj2.send_message(message, email)
            else:
                print("Incorrect Email Id")

        if x == 3:
            number = input("Enter number: ")
            if validate.is_valid_number(number):
                message = input("Enter Message to send: ")
                obj3.send_message(message, number)
            else:
                print("Invalid Number")
