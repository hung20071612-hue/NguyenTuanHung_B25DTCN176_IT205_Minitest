count = 0
sum_product = 0
while quantity_box_product != 0:
    quantity_box_product = int(input("Mời bạn nhập số sản phẩm cho mỗi thùng hàng"))
    if quantity_box_product < 0:
        print("Số lượng không hợp lệ, bỏ qua thùng này")
        continue
    elif quantity_box_product > 0:
        sum += quantity_box_product
        count += 1
print(f""" 
Tổng số thùng hàng hợp lệ đã đếm: {count}
Tổng số lượng sản phẩm thu được: {sum}
""")