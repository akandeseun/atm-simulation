# ATM Simulation Project Curated by Oluwaseun of the 44'squad. @stickers_NG :)

def welcome():
    print('''
          * * * * * * * * * * * * * * * * * * * * * * * * 
          *        WELCOME TO ABC BANK OF NIGERIA       *
          *                 ATM SERVICE                 *
          * * * * * * * * * * * * * * * * * * * * * * * *
                                                            ''')

# details_dictionary = {"0123456789": 1234, "12345678910": 1111, "0000000000": 2222}
# account_balance_dictionary = {"0123456789": 10000, "1234567891": 3000, "0000000000": 8000}





def main_menu():
    print('Main Menu')
    global menu_input
    menu_input = int(input('\t 1 - View My Balance \n'
                          '\t 2 - Withdraw Cash\n'
                          '\t 3 - Deposit Funds\n'
                          '\t 4 - Exit\n'
                          'Enter a choice:\n'))


def account_request_and_validation():
    i = 1
    # j = 0
    while(i <= 3):
        # j = j + 1
        global details_dictionary
        global account_balance_dictionary

        details_dictionary = {"0123456789": 12345}
        account_balance_dictionary = {"0123456789": 10000}
        try:
            global account_number_request
            global pin_number_request

            account_number_request = str(input('Enter your 10-digit Account Number\n'))
            pin_number_request = int(input('Enter your 5-digit Pin Number\n'))
        except ValueError:
            print('Please Enter a Valid Number')
            continue

        # Returns either true or false to know if given account number and pin correlates
        proceed = details_dictionary[account_number_request] == pin_number_request

        # Proceeds to main menu if pin is correct
        if proceed == True:
            main_menu()
            break
        # prompts user to re-enter if incorrect
        elif proceed == False:
            print('********** Incorrect Login Details, Please Re-enter************')
            print('********** NOTE THAT YOU WOULD BE LOGGED OUT AFTER 3 FAILED ATTEMPTS**********')
            Attempts = 'Attempt %d' % i
            print(Attempts)
            i = i + 1



def view_balance ():
    if account_number_request == '0123456789':
        print('Your Account Balance is ', '#', account_balance_dictionary["0123456789"])

    # go_back = input('press * to return to main menu')
    # if go_back == '*':
    #     main_menu()

def withdraw_cash():
    withdrawal_amount = int(input('\t 1 - 1000 Naira \n'
                           '\t 2 - 2000 Naira\n'
                           '\t 3 - 5000 Naira\n'
                           '\t 4 - 10000 Naira\n'
                           '\t 5 - 20000 Naira\n'
                           '\t 6 - Cancel Transaction\n'
                           'Enter a choice:\n'))
    if withdrawal_amount == 1:
        if (account_balance_dictionary['0123456789'] - 1000) < 0:
            print('Insufficient Funds')
            print('Current Balance is ', account_balance_dictionary['0123456789'])
        elif (account_balance_dictionary['0123456789'] - 1000) > 0:
            account_balance_dictionary['0123456789'] = account_balance_dictionary['0123456789'] - 1000
            print('******Withdrawal Successful******')
            print('Current Balance is ', account_balance_dictionary['0123456789'])

    #         WITHDRAWAL OPTION 2
    elif withdrawal_amount == 2:
        if (account_balance_dictionary['0123456789'] - 2000) < 0:
            print('Insufficient Funds')
            print('Current Balance is ', account_balance_dictionary['0123456789'])
        elif (account_balance_dictionary['0123456789'] - 2000) > 0:
            account_balance_dictionary['0123456789'] = account_balance_dictionary['0123456789'] - 1000
            print('******Withdrawal Successful******')
            print('Current Balance is ', account_balance_dictionary['0123456789'])

    #         WITTHDRAWAL OPTION 3
    elif withdrawal_amount == 3:
        if (account_balance_dictionary['0123456789'] - 5000) < 0:
            print('Insufficient Funds')
            print('Current Balance is ', account_balance_dictionary['0123456789'])
        elif (account_balance_dictionary['0123456789'] - 5000) > 0:
            account_balance_dictionary['0123456789'] = account_balance_dictionary['0123456789'] - 5000
            print('******Withdrawal Successful******')
            print('Current Balance is ', account_balance_dictionary['0123456789'])


def deposit_funds():
    deposit_amount = int(input('Please Enter the Deposit Amount: \n'))
    account_balance_dictionary['0123456789'] = account_balance_dictionary['0123456789'] + deposit_amount
    print('******Account Deposit Successful******')
    print('Your New Balance is ', account_balance_dictionary['0123456789'])

welcome()
account_request_and_validation()

if menu_input == 1:
    view_balance()
elif menu_input == 2:
    withdraw_cash()
elif menu_input == 3:
    deposit_funds()
elif menu_input == 4:
    print('You have exited the program')
    exit()




