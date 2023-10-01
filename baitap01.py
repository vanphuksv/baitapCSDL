def dao_nguoc_mang(mang):
    trai = 0
    phai = len(mang)-1

    while trai < phai:
        mang[trai],mang[phai]=mang[phai],mang[trai]
        trai += 1
        phai -= 1
mang = [1,2,3,4,5]
dao_nguoc_mang(mang)
print("mang sau khi dao nguoc:",mang)