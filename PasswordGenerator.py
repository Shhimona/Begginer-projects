import random
import string

def generate_password(lenght=9):
    alphabet= string.ascii_letters + string.digits
    password = "".join(random.choice(alphabet) for i in range(lenght))
    return password

password = generate_password()
print(f"This is your password:{password}")

def check_password_strenght(password):
    score=0
    feedback=[]

    if len(password)>=8:
       score=score+1
    else:
       feedback.append("Password must have at least 8 characters")

    return score,feedback