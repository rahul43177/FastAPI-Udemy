# Dictionary
# A dictionary is an unordered collection of key-value pairs.

# Creating a Dictionary
user_dictionary = {
    'username': "rahul4317",  # Key: 'username', Value: "rahul4317"
    "name": "Rahul",  # Key: "name", Value: "Rahul"
    "Age": 23  # Key: "Age", Value: 23
}

print(user_dictionary)  # Output: {'username': 'rahul4317', 'name': 'Rahul', 'Age': 23}

# Getting Values
userName = user_dictionary.get("username")  # Getting the value of the key "username"
name = user_dictionary.get("name")  # Getting the value of the key "name"
age = user_dictionary.get("Age")  # Getting the value of the key "Age"

print(userName, name, age)  # Output: rahul4317 Rahul 23

# Adding a New Key-Value Pair
user_dictionary["country"] = "India"  # Adding a new key-value pair
userCountry = user_dictionary.get("country")  # Getting the value of the key "country"
print(userCountry)  # Output: India

# Length of the Dictionary
print(len(user_dictionary))  # Output: 4

# Looping Through the Dictionary
print("---------------------------")
for x, y in user_dictionary.items():  # Looping through the dictionary
    print(x, y)  # Output: username rahul4317, name Rahul, Age 23, country India

# Removing a Key-Value Pair
user_dictionary.pop("Age")  # Removing the key-value pair with key "Age"
print(user_dictionary)  # Output: {'username': 'rahul4317', 'name': 'Rahul', 'country': 'India'}

# Additional Methods
# keys(): Returns a view object that displays a list of all the available keys in the dictionary.
print(user_dictionary.keys())  # Output: dict_keys(['username', 'name', 'country'])

# values(): Returns a view object that displays a list of all the values in the dictionary.
print(user_dictionary.values())  # Output: dict_values(['rahul4317', 'Rahul', 'India'])

# update(): Updates the dictionary with the key-value pairs from another dictionary or an iterable of key-value pairs.
new_dict = {"city": "Delhi"}
user_dictionary.update(new_dict)  # Updating the dictionary
print(user_dictionary)  # Output: {'username': 'rahul4317', 'name': 'Rahul', 'country': 'India', 'city': 'Delhi'}

# clear(): Removes all the items from the dictionary.
user_dictionary.clear()  # Clearing the dictionary
print(user_dictionary)  # Output: {}

# copy(): Returns a shallow copy of the dictionary.
copy_dict = user_dictionary.copy()  # Creating a copy of the dictionary
print(copy_dict)  # Output: {}

# fromkeys(): Creates a new dictionary with specified keys and values.
new_dict = dict.fromkeys(["a", "b", "c"], 0)  # Creating a new dictionary
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# Best Practices
# Use meaningful and consistent key names.
# Avoid using mutable objects as keys (e.g., lists, dictionaries).
# Use the get() method to avoid KeyError exceptions when accessing values.
# Use the in operator to check if a key exists in the dictionary.

# Common Use Cases
# Configuration files: Dictionaries can be used to store configuration settings, such as user preferences or application settings.
# Data storage: Dictionaries can be used to store data in a structured format, such as a database or a data warehouse.
# Cache: Dictionaries can be used as a cache to store frequently accessed data.

# Additional Tips
# Dictionaries are mutable, meaning they can be modified after creation.
# Dictionaries are unordered, meaning the order of the key-value pairs is not guaranteed.
# Dictionaries can be nested, meaning a dictionary can contain another dictionary as a value.