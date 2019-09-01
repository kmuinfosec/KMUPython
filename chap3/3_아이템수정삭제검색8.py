infinite_members = [ "김성규", "장동우", "남우현", "이성열", "엘", "이성종" ]
name = input("이름 >")
if name in infinite_members :
    idx = infinite_members.index(name)
    print("{}는 인피니트의 {}번째 멤버입니다.".format(name, idx))
else :
    print("{}는 인피니트의 멤버가 아닙니다.".format(name))
