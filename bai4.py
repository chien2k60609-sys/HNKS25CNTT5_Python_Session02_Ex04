name = input('Nhập họ và tên bệnh nhân: ')
age = int(input('Nhập tuổi bệnh nhân: '))
systolic_bp = int(input('Nhập huyết áp tâm thu (mmHg): '))
blood_sugar = int(input('Nhập đường huyết (mg/dL): '))

if age < 0 or age > 150 or systolic_bp < 0 or blood_sugar < 0:
    print('Dữ liệu nhập vào không hợp lệ')
else:
    if age < 75 and 90 <= systolic_bp <= 140 and blood_sugar < 150:
        print('ĐỦ ĐIỀU KIỆN PHẪU THUẬT')
    else:
        print('TỪ CHỐI PHẪU THUẬT')