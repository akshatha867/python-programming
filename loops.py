# for i in range(1,11):
#     print(i)
# for i in range(1,21):
#     if i%2==0:
#         print(i)
# total=0
# for i in range(1,11):
#     toatl=total+i
# print(total)

# num=int(input("Enter a number:"))
# for i in range(1,11):
#     print(num*i)

#sum of digits
# total=0
# num=int(input("Enter a number:"))
# while(num>0):
#     rem=num%10
#     total=total+rem
#     num=num//10
# print(total)

#reverse a number
# num=123
# rev=0
# while(num>0):
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10

# print(rev)

#palindrome
# num=int(input("Enter a number:"))
# rev=0
# temp=num
# while(num>0):
#     rem=num%10
#     rev=rev*10+rem
#     num=num//10
# print(rev)
# if(rev==temp):
#     print("palindrome")
# else:
#     print("not a palindrome")

#counting the digits
# num=int(input("Enter a number:"))
# count=0
# num=abs(num)
# if num==0:
#     count=1
# while num>0:
#     num=num//10
#     count+=1
# print(count)


#sum of even digits
# num=int(input("Enter a number:"))
# total=0
# count=0
# while num>0:
#     rem=num%10
#     if rem%2==0:
#         total+=rem
#         count+=1
#     num=num//10
# print(total)
# print(count)

#count even and odd digits
num=int(input("Enter a number:"))
evenCount=0
oddCount=0

if num==0:
    evenCount+=1
while num>0:
    rem=num%10

    if rem%2==0 :
        evenCount+=1
        
    else:
        oddCount+=1
        
    num=num//10
print("Even count:",evenCount)
print("Odd count",oddCount)

