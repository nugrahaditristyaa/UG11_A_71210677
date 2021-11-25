def ambil_tengah(a1, a2=0):
    if(a2):
        dihitung = len(a1)
        dibagi = (dihitung // 2)
        return(a1[dibagi+a2])
    else:
        dihitung = len(a1)
        dibagi = (dihitung // 2)
        return(a1[dibagi])

print(ambil_tengah("abcdefg",1))
print(ambil_tengah("abcdefg",2))
print(ambil_tengah("abcd"))
