def main():
    name = input("What's your name? ")
    grades = []
    while True:
        g = input("Enter your grades: ").strip()
        if g == "":
            break

        try:
            grades.append(int(g))
        except ValueError:
            print("Please enter a valid whole number.")

    if not grades:
        print("No grades were entered.")
        return
    
    max_score = max(grades)
    min_score = min(grades)        
    average =  sum(grades) / len(grades)
    analyize = {
    "A": "GOAT. (said loud and clear!)",
    "B": "Humm...I see you.",
    "C": "...Not Bad.",
    "D": "Nice Try, I hope it'll be the last.",
    "F": "What the heck, man."
}
    if average > 80:
        con = analyize["A"]
        grade = list(analyize)[0]
    elif 80 >= average > 70:
        con = analyize["B"]
        grade = list(analyize)[1]
    elif 70 >= average > 60:
        con = analyize["C"]
        grade = list(analyize)[2]
    elif 60 >= average > 50:
        con = analyize["D"]
        grade = list(analyize)[3]
    else:
         con = analyize["F"]
         grade = list(analyize)[4]

    summary(name, average, max_score, min_score, grade, con)


def summary(n, avg, max_val, min_val, letter, note):
    print(f"""{n}'s Summary:
Average: {avg:.2f} ({letter})
Highest Score: {max_val}
Lowest Score: {min_val}
Conclusion: {note}""")

if __name__ == "__main__":
    main()


#(Note: max() and min() raise a ValueError on empty lists, which is why both errors are caught above).
#Inside def summary(...): Choose names that make sense inside that function, regardless of what main() named them.
#because it works by position
#Try to make the keys of dict easy to call.

