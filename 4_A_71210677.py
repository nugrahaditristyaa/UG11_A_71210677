def ambildanbalik(a1,b2,c3,h):
    if(h):
        h = a1[b2-1:c3]
        return(h[::-1])
    elif(not h):
        return(a1[b2-1:c3])
    else:
        print("Maaf, salah input")
print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("Qwerty",3,4,True))
print(ambildanbalik("Qwerty",2,2,False))
    
