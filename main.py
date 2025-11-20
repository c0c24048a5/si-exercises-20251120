def main():
items = [
{"name": "コーヒー", "amount": 300, "num": 2},
{"name": "本","amount": 500, "num": 1}
]
items = add_item(items)
def print_items(items):
print("|商品名|金額|商品数|")
print("|----|----|----|")
for item in items:
name = item["name"]
num = item["num"]
amount = item["amount"]
print(f"|{name}|{amount}|{num}|")
if __name__ == "__main__":
main()