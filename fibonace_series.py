def febo(n):
    first_num=0
    sec_num=1
    r=n-3

    if n == 1:
        print(first_num)
    elif n == 2:
        print(first_num,sec_num)
    else:
         print(first_num, sec_num)
         for i in range(n-2):
             third_num= first_num + sec_num
             first_num=sec_num
             sec_num=third_num
             print(third_num)
nu=int(input("Enter a number:"))
febo(nu)
