import json
def load_data():
    try:
        with open("data.json","r")as file:
            return json.load(file)
        
    except FileNotFoundError:
        return {"income":0,"expenses":[]}
    
def save_data(data):
    with open("data.json","w") as file:
        json.dump(data,file,indent=4)


def add_income():
    amount=float(input("Enter today's Income: "))
    data=load_data()
    data["income"]+=amount
    save_data(data)
    print("\nIncome added successfully!")

def add_expense():
    date=input("\nEnter date : ")
    category=input("\nEnter Category(food, rent etc) : ")
    amount=float(input("\nEnter amount : "))
    data=load_data()
    data["expenses"].append({"date":date,"category":category,"amount":amount})
    save_data(data)
    print("Expense added successfully!")

def view_summary():
    data=load_data()
    total_expense=sum(i["amount"] for i in data["expenses"])
    balance=data["income"]-total_expense

    print("Expense Summary")
    for i in data["expenses"]:
        print(f"{i['date']} |{i['category']}  |Rs.{i['amount']}")  
        print("\n")

    print("\n Total Income :  Rs{}".format(data["income"]))
    print(f"\n Total expense:  Rs{total_expense}")
    print(f"\n Balance      :  Rs{balance}")


def main():
    print("started")
    while True:
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("See you again!")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
              