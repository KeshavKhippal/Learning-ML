forw=0
back=-1
str="hello"
while(forw<len(str)//2):
    if str[forw]!=str[back]:
        print("Not ")
        break
    forw+=1
    back-=1
print("Palin")