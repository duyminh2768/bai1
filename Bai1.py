def CongChuoi(a,b):
    return(a+ "-" +b)

#Ham tim ten hs
def TimTen(hoten,ten):
    id=1
    for i in hoten:
        if i==ten:
            print("Tim thay roi:",id)
        else:
            id=id+1