from matrimony_add_data import user_data_add
from matrimony_search_data import user_data_search
from matrimony_match_data import user_match_data
from matrimony_compability_score import find_compability_score
from compability_class import compatibility

def get_matrimony_admin():
    try:
        print("Menu Bar:")
        menu_input = input(
        "To 'Add'/ 'check the account status' press: 1\nTo 'Edit'/'Delete' your data press: 2\nAdmin : 3\nTo compare the match with compatibility score for your data press: 4\n")
        # "To find the matching profile based on Astrology:5 \n")

        menu_input = int(menu_input)
        if menu_input == 1:
            return_add_data = user_data_add()
            return return_add_data
        elif menu_input == 2:
            return_search_data = user_data_search()
            return return_search_data
        elif menu_input == 3:
            return_match_data = user_match_data()
            return return_match_data
        elif menu_input == 4:
            return_suggested_data = find_compability_score()
            return return_suggested_data
        else:
            print("The input is out of order, Please select the right one\n")
            return get_matrimony_admin()
    except ValueError:
        print('there is a value error')
        get_matrimony_admin()

get_matrimony_admin()
compat_class = compatibility()
compat_class.find_compability_score()

#give the id to the profile