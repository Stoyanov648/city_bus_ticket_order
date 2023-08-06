import sys
from datetime import datetime
# This is a program for traveling with the city buss in Sofia,Bulgaria
# every ticket costs X amount of bgn and after every third transaction,
# tickets become free until the next day
paid_dict = {}  # The transaction registry
ticket_dict = {}  # The ticket registry


def get_card():
    """get_card will accept only 12 int digits like a real debit card,
    and this function will also prevent any crashes scenarios with multiple exceptions"""
    loop_until = 0
    while loop_until != 1:
        try:
            num = int(input('Insert card number here: '))
            if len(str(num)) == 12:
                loop_until = 1  # Set loop_until to 1 to exit the while loop
                return num
            else:
                print("Enter valid 12 digit Card Number")
        except ValueError:
            print("Invalid Card Number")
        except EOFError:
            print("Invalid Card Number")
            sys.exit()  # this program imitates the card payment in the buss, so there won't be a "ctr+D" option
            #  and it remains as my exit shortcut.


def get_card_number(number: int):
    """This function will accept the card_owner's card detail.
    After accepting the details it's going to check if the cardholder,
    is in the Paid dict,and if not, will register him.After every second transaction per unique card number,
     the tickets will be free for the end of the day"""
    if number not in paid_dict:
        paid_dict[number] = f"Card: {number}'s ticket has been successfully issued! Enjoy your ride!"
        ticket_dict[number] = f'first ticked ID:{number} issued on {datetime.now()}'
        print(f'{paid_dict[number]}')
        print('\t\t', ticket_dict[number])
        print('\t\t\t1.60 BGN Charged')
    elif number in paid_dict and paid_dict[number] == (f"Card: {number}'s ticket has been successfully "
                                                       f"issued! Enjoy your ride!"):
        paid_dict[number] = f"Card: {number}'s second ticket has been successfully issued! Enjoy your ride!"
        ticket_dict[number] = f'Second ticket with ID:{number} issued on {datetime.now()}'
        print(f'{paid_dict[number]}')
        print('\t\t', ticket_dict[number])
        print('\t\t\t1.60 BGN Charged')
    elif number in paid_dict and paid_dict[number] == (f"Card: {number}'s second ticket has been successfully "
                                                       f"issued! Enjoy your ride!"):
        paid_dict[number] = f"Card: {number}'s third ticket has been successfully issued! Enjoy your ride!"
        ticket_dict[number] = f'Daily ticket with ID:{number} issued on {datetime.now()}'
        print(f"{ticket_dict[number]}")
        print('\t\t', ticket_dict[number])
        print('\t\t\t0.80 BGN Charged')
    elif number in paid_dict and paid_dict[number] == (f"Card: {number}'s third ticket has been successfully "
                                                       f"issued! Enjoy your ride!"):
        print(f'\tCard: {number} will travel for free, we wont charge this card more than 4 BGN per day ')
        print(f'\t\t {ticket_dict[number]} will last until the end of the day')


while True:
    get_card_number(get_card())
