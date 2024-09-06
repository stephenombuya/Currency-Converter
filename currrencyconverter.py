import requests

# Define the function for currency conversion
def currency_converter():
    # Enter the amount to convert
    amount = int(input("Please enter amount to convert: "))

    # currency code of the amount to convert
    from_currency = input("Enter the currency code of the amount you are converting: ").upper()

    # currency code of the amount to convert to
    to_currency = input("Enter the currency code you are converting to: ").upper()

    # Make a request to a currency API
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'
    
    try:
        # Get the conversion rate 
        response = requests.get(url, verify=True)
        data = response.json()

        if to_currency in data['rates']:
            # Calculate the converted amount
            converted_amount = amount * data['rates'][to_currency]
            return f'\nThe amount is {converted_amount:.2f} and the currency is {to_currency}'
        else:
            return f'Currency {to_currency} not found!'
    
    except Exception as e:
        return f'Error occurred: {str(e)}'

# Call the function
print(currency_converter())