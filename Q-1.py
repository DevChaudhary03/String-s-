a = int(input())
vowels = "aeiouAEIOU"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(a):
    s = input()
    v = 0
    c = 0
    for i in s:
        if i in vowels:
            v += 1
        elif i in letters:
            c += 1
    print(v, c)




