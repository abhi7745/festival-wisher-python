# pip install holidays
import holidays
from datetime import date, datetime

print(date.today())

for day, fest_name in sorted(holidays.India(years=date.today().year, state='KL').items()):
    print(day, fest_name)
    # print(type(day))

    # if datetime.strptime('2022-12-25', '%Y-%m-%d').date() == day:
    if date.today() == day:
        # print('Trueee')
        if fest_name == 'Republic Day':
            print('Republic Day')

        elif fest_name == 'Holi':
            print('Holi')

        elif fest_name == 'Independence Day':
            print('Independence Day')

        elif fest_name == 'Gandhi Jayanti':
            print('Gandhi Jayanti')

        elif fest_name == 'Diwali':
            print('Diwali')

        elif fest_name == 'Christmas':
            print('Christmas')



# india_holidays = holidays.India(years=2022, state='KL')
# # print(india_holidays)

# print('01-01-2022' in india_holidays)


def email_sender(fest_name, receiver_email):
    pass