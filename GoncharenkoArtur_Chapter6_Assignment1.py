# A program that validates each piece of information using regular expressions and then outputs whether they are valid or not. 


import re

# Function to validate a phone number with one of the two formats.
def validate_phone_number(phone):
    pattern = r"^(\(\d{3}\)\s?|\d{3}-)\d{3}-\d{4}$"
    return bool(re.match(pattern, phone))

# Function to validate a social security number.
def validate_ssn(ssn):
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    return bool(re.match(pattern, ssn))

# Function to validate a zip code with one of two formats.
def validate_zip_code(zip_code):
    pattern = r"^\d{5}(-\d{4})?$"
    return bool(re.match(pattern, zip_code))

# The main function.
def main():
    # User inputs phone number, SSN, and zip code.
    phone = input("Enter a phone number ((XXX) XXX-XXXX or XXX-XXX-XXXX): ")
    ssn = input("Enter a social security number (XXX-XX-XXXX): ")
    zip_code = input("Enter a zip code (XXXXX or XXXXX-XXXX): ")

    # Validate what the user inputted.
    phone_valid = validate_phone_number(phone)
    ssn_valid = validate_ssn(ssn)
    zip_valid = validate_zip_code(zip_code)

    # Prints out results.
    print("\nValidation Results:")
    print(f"Phone Number Valid: {'Yes' if phone_valid else 'No'}")
    print(f"SSN Valid: {'Yes' if ssn_valid else 'No'}")
    print(f"Zip Code Valid: {'Yes' if zip_valid else 'No'}")


if __name__ == "__main__":
    main()
