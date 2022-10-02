from colorama import Fore
import data_service as dts
import state
import mongo_setup



def main():
    mongo_setup.global_init()
    print_header()
    run()


def run():
    while True:
        try:
            login_or_register()
            get_action()
            show_commands()
            get_action()
        except KeyboardInterrupt:
            return


def login_or_register():
    print("what would you like to do?")
    print('[C]reate an account')
    print('[L]ogin to your account\n')
    user_ans = input().upper()
    if user_ans == 'C':
        create_account()
    elif user_ans == 'L':
        log_into_account()
    else:
        dts.error_msg('please answer with C or L')
        exit_app()


def show_commands():
    print("what would you like to do?")
    print('[S]how optional meals in this city')
    print('e[X]it the app\n')
    option = input().upper()
    if option == 'S':
        dts.find_a_meal()
    elif option == 'X' or 'EXIT' or 'QUIT':
        exit_app()
    else:
        dts.error_msg('please chose a valid option')






def get_action():
    text = '> '
    if state.active_account:
        text = f'{state.active_account.name}> '

    action = input(Fore.YELLOW + text + Fore.WHITE)
    return action.strip().lower()


def create_account():
    print('****************REGISTER****************')
    name = input("Whats your name? ").lower().capitalize()
    email = input("Wats your e-mail address? ")
    dts.validate(email)
    # checking if account exist
    old_account = dts.find_account_by_email(email)
    if old_account:  # is True
        dts.error_msg(f'account with email {email} already exists!')
        raise Exception
    country = input("What country are you from? ").lower().capitalize()
    city = input("What city are you from? ").strip().lower().capitalize()
    is_vegan = True if input("Are you a vegan? y/n ").lower() == "y" else False
    is_vegetarian = True if input("Are you a vegetarian? y/n ").lower() == "y" else False
    is_kosher = True if input("Do you eat only kosher food? y/n ").lower() == "y" else False
    is_halal = True if input("Do you eat only halal food? y/n ").lower() == "y" else False
    hobbies = input("add some hobbies you have (do not press the Enter key) ")
    can_you_host = True if input("Can you host at your home? y/n ").lower() == "y" else False
    state.active_account = dts.create_account(name, email, country, city, is_vegan, is_vegetarian, is_kosher, is_halal,
                                              hobbies, can_you_host)
    dts.success_msg(f'account was created for {name}')


def log_into_account():
    print('****************LOGIN****************')
    email = input("Whats your email address? ")
    account = dts.find_account_by_email(email)
    if not account:
        dts.error_msg(f'Could not find account with email {email}.')
        return
    state.active_account = account
    dts.success_msg('Logged in successfully!')


def exit_app():
    print()
    print('Goodbye!')
    raise KeyboardInterrupt()


def print_header():
    header = \
        """
          __  __         _                  _   ___      _   
 |  \/  |___ ___| |_   __ _ _ _  __| | | __|__ _| |_ 
 | |\/| / -_) -_)  _| / _` | ' \/ _` | | _|/ _` |  _|
 |_|  |_\___\___|\__| \__,_|_||_\__,_| |___\__,_|\__|

         (  )   (   )  )
      ) (   )  (  (
      ( )  (    ) )
      _____________
     <_____________> ___
     |             |/ _ 
     |               | | |
     |               |_| |
  ___|             |\___/  
 /    \___________/    
 \_____________________/

By Asher-Epstein-42

Welcome to MEET & EAT, a platform to meet new people and to have a nice meal today!
M&E finds people around you with the same preference in food (vegan,kosher,halal, etc..).
you can host them for dinner or find someone around you that would be happy to hot you for dinner!
    """
    print(header)


if __name__ == '__main__':
    main()
