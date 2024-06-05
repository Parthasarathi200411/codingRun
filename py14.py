from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    try:
        birthdate = datetime.strptime(birthdate, '%m/%d/%Y')
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    except ValueError:
        return None

def main():
    while True:
        dob = input("Please enter your date of birth (mm/dd/yyyy): ")
        age = calculate_age(dob)
        if age is not None:
            print("Your age is:", age, "years")
            break
        else:
            print("Invalid date format. Please try again.")

if __name__ == "__main__":
    main()