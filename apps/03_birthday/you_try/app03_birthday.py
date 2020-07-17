""" Birthday App """
import datetime

def print_header():
    """ Print header """
    print('--------------------------------')
    print('          BIRTHDAY APP')
    print('--------------------------------')
    print()


def get_birthdate():
    """ Get birthdate from user """
    num = input('What year were you born [YYYY]? ')
    year = int(num)

    num = input('What month were you born [MM]? ')
    month = int(num)

    num = input('What day were you born [DD]? ')
    day = int(num)

    bday = datetime.date(year, month, day)
    print()
    print('It looks like you were born on {}'.format(bday.strftime('%d/%m/%Y')))

    return bday


def calculate_difference(now, birthdate):
    """ Calulate difference between 2 dates
        and return  the amount of days until next birthday """
    this_year = datetime.date(birthdate.year, now.month, now.day)
    delta = birthdate - this_year

    return delta.days


def print_birthday_information(num_of_days):
    """ Print birthday information """
    if num_of_days < 0:
        print('You had your birthday {} days ago'.format(abs(num_of_days)))
        print('Hope you enjoyed it!')
    elif num_of_days > 0:
        print('Looks like your birthday is in {} days.'.format(num_of_days))
        print('Hope you\'re looking forward to it!')
    else:
        print('Happy Birthday!')


def main():
    """ Main method to run program """
    print_header()
    birthdate = get_birthdate()
    current_date = datetime.date.today()
    num_of_days = calculate_difference(current_date, birthdate)
    print_birthday_information(num_of_days)


main()
