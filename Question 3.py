import datetime

def calculate_age(birthdate_str):
    day, month, year = birthdate_str.split('/')
    day = int(day)
    month = int(month)
    year = int(year)

    today = datetime.date.today()
    age = today.year - year
    if (today.month < month) or (today.month == month and today.day < day):
        age -= 1
    return age

def main():
    birthdate = "06/08/2000"
    age = calculate_age(birthdate)
    print(f"Your age is: {age}")

if __name__ == "__main__":
    main()