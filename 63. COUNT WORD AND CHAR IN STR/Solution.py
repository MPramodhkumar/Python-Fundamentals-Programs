#python
str1=str(input())
char=0
word=1
for i in str1:
    char=char+1
    if (i==' '):
        word=word+1
print(word)
print(char)
