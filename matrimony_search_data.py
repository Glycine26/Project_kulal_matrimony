def user_data_search():
    import json
    from pprint import pprint

    with open(r'matrimony_data.json', 'r') as file:
        profile_data = json.load(file)

    def get_user_name(user_name):
        # user_name = input("Enter your name: ")
        while True:
            name_list = [num for num in user_name if num.isdigit()]
            if len(name_list) > 0:
                print("User name can't be number")
                break
            elif len(user_name) == 0:
                print("Name field can't be empty")
                break
            else:
                return user_name.capitalize()
        # print("validation failed")
        return get_user_name(user_name)

    # user contact number function
    def get_user_number(number):
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
    def get_user_gender(gender):
        cap_gender = gender.capitalize()
        if cap_gender == "Male" or cap_gender == "Female":
            return cap_gender
        else:
            return get_user_gender(input("Enter the valid gender(Male/Female): "))
    def search_for_key():
        available_keys = {0 :"user_name", 1:"user_contact", 2:"user_gender", 3:"email_id", 4:"birth_date", 5:"user_location", 6:"user_job", 7:"user_education", 8:"user_height", 9:"user_nakshatra", 10:"user_rashi", 11:"bhari_father", 12:"bhari_mother", 13:"user_family_info", 14:"user_active", 15:"mute_reason"}
        print("The available keys are: ")
        for key,value in available_keys.items():
            print(f"{key} : {value}")

        input_keys = input("Enter the keys you are looking to search (comma-separated): ")
        input_keys = [int(key.strip()) for key in input_keys.split(',')]

        selected_keys = [available_keys.get(key) for key in input_keys]
        selected_keys = [key for key in selected_keys ]
        # key_list = list(selected_keys)
        # selected_keys = [key.strip() for key in selected_keys]
        matching_profiles = []
        for profile in profile_data:
            if all(key in profile for key in selected_keys):
                matching_profiles.append(profile)
        if len(matching_profiles) > 0:
            print("Keys are matching, Now enter the value")
        else:
            print("No profile with the matching keys found")
            return search_for_key()
        return selected_keys, matching_profiles

    def search_for_value(search_keys,profiles):
        input_values = {}
        for key in search_keys:
            value = input(f"Enter the value for key '{key}': ")
            input_values[key] = value
        # print(input_values)
        filtered_profile = []
        for profile in profiles:
            if all(profile.get(key) == value for key,value in input_values.items()):
                filtered_profile.append(profile)
                # return filtered_profile
        if len(filtered_profile) == 0:
            print("No profiles match the specified criteria.\n")
        # return user_data_search()
        pprint(filtered_profile,sort_dicts=False)
        print("\n")
        return "Done,Thank you"

    def edit_data():
        name = get_user_name(input("Enter your name: "))
        contact_number = get_user_number(input("Enter your contact number: "))
        gender = get_user_gender(input("Enter your gender: "))

        for search_data in profile_data:
            if search_data.get("user_name") == name and search_data.get("user_contact") == contact_number and search_data.get("user_gender") == gender:
                print("Here is your profie:\n")
                pprint(search_data,indent=1,sort_dicts=False)
                
                print("\n")
                available_keys = {0: "user_name", 1: "user_contact", 2: "user_gender", 3: "email_id", 4: "birth_date",
                                  5: "user_location", 6: "user_job", 7: "user_education", 8: "user_height",
                                  9: "user_nakshatra", 10: "user_rashi", 11: "bhari_father", 12: "bhari_mother",
                                  13: "user_family_info", 14: "user_active", 15: "mute_reason"}
                print("The available keys, to edit are: \n")
                for key,value in available_keys.items():
                    print(f"{key} : {value}")
                    
                input_key = input("\nEnter the keys of the data(comma-separated): ")
                input_key = [int(key.strip()) for key in input_key.split(',')]
                selcected_key = [available_keys.get(key) for key in input_key]
                
                for key in selcected_key:
                    changed_value = input(f"Enter the data for {key}: ")
                    search_data[key] = changed_value
                
                print("Your data changes successfully added")
        
        with open('matrimony_data.json','w') as file:
            json.dump(profile_data,file,indent=2)


    print("\n")
    admin_menu = input("To search for profile with key & value press: 1\n"
                       "To edit the data press: 2\n")
    admin_menu = int(admin_menu)
    if admin_menu == 1:
        # return_search_data = search_for_key()
        keys, matching_profiles = search_for_key()
        filtered_data = search_for_value(keys, matching_profiles)
        # for items in filtered_data:
        pprint(filtered_data)
    elif admin_menu == 2:
        return_data_edit = edit_data()
        return return_data_edit
    else:
        print("The input is out of order, Please select the right one\n")
        # return matrimony_admin()
