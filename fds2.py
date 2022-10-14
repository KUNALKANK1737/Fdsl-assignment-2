def frequency():
    
    char = input("enter the char who's freq is to be find :")
    count=0
    for i in str1:
        if (char==i):
            count=count+1
    print ("The character {} is repeated {} times".format(char,count))
def longest_length():
    l=str1.split()
    print(l)
    n=0
    for i in range (len(l)):
        if n<len(l[i]):
            n=len(l[i])
    print("longest lenght is in string is ",n)
def palindrome():
    
    i=0
    str2=str1[::-1]
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            print ("it is not  a palindrome")
        else:
            print("it is a palindrome")
            break
def substring():
    v=input("enter the substring to be found :")
    l=str1.split()
    for s in l:
        if v in s:
          print("{} is present in string ".format(v))
        else:
            print("it is not present in the string :")
        break
i=0
while(i==0):
 print("press 1:frequency\npress 2:longest_length\npress 3:palindrome\npress 4:substring")
 o=int(input("enter your choice :"))
 if(o==1):
    str1=input("enter the string :")
    n=len(str1)
    frequency()
 if(o==2):
    str1=input("enter the string :")
    n=len(str1)
    longest_length()
 if(o==3):
    str1=input("enter the string :")
    n=len(str1)
    palindrome()
 if(o==4):
    str1=input("enter the string :")
    n=len(str1)
    substring()
