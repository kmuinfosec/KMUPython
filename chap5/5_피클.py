# 피클
import pickle

# 피클링
f = open("myDic.dat", "wb")
pickle.dump({"waiver":"권리 포기, 면제", "tuition":"수업료", "insurance":"보험"}, f)
f.close()

# 언피클링
f = open("myDic.dat", "rb")
dic = pickle.load(f)
print(dic)
f.close()