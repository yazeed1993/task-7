#######
# Q 1 #
#######
# rows = 6
# for xx in range(1, rows):
#     for i in range(1, xx + 1):
#         print(i, end=' ')
#     print("")

#######
# Q 2 #
#######
# number = int(input("Enter number: "))
# sum = 0
# for i in range(1, number + 1):
#     sum += i
# print('sum is :  ' + str(sum))

#######
# Q 3 #
#######

# l0 = input('enter your name ')
# for i in range(0,7):
#     for j in l0[0:i+1]:
#         print(j, end='')
#     print()
# for ii in range(0,7):
#     for jj in l0[0:-1-ii]:
#         print(jj, end='')
#     print()

#######
# Q 4 #
#######
# l0 = input('enter your name ')
# x=l0[::-1]
# print(x)

#######
# Q 5 #
#######
# num = int(input("Enter Range: "))
# i = num
# while ( i >= 1):
#     print (i, end = ' ')
#     i = i - 1

#######
# Q 6 #
#######
# for i in range(10):
#     print((i + 1) * 5, end=' ')

#######
# Q 7 #
#######
def num1():
    n0 = input('Enter the Limit_Number: ')
    n1 = int(input('Enter the maximum outputs to display (Max display_on_screen): '))
    n2 = int(input('Enter the Target_Number : '))
    for x in n0:
        for i in range(n1):
            print((i + 1) * n2, end=' ')
num1()






