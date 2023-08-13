#######
# Q 1 #
#######
def num_row():
    rows = 6
    for xx in range(1, rows):
        for i in range(1, xx + 1):
            print(i, end=' ')
        print("")


num_row()
#######
# Q 2 #
#######
def num_calc():
    number = int(input("Enter number: "))
    sum = 0
    for i in range(1, number + 1):
        sum += i
    print('sum is :  ' + str(sum))

num_calc()
#######
# Q 3 #
#######
def prnt_name():
    l0 = input('enter your name ')
    for i in range(0, 7):
        for j in l0[0:i + 1]:
            print(j, end='')
        print()
    for ii in range(0, 7):
        for jj in l0[0:-1 - ii]:
            print(jj, end='')
        print()

prnt_name()


#######
# Q 4 #
#######
def rev_name():
    l0 = input('enter your name ')
    x = l0[::-1]
    print(x)

rev_name()


#######
# Q 5 #
#######

def num_rev_range():
    num = int(input("Enter Range: "))
    i = num
    while (i >= 1):
        print(i, end=' ')
        i = i - 1


num_rev_range()

#######
# Q 6 #
#######

def num_multi():
    for i in range(10):
        print((i + 1) * 5, end=' ')


num_multi()

#######
# Q 7 #
#######
def limit_num():
    limit = int(input('Enter the Limit_Number: '))
    maxi = int(input('Enter the maximum outputs to display (Max display_on_screen): '))
    target = int(input('Enter the Target_Number : '))

    for i in range(maxi):

        res = (i + 1) * target
        if res >= limit:
            break
        print(res, end=' ')


limit_num()