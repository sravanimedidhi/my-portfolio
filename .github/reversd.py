# def reversed_string(str):
#     if len(str) == 0:
#         return str
#     reversed_string(str[1:]) + str[0]
# print(reversed_string("Heloo"))





# text = "python"
# rev = ""
# i =len(text)-1
# while i>=0:
    
#     rev += text[i]
#     i -= 1
# print(rev)

text = "python"
rev = ""
i = len(text) - 1

while i >= 0:
    rev += text[i]
    i -= 1

print(rev)
