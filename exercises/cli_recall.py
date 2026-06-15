
import json

with open("./cards.json", "r", encoding="utf-8") as f:
    cards=json.load(f)

correct=0
for card in cards:
    front=card["front"]
    back=card["back"]
    print(f"{front}")

    response = input("按回车看答案...")
    if response == "":
        print(f"{back}")
    rating = input("答对了吗？(y/n) ")
    if rating == 'y':
        correct = correct + 1
print(f"你答对了{correct}/{len(cards)}张")