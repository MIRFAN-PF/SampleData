# import json
# import os
# from faker import Faker
# import random

# # Load a list of Islamic names
# islamic_names = [
#     "Mohammed",
#     "Fatima",
#     "Ali",
#     "Aisha",
#     "Omar",
#     "Khadijah",
#     # Add more Islamic names as needed
# ]

# fake = Faker()

# def is_islamic_country(country):
#     # Define a list of Islamic countries (customize as needed)
#     islamic_countries = ["Saudi Arabia", "Pakistan", "Iran", "Egypt", "Indonesia", "Turkey"]

#     return country in islamic_countries

# def generate_fake_person_data(country, state, city, num_records):
#     person_data = {
#         "localisation": {
#             "country": country,
#             "country_code": fake.country_code(),
#         },
#         "data": [],
#     }

#     for _ in range(num_records):
#         if is_islamic_country(country):
#             name = random.choice(islamic_names)
#         else:
#             name = fake.name()
        
#         # Use provided state and city if available, otherwise generate random values
#         if state and city:
#             address = f"{fake.building_number()} {fake.street_address()}, {city}, {state}, {country}, {fake.zipcode()}"
#         else:
#             address = fake.address()
        
#         state_name = state if state else fake.state()
#         city_name = city if city else fake.city()
        
#         phone = fake.phone_number()
#         formatted_phone = f"+1-{phone[0:3]}-{phone[4:7]}-{phone[8:12]}"
        
#         person = {
#             "name": name,
#             "age": fake.random_int(min=18, max=80, step=1),
#             "dob": fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=80).strftime("%Y-%m-d"),
#             "address": address,
#             "state": state_name,
#             "city": city_name,
#             "zipcode": fake.zipcode(),
#             "email": fake.email(),
#             "phone": formatted_phone,
#             "ssn": fake.ssn(),
#         }

#         person_data["data"].append(person)

#     return person_data

# if __name__ == "__main__":
#     country = input("Enter the country: ")
#     state = input("Enter the state (or leave empty for random): ")
#     city = input("Enter the city (or leave empty for random): ")
#     num_records = int(input("Enter the number of records to generate: "))

#     person_data = generate_fake_person_data(country, state, city, num_records)

#     current_directory = os.path.dirname(os.path.realpath(__file__ if "__file__" in globals() else "."))
#     json_file_path = os.path.join(current_directory, "fake_person_data.json")

#     with open(json_file_path, "w") as json_file:
#         json.dump(person_data, json_file, indent=4)

#     print(f"Generated and saved {num_records} fake person records to '{json_file_path}'.")


from faker import Faker

# Create a Faker instance with the desired locale (Arabic)
fake = Faker('ar_JO')

# Generate and print Islamic boys' and girls' names
islamic_boys_name = fake.first_name_male()
islamic_girls_name = fake.first_name_female()

print("Islamic Boy's Name:", islamic_boys_name)
print("Islamic Girl's Name:", islamic_girls_name)