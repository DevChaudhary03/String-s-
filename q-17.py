# a=input()
# a=a+a
# r=' '
# if ch in a:
#     if not ch.isupper():
#         r+=ch
# f=''
# for ch in r:
#     if ch in 'aeiou':
#         f+='#'
#     else:
#         f+=ch
# print(f)

a=input()
a=a+a
r=''.join(ch for ch in a if ch.islower())
f=''.join('#'if ch in 'aeiouAEIOU' else ch for ch in r)
print(f)