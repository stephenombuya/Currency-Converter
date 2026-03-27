import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/"


def get_rates(base_currency):
    try:
        response = requests.get(f"{API_URL}{base_currency}", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def convert_currency(amount, from_currency, to_currency):
    data = get_rates(from_currency)

    if "error" in data:
        return f"❌ API Error: {data['error']}"

    rates = data.get("rates", {})

    if to_currency not in rates:
        return f"❌ Currency '{to_currency}' not found."

    converted_amount = amount * rates[to_currency]
    return f"✅ {amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}"


def list_currencies(base_currency="USD"):
    data = get_rates(base_currency)

    if "error" in data:
        print(f"❌ Error fetching currencies: {data['error']}")
        return

    print("\n🌍 Available currencies:")
    print("-" * 40)
    for currency in sorted(data["rates"].keys()):
        print(currency)


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("❌ Amount must be greater than 0.")
                continue
            return amount
        except ValueError:
            print("❌ Please enter a valid number.")


def get_currency_input(prompt):
    while True:
        currency = input(prompt).upper().strip()
        if len(currency) == 3 and currency.isalpha():
            return currency
        print("❌ Invalid currency code (e.g., USD, EUR, KES).")


def menu():
    while True:
        print("\n💱 Currency Converter")
        print("-" * 40)
        print("1. Convert Currency")
        print("2. List Available Currencies")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            amount = get_valid_amount()
            from_currency = get_currency_input("From currency (e.g., USD): ")
            to_currency = get_currency_input("To currency (e.g., KES): ")

            result = convert_currency(amount, from_currency, to_currency)
            print(result)

        elif choice == "2":
            base = get_currency_input("Enter base currency (default USD): ") or "USD"
            list_currencies(base)

        elif choice == "3":
            print("👋 Exiting... Stay sharp!")
            break

        else:
            print("❌ Invalid choice. Try again.")


def main():
    print("🚀 Welcome to the PRO Currency Converter")
    menu()


if __name__ == "__main__":
    main()
