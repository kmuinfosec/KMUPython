# 주문 받기 심화


def more_order(question):
    if question == "네":
        pass
    elif question == "아니오":
        print("알겠습니다.")
    else:
        more_order(input("네?? 다시 한 번 말씀해주시겠어요?"))


menu = {"옛날김밥":2500, "치즈김밥":3000, "참치김밥":3000}
print("메뉴판->", menu)
price = 0
while True:
    order = input("주문 도와드리겠습니다.\n")
    try:
        print("{}은 {}원입니다. 몇 개 주문하시겠습니까?".format(order, menu[order]))
    except KeyError:
        print("그 메뉴는 팔지 않는 것 같습니다. 메뉴판을 다시 한 번 확인부탁드립니다. ")
        print(menu)
    else:
        count = int(input())
        price += menu[order] * count
        answer = input("더 필요한 것이 있으신가요? -> 네/아니오")
        more_order(answer)
        if answer == "아니오":
            if price == 0:
                print("주문한 내역이 없으십니다.")
                continue
            else:
                print("결제 도와드리겠습니다. 총 {}원입니다.".format(price))
                break
