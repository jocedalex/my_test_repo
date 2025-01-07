from datetime import date, datetime

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property    
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age

def check_adult(func):
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            raise Exception("User is not an adult.")
        return func(user, *args, **kwargs)
    return wrapper

@check_adult
def access_restricted_area(user):
    return "Access granted to restricted area."

# Example usage
user = User(datetime.strptime('2008-05-15', '%Y-%m-%d'))
try:
    print(access_restricted_area(user))
except Exception as e:
    print(e)

adult_user = User(datetime.strptime('1990-05-15', '%Y-%m-%d'))
try:
    print(access_restricted_area(adult_user))
except Exception as e:
    print(e)