import random
def main():
    orginal_num = random.randint(1,10)
    attempt = 0
    while True:
        try:
            num = int(input("Guess the number: "))
            attempt +=1 
            if num == orginal_num:
                print(f"Correct!, your attempts: {attempt}")
                break
            elif num > orginal_num + 2:
                print("too high, try again.")
            elif num > orginal_num:
                print("high, try again.")
            elif num < orginal_num - 2:
                print("too low, try again.")
            else:
                print("low, try again.")
        except ValueError:
            print("Please Enter A Vaild Number!")
            

if __name__ == "__main__":
    main()

#Remove redundant pass: pass is a placeholder for empty code blocks. Since your except block already contains a print() statement, pass is unnecessary.