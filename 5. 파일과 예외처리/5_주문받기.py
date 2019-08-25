# 주문 받기


def menu(m, all_menu):
    if m not in all_menu:
        raise NameError("{}은(는) 메뉴판에 없습니다, 손님.".format(m))
    else:
        print("{} 주문받았습니다.".format(m))


menulist = ["짜장면", "짬뽕"]
print("메뉴판 ->", menulist)
question = input("주문 도와드리겠습니다.\n")

try:
    menu(question, menulist)
except NameError as e:
    print(e)