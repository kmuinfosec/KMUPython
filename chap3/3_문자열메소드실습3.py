print("핸드폰 번호를 입력합니다. 하나씩 차근차근 입력해주세요.")
phonenumber=""
for j in range(11):
    phone = input("")
    if phone.isdecimal():
        phonenumber += phone
        if j == 2 or j ==6:
            phonenumber += "-"
    else:
        print("숫자가 입력되지않았습니다. 실행을 중지합니다.")
        exit()
if len(phonenumber) == 13:
    print(phonenumber)
