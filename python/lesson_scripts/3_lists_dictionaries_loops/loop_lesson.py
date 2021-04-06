'''
What is a loop?

Allows you to repeat the same process many times
    with a small amount of code
    "iterating"

    each time a process is done '1 iteration'
'''

num_list = [.2, 0.89, -1.2, 0, 0.00000, 5.6, -.0003]

# for loops

# number is the 'iterator variable'
# changes each iteration of the loop
for number in num_list:
    print(number*100+32)


# combine the loop with logic
for number in num_list:
    if number > 0:
        print(f'{number} is positive!')
    elif number < 0:
        print(f'{number} is negative!')
    else:
        print(f'{number} is zero')