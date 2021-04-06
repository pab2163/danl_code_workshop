'''
Complimentary funcationatly to lists

DO NOT have order

DO have labels

All data are stored in key-values

key:value

word:definition

key to data : data itself
'''

user_account = {'username': 'paul',
                'password': '78eg2',
                'year': 2021,
                'transations': [2, 45.1, 99.0]}


print(user_account)

# getting specific data by NAME from a dictionary

print(user_account['password'])

print(user_account['username'])

print(user_account.keys())