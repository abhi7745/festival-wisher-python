from datetime import date, datetime

# print(date.today())

fest_name_data = {
                    'NewYear' : '2022-01-01', 
                    'RepublicDay' : '2022-01-26', 
                    'IndependenceDay' : '2020-08-15',   
                    'GandhiJayanti' : '2020-10-02',  
                    'Christmas' : '2022-12-25',
                }



for fest_name, day in fest_name_data.items():
    # print(fest_name, day)
    if date.today() == datetime.strptime(day, '%Y-%m-%d').date():
        # print('Trueee')
        if fest_name == 'NewYear':
            print('NewYear')

        elif fest_name == 'RepublicDay':
            print('RepublicDay')

        elif fest_name == 'IndependenceDay':
            print('IndependenceDay')

        elif fest_name == 'GandhiJayanti':
            print('GandhiJayanti')

        elif fest_name == 'Christmas':
            print('Christmas')



def email_sender(fest_name, receiver_email):
    pass
        
