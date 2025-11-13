# #check word with more vowels and consonants . for each given string ,print wheather it contains more vowels or more consonants.

# a=int(input()) 
# vowels="aeiouAEIOU"
# letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"   
# for i in range (a):
#     s=input()
#     v=0
#     c=0
#     for i in s:
#         if i in  vowels:
#             v+=1
#         elif i in letters:
#             c+=1
#     if v>c:
#         print("more Vowels")
#     elif v<c:
#         print("more letters")
#     else:
#         print("same number")
    

#Q- check and print count of the vowels and the consonants in a word
a=int(input())
vowels="aeiouAEIOU"
consonants="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range (a):
    s=input()
    v=0
    c=0
    for i in s:
        if i in vowels:
            v+=1
        elif i in consonants:
            c+=1
    print("total vowels"+str(v))
    print("total consonanta"+str(c))

