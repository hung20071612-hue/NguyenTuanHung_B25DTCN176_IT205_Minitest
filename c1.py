price = float(input("Nhập đơn giá của sản phẩm: "))
quantity = int(input("Nhập số lượng hàng mua: "))
total_price = price * quantity
if total_price >= 1_000_000:
    total_price = total_price * 0.9
print(f"Số tiền cuối cùng mà khánh cần thanh toán: {total_price} VND")