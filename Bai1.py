import bai4 as inchuoi
def CongChuoi(a,b):
    return(a+ " -> " +b)

#Ham tim ten hs
def TimTen(hoten,ten):
    id=1
    for i in hoten:
        if i==ten:
            print("Tim thay roi:",inchuoi.InHoa(CongChuoi(ten,str(id))))
            break
        else:
            id=id+1
    if id==len(hoten)+1:
        print("Khong tim thay!")
    