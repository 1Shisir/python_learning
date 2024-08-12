#WAP to create a dictionary containing the 10 countries with their currency.Ask the user to country and print the data 
# Give user the choice to exit the program and ask if wants to continue or not

# countries = []
# def get_data():
#     for i in range(3):
#         country = input("Enter the country:")
#         currency = input("Enter the currency:")
#         countries.append({
#             'country': country,
#             'currency': currency
#         })

# get_data()
# choice =''
# while(choice == 'y'):
#     kasko_data = input("Enter the country:")
#     for country in countries:
#         if(country['country'] == kasko_data):
#             print(f"Currency of {kasko_data} is {country['currency']}")
#             break
#     choice = input("Do you want to continue(y/n):")    

countries = {}
def get_data():
    for i in range(3):
        country = input("Enter the country:")
        currency = input("Enter the currency:")
        countries[country] = currency
    return

get_data()
sodha = input("Enter the country:")
print(f"Currency of {sodha} is {countries[sodha]}")
print(countries)