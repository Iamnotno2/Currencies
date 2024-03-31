from tabulate import tabulate
import csv
import requests

def main():
    print("This is a small currency program, it will give you live currency rates along with the capablity of currency conversion")
    print()
    while True:
        print(start_prompt())
        user_option = input("Select one of the Options(1,2,3): ").strip()
        option_selected = option(user_option)
        if option_selected == 1:
            print(get_country_currency())
        if option_selected == 2:
            # Ask user, if the user wants to check the currencies list first
            user_input = input("Would you like to see the supported currencies list first (Yes/No) ").strip().upper()
            if user_input == "YES":
                print(get_country_currency())
            while True:
                try:
                    print(get_currency_rate(input("Input Currency: ").strip().upper()))
                    break
                except KeyError:
                    print("Invalid Currency - Try Again")
                    pass
        if option_selected == 3:
            result_value = currency_converter()
            print()
            print(result_value)
        print()
        if program_continue(input("Would you like to see the Options menu again? (Yes/No) ").upper().strip()):
            print()
            pass
        else:
            break

def start_prompt():
    start_prompt = []
    with open("start_prompt.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            start_prompt.append({"Ser": row["Ser"], "Option": row["Option"], "Description": row["Description"]})
    return (tabulate(start_prompt, headers="keys", tablefmt="pretty"))

def option(n):
    while True:
        try:
            if n in ["1", "2", "3"]:
                return int(n)
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid Option - Try Again")
            n = input("Select one of the Options(1,2,3): ").strip()
            pass


def get_country_currency():
    currencies = []
    with open("currencies.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            currencies.append({"Country": row["Country"], "Currency": row["Currency"]})
    return (tabulate(currencies, headers="keys", tablefmt="pretty"))


def get_currency_rate(n):
    #Live currency rates, courtesy "https://www.exchangerate-api.com"Rates By Exchange Rate API
    response = requests.get("https://open.er-api.com/v6/latest/USD")
    o = response.json()
    return o["rates"][n]


def currency_converter():
    print()
    instructions = [
    {"Key": "Input as such ", "Description": ""},
    {"Key": "Input First Currency: ", "Description": "USD"},
    {"Key": "Input First Currency Value: ", "Description": "25"},
    {"Key": "Input Second Currency:  ", "Description": "PKR"}
    ]
    print (tabulate(instructions, headers="firstrow", tablefmt="pretty"))
    print()
    currencies = []
    with open("currencies.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            currencies.append(row["Currency"])
    while True:
        first_currency = input("Input First Currency: ").strip().upper()
        if first_currency in currencies:
            break
        else:
            print("Invalid Currency - Try Again")
            pass
    while True:
        try:
            first_currency_value = float(input("Input First Currency Value: "))
            break
        except ValueError:
            print("Invalid Value - Try Again")
            pass
    while True:
        second_currency = input("Input Second Currency: ").strip().upper()
        if second_currency in currencies:
            break
        else:
            print("Invalid Currency - Try Again")
            pass
    amount = (get_currency_rate("USD")/get_currency_rate(first_currency)) * first_currency_value * get_currency_rate(second_currency)
    return f"{first_currency_value} {first_currency} to {second_currency} = {amount:.2f} {second_currency}"

def program_continue(n):
        if n == "YES":
            return True
        else:
            return False



if __name__ == "__main__":
    main()
