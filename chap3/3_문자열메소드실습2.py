beginagain = [
    "I thought I saw you out there crying",
    "I thought I heard you call my name",
    "I thought I heard you out there crying"
    ]

for i in beginagain:
    if i.startswith("I") and i.endswith("ing"):
        print(i)
    else:
        print("")
