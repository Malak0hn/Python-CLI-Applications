def main():    
    options = ["Add", "View", "Set", "Exit"]
    budget = {}
    expense = {}
    #to compare the two dicts for the summary
    target_limit = None
    savings = None
    comments = ["This's what called financially free, man!", "USER SURVIVED!", "See you in the jail, buddy..."]
    name = input("Enter username: ").strip().title()
    #for summary
    first_turn = True
    while True:
        print("""1. Add expense
2. View expenses
3. Set budget
4. Exit""")
    #Set will be in the main
        try:
            req = input("Enter your request: ").title().strip()
            if req not in options:
                print("Request non-founded, Please try again.")
                continue
            if req == "Exit":
                return
            
            elif req == "Set":
                if first_turn:
                    target_limit = int(input("Enter your total limit: "))
                    first_turn = False
                setting(target_limit, budget)    
            elif req == "Add":
                key = input("Enter category (e.g., Food): ").strip().title()
                val = int(input("Enter amount: "))
                add(expense, key, val)

            else:
                #need the actual limit and find the largest/smallest expense
                if not expense or target_limit is None:
                    print("Please add at least one expense limit and set a budget first!")
                    continue
                total = sum(sum(amount) for amount in expense.values())
                high = max(sum(amount) for amount in expense.values())
                low =  min(sum(amount) for amount in expense.values())
                summary(name, target_limit, total, high, low, comments, budget, expense)
        except ValueError:
            print("Please enter a vaild value.")
            continue

def setting(target_limit, budget): 
    category = input("Enter category (e.g., Food): ").strip().title()
    amount = int(input("Enter amount: "))

    if category not in budget:
        budget[category] = []
    budget[category].append(amount)

    calculation = sum(sum(amount) for amount in budget.values()) 

    if calculation > target_limit:
        print("Your category budgets exceed your total limit, try again.")
        return
          
    return calculation

def add(expense, k, v):
    if k not in expense:
        expense[k] = []
    expense[k].append(v)

def summary(n, limit, total, high, low, comnt, budget, expense):
    #total_budgeted = sum(sum(amt) for amt in budget.values())
    savings = limit - total
    #compare first
    if limit > total:
        result = comnt[0]
    elif limit == total:
            result = comnt[1]
    else:
        result = comnt[2]  

    print(f"""\n{n}'s Summary:
Target limit: {limit}
Your total expenses: {total}
\n--- Category Breakdown ---""")
    all_cat = set(budget.keys()) | set(expense.keys())
    for category in all_cat:
        cat_budget = sum(budget.get(category, [0]))
        cat_spent = sum(expense.get(category, [0]))
        print(f"{category}: Spent ${cat_spent} / Allocated ${cat_budget}\n")

    print(f"""The highest expense: {high}
    The lowest expense: {low}
    Savings: {savings}
    {result}\n""")



if __name__ == "__main__":
    main()