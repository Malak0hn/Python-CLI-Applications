def main():
    inventory = {}
    req = ["Log", "Sum Up", "Quit"]
    while True:
        for request in req:
            print(request)
        try:
            ur_req = input("Enter your request: ").strip().title()
            if ur_req not in req:
                print("wrong answer try again later...")
                continue
            if ur_req == "Quit":
                return
            
            elif ur_req == "Log":
                log_cat = input("Enter your category: ").strip().title()
                amount = int(input("Enter its amount: "))
                if log_cat not in inventory:
                    inventory[log_cat] = []
                inventory[log_cat].append(amount)

            elif ur_req == "Sum Up":
                if not inventory:
                    print("Inventory is empty! Please log an item first.")
                    continue
                total = sum(sum(amount) for amount in inventory.values())
                high = max(sum(amount) for amount in inventory.values())
                low = min(sum(amount) for amount in inventory.values())
                summary(inventory, total, high, low)

        except ValueError:
            print("Enter a vaild answer!")
            continue 

def summary(inv, total, high, low):
    print(f"""
Inventory Report:
Your total: {total}
The Highest Value: {high}
The Lowest Value: {low}
\n Categories Details
""")
    for category in inv:
        spent = sum(inv.get(category,[0]))
        print(f"""Category: {category}
Amount Spent: {spent}\n""")   



if __name__ == "__main__":
    main()                 