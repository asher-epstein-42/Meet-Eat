import re
from colorama import Fore

import state
from host import Host

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def create_account(name: str, email: str, country: str, city: str, is_vegan: bool, is_vegetarian: bool, is_kosher: bool,
                   is_halal: bool, hobbies: str, can_you_host: bool):  # -> Host
    host = Host()
    host.name = name
    host.email = email
    host.country = country
    host.city = city
    host.is_vegan = is_vegan
    host.is_vegetarian = is_vegetarian
    host.is_kosher = is_kosher
    host.is_halal = is_halal
    host.hobbies = hobbies
    host.can_you_host = can_you_host
    host.save()
    return host


def find_account_by_email(email: str):  # -> Host
    host_name = Host.objects(email=email).first()
    return host_name
def validate(email):
    # pass the regular expression
    # and the string into the fullmatch() method
    if not (re.fullmatch(email_regex, email)):
        error_msg(f'{email} is an invalid email')
        raise Exception


def find_a_meal():
    current_account = state.active_account
    print(f"here are some matches we found for you in {current_account.city}: \n")
    for host in Host.objects:
        if host.email != current_account.email and host.can_you_host == True and host.city == current_account.city and host.is_vegan == current_account.is_vegan and host.is_vegetarian == current_account.is_vegetarian and host.is_kosher == current_account.is_kosher and host.is_halal == current_account.is_halal:
            print(f"{host.name} is in your city.you can send him a message via {host.email}. you can talk to him about {host.hobbies}.")





def success_msg(text):
    print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)


def error_msg(text):
    print(Fore.LIGHTRED_EX + text + Fore.WHITE)
