word =str(input())
print(word)
for mirror in range (len(word)-1,-1,-1):
    print(word[mirror],end="")
