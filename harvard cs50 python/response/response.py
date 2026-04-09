from validator_collection import validators, checkers, errors
email_add=input("what's you emailadress")
if checkers.is_email(email_add)==True :
    print("valid")
else:
    print("Invalid")

