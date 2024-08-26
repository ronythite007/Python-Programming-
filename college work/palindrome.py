try:
    str=input("enter the string : ")
    lenth=len(str)
    flag=0
    for i in range(0,lenth):
        if str[i]!=str[lenth-1-i]:
            flag=1
            break

    if flag:
        print ("String is not palimdrom")

    else:
        print("String is palimdrom")
    char=input("Enter the number of occurence of the character : ")
    count=0

    for j in str:
        if j == char:
            count+=1
    print("The character '",char,"' occure ",count," times")

    words=str.split()
    no_of_words=len(words)
    print("The number of words in string are ",no_of_words)
    a=0
    for k in words:
        a=len(k)
        for l in range(1,no_of_words):
            if a> len(words[l]):
                    print(k) 
except Exception as e:
    print("the error is ",e)
