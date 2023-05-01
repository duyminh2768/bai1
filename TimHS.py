hoten=""
print("bam phim # de dung")
thutu=-1
ds=[]
while hoten!="#":
    hoten=str(input("Nhap ho ten:"))
    thutu=thutu+1
    if hoten!="#":
        ds.append(hoten)
    
        


print(ds)



def tim(ds,hoten):
    #Tham so ds: Danh sach ho ten
    #Tham so hoten: Ho ten can tim
    id=1
    for i in ds:
        if i == hoten:
            print("so thu tu cua",hoten,"la",id)
            break
        else:
            id=id+1
    
    if id >len(ds):
            print("ko co trg danh sach")
    return()

tencantim=str(input("ten can tim la:"))
print(tim(ds,tencantim))