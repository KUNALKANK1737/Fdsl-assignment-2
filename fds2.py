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
    
    #for n in  range (0,-1):
     #   reverse=str1[n-i] 
      #  print(reverse)
    i=0
    for i in range(len(str1)):
        if str[i]!=str1[-1-i]:
            print ("it is not  a palindrome")
        else:
            print("it is a palindrome")
            break


 
str1=input("enter the string :")
n=len(str1)
frequency()
longest_length()
palindrome()
    
