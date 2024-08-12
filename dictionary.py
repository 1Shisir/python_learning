# a = {
#     'name': 'John',
#     'age': 25,
#     'address': 'Kathmandu'
# }

# print(type(a)) # returns dictionary
# print(a['name']) # returns John

# print(a.get('age')) # returns 25

#WAP to store the data of students containing name, age and address and display the data asked by the user .
#Give user  to enter the choice to exit the problem and ask if wants to continue or not

    
data = {
    'student1': {
        'name': 'John',
        'age': 25,
        'address': 'Kathmandu'
    },
    'student2': {
        'name': 'Ram',
        'age': 20,
        'address': 'Lalitpur'
    },
    'student3': {
        'name': 'Sita',
        'age': 22,
        'address': 'Bhaktapur'
    },
    'student4': {
        'name': 'Gita',
        'age': 23,
        'address': 'Kathmandu'
    }
}

def get_data():
    kati_choto_sodne = int(input("Enter the number of students:"))
    for i in range(kati_choto_sodne):
        name = input("Enter the name:")
        age = int(input("Enter the age:"))
        address = input("Enter the address:")
        data[f'student{i+1}'] = {
            'name': name,
            'age': age,
            'address': address
        }
    return
get_data() 
print(data)   
def display_data():
    ask = input("Kasko data:")
    print(f"Name: {data[ask]['name']}")
    print(f"Age:{data[ask]['age']}")
    print(f"Address:{data[ask]['address']}")
    return

display_data()
feriSodha = input("Do you want to continue:")
while(feriSodha == 'yes'):
    display_data()
    feriSodha = input("Do you want to continue:")    