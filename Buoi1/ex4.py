#tạo ds rỗng để lưu KQ
j=[]
#Duyệt qua tất cả số trong đoạn từ 2000->3200, xem có % 7 và không phải bội số của 5
for i in range(2000, 3200):
    if(i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print (",".join(j))