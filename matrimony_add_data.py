import json
import re
import datetime
from pprint import pprint

def data_load():
    with open(r'matrimony_data.json', 'r')as file:
        profile_sheet_in = json.load(file)
        return profile_sheet_in
    
#data upload to json file
def data_upload(profile_sheet_out):
    with open('matrimony_data.json', 'w') as file:
        json.dump(profile_sheet_out, file, indent=2) 

# user_name function
def get_user_name(user_name=None):
    if user_name is None:
        user_name = input("Enter your name: ")
        
    if any(char.isdigit() for char in user_name):
        print("User name can't contain numbers.")
        return get_user_name()
    elif len(user_name) == 0:
        print("User name can't be empty.")
        return get_user_name()
    else:
        user_name =' '.join(word.capitalize() for word in user_name.split())
        # print(user_name)
        return user_name
    
# user contact number function
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

# user gender function
def get_user_gender(gender=None):
    gender = input("Enter your gender:")
    cap_gender = gender.capitalize()
    gender_dict = {"M": "Male", "Male": "Male", "F": "Female", "Female": "Female"}
    if cap_gender not in gender_dict:
        return get_user_gender()
    else:
        return gender_dict[cap_gender]

#Verify user email
def get_user_mail_id(mail_id=None):
    mail_id = input("Enter your email Id: ")
    if re.fullmatch(r"[^@]+@[^@]+\.[^@]+", mail_id):
        return mail_id
    else:
        return get_user_mail_id()

#Verify user DOB format
def get_user_dob(DOB=None):
    DOB = input("Enter your date of Birth(dd/mm/yyyy): ")
    try:
        date_of_birth = datetime.datetime.strptime(DOB, "%d/%m/%Y")
        return date_of_birth.isoformat()
        # Convert datetime object to string
    except (ValueError, TypeError, SyntaxError):
        print("Please follow the format")
        return get_user_dob()

#Verify user location
def get_user_location(location=None):
    location = input("Your place: ")

    if len(location) == 0:
        return get_user_location()
    else:
        return location

#Verify user job
def get_user_job(job=None):
    job = input("Enter your Profession: ")
    if len(job) == 0:
        return get_user_job()
    elif job.isdigit():
        return get_user_job()
    else:
        return job

#Check for special chars in user_education
def check_special_character(character):
    special_characters = "!@#$%^&*()=+`~[]{}|;:'\"<>?/"
    for char in character:
        if char in special_characters:
            return True
    return False

#verify user education
def get_user_education(qualification=None):
    qualification = input("You highest qualification: ")
    
    if len(qualification) == 0:
        return get_user_education()
    elif qualification.isdigit():
        print("Digits not allowed, Please enter your highest qualification")
        return get_user_education()
    elif check_special_character(qualification):
        print("Special characters are not allowed.")
        return get_user_education()
    else:
        return qualification

#Verif
def get_user_height(height=None):

    height = input("Enter your height in feet,inches (e.g., 5,6): ")
    try:
        feet,inches = map(str.strip, height.split(','))
        feet = int(feet)
        if inches == '':
            inches = 0
            return feet
        else:
            inches = int(inches)
        
        #To check inches in range
        if not 0 <= inches < 12:
            print("Inches must be between 0 to 11")
            return get_user_height()
        else:
            return feet,inches
    except ValueError:
        print("Please enter a valid height in the format feet,inches (e.g., 5,6).")
        return get_user_height()
    except Exception as error:
        print(f"{error}")
        return get_user_height()

def get_user_nakshatra():
    my_nakshatra = input("Enter your Nakshatra: ")
    my_nakshatra = ' '.join(word.capitalize() for word in my_nakshatra.split())
    nakshatras = ["Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra", "Punarvasu", "Pushya",
                    "Ashlesha", "Magha", "Purva Phalguni",
                    "Uttara Phalguni", "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
                    "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
                    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"]
    # for nak in nakshatras:
    if not my_nakshatra in nakshatras:
        print(
            "You are allowed only to write name of the Nakshatras - Ashwini, Bharani, Krittika, Rohini, Mrigashira, Ardra, Punarvasu, Pushya, Ashlesha, Magha, Purva Phalguni, Uttara Phalguni, Hasta, Chitra, Swati, Vishakha, Anuradha, Jyeshtha, Mula, Purva Ashadha, Uttara Ashadha, Shravana, Dhanishta, Shatabhisha, Purva Bhadrapada, Uttara Bhadrapada, Revati ")
        return get_user_nakshatra()
    else:
        return my_nakshatra

def get_user_raashi():
    my_raashi = input("Enter your raashi: ")
    my_raashi = ' '.join(word.capitalize() for word in my_raashi.split())
    raashi = ["Mesh", "Vrishabha", "Mithuna", "Karkataka", "Simha", "Kanya", "Tula", "Vrishchika", "Dhanu",
                "Makara", "Kumbha", "Meena"]
    if not my_raashi in raashi:
        print(
            "You are only allowed to give valid raashi : Mesh, Vrishabha, Mithuna, Karkataka, Simha, Kanya, Tula, Vrishchika, Dhanu, Makara, Kumbha, Meena")
        return get_user_raashi()
    else:
        return my_raashi

def get_user_m_bari():
    mother_bari = input("Enter Father side Bari: ")
    mother_bari = mother_bari.capitalize()
    bari = ["Salyan", "Bangera", "Maran", "Uppiyan", "Banjan", "Aikyan", "karmaberan", "Anchan"]
    if mother_bari in bari:
        return mother_bari
    else:
        print(
            "You are allowed to give valid bari : Salyan, Bangera, Maran, Uppiyan, Banjan, Aikyan, karmaberan, Anchan")
        return get_user_m_bari()

def get_user_f_bari():
    father_bari = input("Enter Mother side Bari: ")
    father_bari = father_bari.capitalize()
    bari = ["Salyan", "Bangera", "Maran", "Uppiyan", "Banjan", "Aikyan", "karmaberan", "Anchan"]
    if father_bari in bari:
        return father_bari
    else:
        print(
            "You are allowed to give valid bari : Salyan, Bangera, Maran, Uppiyan, Banjan, Aikyan, karmaberan, Anchan")
        return get_user_f_bari()

def get_user_family_info():
    print("\n Enter your family details: ")
    family_info = {}
    family_info["no_of_brothers"] = input("Number of brothers: ")
    family_info["no_of_sisters"] = input("Number of sisters: ")
    family_info["married_brothers"] = input("Number of married brothers: ")
    family_info["married_sisters"] = input("Number of married sisters: ")
    family_info["father_name"] = input("Father's name: ")
    family_info["mother_name"] = input("Mother's name: ")
    family_info["father_occupation"] = input("Father's occupation: ")
    family_info["mother_occupation"] = input("Mother's occupation: ")
    return family_info

def get_meta_count():
    with open('matrimony_count_data.json', 'r') as count_sheet:
        count_profile = json.load(count_sheet)
    return count_profile.get('user_count',0)
#try exception if the with with open file deleted

def set_meta_count(count_value):
    with open('matrimony_count_data.json', 'w') as count_file:
        json.dump({'user_count' : count_value}, count_file)
    
def check_duplicate_data(name,contact,gender,profile_sheet_in):
    user_name_found = None
    ask_reason = None
    user_status = True
    for duplicate_data in profile_sheet_in:
        if duplicate_data.get("user_name") is None:
            continue
        
        if duplicate_data.get("user_name") == name:
            user_name_found = True
            # print(f"User name with {name} doesn't exist.")
            # return
        
        if duplicate_data.get("user_name") == name and duplicate_data.get(
                "user_contact") == contact and duplicate_data.get(
            "user_gender") == gender and duplicate_data.get("user_active") == True:

            take_input = input("You are already have account\n"
                               "Press 'Enter'\n")
            if len(take_input) < 1:
                pprint("Your profile setting up to find the match")
                exit()
    
    if not user_name_found:
        # print(f"User name {name} doesn't exist.")        
    # else:
        new_profile = {}
        new_profile["user_name"] = name
        new_profile["user_contact"] = contact
        new_profile["user_gender"] = gender
        email_id3 = get_user_mail_id()
        new_profile["email_id"] = email_id3

        # Load the current count
        user_count = get_meta_count()
        user_count += 1
        new_profile['user_id'] = user_count

        #Save the updated count
        set_meta_count(user_count)

        dob3 = get_user_dob()
        new_profile["birth_date"] = dob3

        location3 = get_user_location()
        new_profile["user_location"] = location3

        job3 = get_user_job()
        new_profile["user_job"] = job3

        education3 = get_user_education()
        new_profile["user_education"] = education3

        height3 = get_user_height()
        new_profile["user_height"] = height3

        nakshatra3 = get_user_nakshatra()
        new_profile["user_nakshatra"] = nakshatra3

        raashi2 = get_user_raashi()
        new_profile["user_rashi"] = raashi2

        bari_father2 = get_user_f_bari()
        new_profile["bhari_father"] = bari_father2

        bari_mother2 = get_user_m_bari()
        new_profile["bhari_mother"] = bari_mother2

        user_family_info2 = get_user_family_info()
        new_profile["user_family_info"] = user_family_info2

        new_profile["user_active"] = user_status
        new_profile["mute_reason"] = ask_reason

        profile_sheet_in.append(new_profile)
        print("Your Data added successfully")
        
    data_upload(profile_sheet_in)
# def data_upload(profile_sheet):
#     with open('matrimony_data.json', 'w') as file:
#         json.dump(profile_sheet, file, indent=2)  # project_matrimony

def user_data_add():
    #Load the current count
    user_count = get_meta_count()
    
    # Find the duplicate:
    name = get_user_name()
    contact_number = get_user_number()
    gender = get_user_gender()
    data_set_in = data_load()
    check_duplicate_data(name,contact_number,gender,data_set_in)
    # data_sheet = check_duplicate_data(name,contact_number,gender,data_set_in)
    # data_sheet_save = data_upload(data_sheet)
    # print(data_sheet)