from pprint import pprint
import json
import sys
from datetime import datetime

def load_data():
    with open('matrimony_data.json', 'r') as file:
        profile_sheet = json.load(file)
    return profile_sheet

def get_user_name(user_name=None):
    if user_name is None:
        user_name = input("Enter your name: ")        
    if len(user_name) == 0:
        print("User name can't be empty.")
        get_user_name()
    user_name =' '.join(word.capitalize() for word in user_name.split())
    # print(user_name)
    return user_name

def get_user_number(number=None):
    if number is None:
        number = input("Enter your contact number: ")
        
    str_number = str(number)
    if not str_number.isdigit():
        return get_user_number(input("Non-digit characters found. Please enter a valid number: "))
    elif len(str_number) < 10:
        return get_user_number(input("Number is less than 10 digits. Please enter a valid number: "))
    elif len(str_number) > 10:
        return get_user_number(input("Number is greater than 10 digits. Please enter a valid number: "))
    else:
        return str_number
 
def user_verification(u_name, u_contact, profile_sheet_in):
    user_gender = None
    for user_data in profile_sheet_in:
        if user_data.get("user_name") == u_name and user_data.get("user_contact") == u_contact and user_data.get("user_active") == True:
            user_gender = user_data.get("user_gender")
            print("Here is your profile:\n")
            pprint(user_data, indent=1, sort_dicts=False)   
    return user_gender
    
def gender_data_list(gender,profile_sheet_in):
    data_set_male = []
    data_set_female = [] 
    for all_data in profile_sheet_in:
        if all_data.get("user_gender") == "Male":
            data_set_male.append(all_data)
        elif all_data.get("user_gender") == "Female":
            data_set_female.append(all_data)

    if gender == "Male":
        return data_set_female

    elif gender == "Female":
        return data_set_male
#INPUT
def ask_user_input(data_sheet):
    name = get_user_name()
    contact_number = get_user_number()
    data_verify_return_gender = user_verification(name,contact_number,data_sheet)
    if not data_verify_return_gender:
        print(f"User with name {name} doesnot exist")
        return
    data_set = gender_data_list(data_verify_return_gender,data_sheet)
    return data_set

def key_value_match(data_set):
    print("\n")
    available_keys = {0: "user_name", 1: "user_contact", 2: "user_gender", 3: "email_id", 4: "birth_date",
                        5: "user_location", 6: "user_job", 7: "user_education", 8: "user_height",
                        9: "bhari_father", 10: "bhari_mother",11: "user_family_info"}
    print("The available keys are: \n")
    for key,value in available_keys.items():
        print(f"{key} : {value}")

    input_key = input("\nEnter the keys of the data(comma-separated): ")
    input_key = [int(key.strip()) for key in input_key.split(',')]
    selected_key = [available_keys.get(key) for key in input_key]
    # selected_key = [match_key for match_key in selected_key]

    input_key_value = {}
    matched_profiles = []
    for match_key in selected_key:
        value = input(f"Enter the value for key {[match_key]} : ")
        input_key_value[match_key] = value

    # data_set = ask_user_input()
    for profiles in data_set:
        
        if not profiles.get("user_active", False):
            continue
        if all(profiles.get(key) == value for key,value in input_key_value.items()):
            matched_profiles.append(profiles)

    if len(matched_profiles) == 0:
        print("No profiles match the specified criteria.\n")
        exit()
    print("here is the profile with matching Key_Value: ")
    matched_profile = pprint(matched_profiles,sort_dicts=False)
    return matched_profile

def astrology_value_match(data_set):
    available_raashi =  {0: 'Mesh', 1: 'Vrishabha', 2: 'Mithuna', 3: 'Karkataka', 4: 'Simha', 5: 'Kanya', 6: 'Tula', 7: 'Vrishchika', 
                        8: 'Dhanu', 9: 'Makara', 10: 'Kumbha', 11: 'Meena'}
    available_nakshatras = {0: 'Ashwini', 1: 'Bharani', 2: 'Krittika', 3: 'Rohini', 4: 'Mrigashira', 5: 'Ardra', 6: 'Punarvasu', 7: 'Pushya', 
                            8: 'Ashlesha', 9: 'Magha', 10: 'Purva Phalguni', 11: 'Uttara Phalguni', 12: 'Hasta', 13: 'Chitra', 14: 'Swati', 
                            15: 'Vishakha', 16: 'Anuradha', 17: 'Jyeshtha', 18: 'Mula', 19: 'Purva Ashadha', 20: 'Uttara Ashadha', 21: 'Shravana', 
                            22: 'Dhanishta', 23: 'Shatabhisha', 24: 'Purva Bhadrapada', 25: 'Uttara Bhadrapada', 26: 'Revati'}
    
    try:
        print("List of Raashis:\n")
        for index1,raashi in available_raashi.items():
            print(f"{index1} : {raashi}")
        input_raashi = input("Enter the key of raashi: ")
        input_raashi_key = int(input_raashi)
        if input_raashi_key not in available_raashi:
            print("Index not found")
            return astrology_value_match()
            
        selected_raashi = available_raashi.get(input_raashi_key)
        
        print("\n List of Nakshatras \n")
        for index2,naks in available_nakshatras.items():
            print(f"{index2} : {naks}")
        input_nakshatra = input("Enter the birth-star: ")
        input_naks_key = int(input_nakshatra)
        if input_naks_key not in available_nakshatras:
            print("Index not found")
            return astrology_value_match()
            
        selected_nakshatra = available_nakshatras.get(input_naks_key)

        # data_set = ask_user_input
        found = False
        for data_key in data_set:
            if not data_key.get("user_active", False):
                continue
            if data_key.get("user_nakshatra") == selected_nakshatra and data_key.get("user_rashi") == selected_raashi:
                print("\nHere is the profile with selected Nakshatra and Raashi: \n")
                pprint(data_key,sort_dicts=False)
                found = True
        if not found: 
            print("No data with selected raashi and Nakshatra found.")
    except ValueError:
        print("Invalid input. Please enter a valid integer index")
        return astrology_value_match()
                
        # print(collect_raashi_star)
def calculate_age(birth_date):
    if birth_date is None:
        return None
    today = datetime.now()
    birth_date = datetime.strptime(birth_date, "%Y-%m-%dT%H:%M:%S")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def quick_search(data_set):
    # data_set = ask_user_input()
    # print(data_set)
    for match_profile in data_set:
        birth_date = match_profile.get("birth_date")
        age = calculate_age(birth_date)
        match_profile["user_age"] = age

    print("\nEnter the age ranges\n")
    input_min_age = input("From: ")
    input_max_age = input("To: ")
    input_max_age = int(input_max_age)
    input_min_age = int(input_min_age)
    age_match_profiles = [profile for profile in data_set if
                            profile.get("user_age") is not None and input_min_age <= profile["user_age"] <= input_max_age and profile.get("user_active",False) ]

    # age_match_profiles = [profile for profile in profile_sheet if input_min_age <= profile["user_age"] <= input_max_age]

    for age_matched_profile in age_match_profiles:
        pprint(age_matched_profile,sort_dicts=False)

def match_options(data_set):
    print("\nThe Match options are:\n")
    while True:
        match_option = input("Keyword Search: 1\nAstrology Search: 2\nQuick Search: 3\n")
        if match_option.isdigit():
            match_option = int(match_option)
            if match_option == 1:
                selected_option = key_value_match(data_set)
                return selected_option

            # Astrology_search_match_find
            if match_option == 2:
                selected_option = astrology_value_match(data_set)
                return selected_option

            if match_option == 3:
                selected_option = quick_search(data_set)
                return selected_option

        else:
            print("Invalid input. Please enter a valid option (1, 2, or 3).")


def user_match_data():
    data_sets = load_data()
    gender_based_data_set = ask_user_input(data_sets)
    if not gender_based_data_set:
        return
    match_options(gender_based_data_set)
