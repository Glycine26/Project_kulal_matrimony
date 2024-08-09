import json
from pprint import pprint
from datetime import datetime
# active_data = None

def load_data():
    with open(r'matrimony_data.json','r') as file:
        active_data = json.load(file)
    return active_data

def get_user_name(user_name):
    if any (char.isdigit() for char in user_name):
        print("User name can't contain numbers.")
        user_name = input("Please enter a valid user name: ")
    if len(user_name) == 0:
        print("User name can't be empty.")
        user_name = input("Please enter a valid user name: ")
    else:
        # return user_name.capitalize()
        return ' '.join(word.capitalize() for word in user_name.split())
    ask_input()

#check the user_number
def get_user_number(number):
    str_number = str(number)
    if not str_number.isdigit():
        return get_user_number(input("You entered non-digit character. Enter the valid number: "))
    elif len(str_number) < 10:
        return get_user_number(input("Number is less than 10 digits. Enter the valid number: "))
    elif len(str_number) > 10:
        return get_user_number(input("Number is more than 10 digits, Enter the valid number: "))
    else:
        return str_number

#if name matches passes the Star and Zodiac
def user_verification(u_name,active_data):
    for match_data in active_data:
        stored_name = match_data.get("user_name")
        if stored_name and match_data.get("user_name") == u_name:
            star = match_data.get("user_nakshatra")
            zodiac = match_data.get("user_rashi")
            return zodiac,star
    print("The user name is not present")
    return ask_input()

#pass the Male/Female database
def verify_gender(user_name,active_data_in):
    male_datas = []
    female_datas = []
    passing_data = []
    u_gender = None

    for gender_datas in active_data_in:
        if user_name == gender_datas.get("user_name"):
            u_gender = gender_datas.get("user_gender")
        genders = gender_datas.get("user_gender")
        if genders == "Male":
            male_datas.append(gender_datas)
        elif genders == "Female":
            female_datas.append(gender_datas)

    if u_gender == "Male":
        passing_data = female_datas
    else:
        passing_data = male_datas
    return passing_data

def get_astro_index(user_zodiac, user_star):
    zodiac_indices = {"Mesh": {
    "Ashwini": 0,
    "Bharani": 1,
    "Kritika": 2
    },
    "Vrishabha": {
    "Kritika": 3,
    "Rohini" : 4,
    "Mrigashira": 5
    },
    "Mithuna": {
    "Mrigashira": 6,
    "Ardra": 7,
    "Punarvasu": 8
    },
    "Karkataka": {
    "Punarvasu": 9,
    "Pushya": 10,
    "Ashlesha": 11
    },
    "Simha": {
    "Magha": 12,
    "Purva Phalguni": 13,
    "Uttara Phalguni": 14
    },
    "Kanya":{
    "Uttara Phalguni": 15,
    "Hasta": 16,
    "Chitra": 17
    },
    "Tula": {
    "Chitra": 18,
    "Swati": 19,
    "Vishakha": 20
    },
    "Vrishchika": {
    "Vishakha": 21,
    "Anuradha": 22,
    "Jyeshtha": 23
    },
    "Dhanu": {
    "Mula": 24,
    "Purva Ashadha": 25,
    "Uttara Ashadha": 26
    },
    "Makara": {
    "Uttara Ashadha": 27,
    "Shravana": 28,
    "Dhanishta": 29
    },
    "Kumbha": {
    "Dhanishta": 30,
    "Shatabhisha": 31,
    "Purva Bhadrapada": 32
    },
    "Meena": {
    "Purva Bhadrapada": 33,
    "Uttara Bhadrapada": 34,
    "Revati": 35
    }}

    if user_zodiac in zodiac_indices:
        zodiac_index = zodiac_indices[user_zodiac].get(user_star)
        if zodiac_index is not None:
            return zodiac_index


def get_profile(u_id,active_data_in):
    while True:
        if u_id.isdigit():
            u_id = int(u_id)
            for comp_data in active_data_in:
                if comp_data.get("user_active",False) and comp_data.get("user_id") == u_id:
                    print("\n")
                    pprint(comp_data,sort_dicts=False)
                    return
            else:
                u_id = input("Invalid ID. Enter again: ")
        else:
            u_id = input("Invalid ID. Enter again: ")

def calculate_age(passed_data):
    birth_date = passed_data.get("birth_date")
    if birth_date is None:
        return None
    today = datetime.now()
    birth_date_datetime = datetime.strptime(birth_date, "%Y-%m-%dT%H:%M:%S")
    age = today.year - birth_date_datetime.year - ((today.month, today.day) < (birth_date_datetime.month, birth_date_datetime.day))
    return age
        

def ask_input(active_data):
    name1 = get_user_name(input("Name of Groom/ Bride: "))
    # name_caps = ' '.join(word.capitalize() for word in name1.split())
    print(name1)
    n_zodiac,n_star = user_verification(name1,active_data)
    if n_star is not None and n_zodiac is not None:
        index_number_user1 = get_astro_index(n_zodiac, n_star)
        print(f"Index of Groom: {index_number_user1}")
    else:
        print("Groom nakshatra/Rashi data not found.")

    #Selecting the M/F data base, based on User nmae 
    datas = verify_gender(name1, active_data)
    user_details = []
    user_details_no_score = []

    #Link to compatibility table
    with open(r'score_card.json','r') as file:
        data_score = json.load(file)

    for user_data in datas:
        user_name = user_data.get("user_name")
        user_id = user_data.get("user_id")
        user_raashi = user_data.get("user_rashi")
        user_nak = user_data.get("user_nakshatra")
        user_age = calculate_age(user_data)
        u_zodiac,u_star = user_verification(user_name,active_data)
        # index_number = get_astro_index(u_zodiac, u_star)    
        try:
            index_number = get_astro_index(u_zodiac, u_star)
            if index_number is None or index_number_user1 is None:
                raise TypeError
            compatibility_score = data_score[index_number_user1][index_number]
            user_details.append([(user_name), (user_id), (user_raashi), (user_nak), (user_age), (compatibility_score)])
        except TypeError:
            user_details_no_score.append([(user_name), (user_id), (user_raashi), (user_nak), (user_age)])
    
    if user_details:
        print("Name", "ID", "RAASHI", "NAKSHATRA", "AGE", "SCORE")   
    for details in user_details:
        print(details)
    if user_details_no_score:
        print("Name", "ID", "RAASHI", "NAKSHATRA", "AGE")
    for details in user_details_no_score:
        print(details)

    get_id = (input("\n Enter the User_id for details: "))
    get_profile(get_id,active_data)

def find_compability_score():
    active_data = load_data()
    ask_input(active_data)