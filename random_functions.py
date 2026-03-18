def age_from_rut(
        rut #Chilena RUT in format 120034-3
        ):
    from datetime import datetime
    today_date = datetime.today()
    slope = 3.3363697569700348e-06
    intercept = 1932.2573852507373
    rut=int(rut.slit("-")[0])
    birth_date = rut * slope + intercept
    birth_date_year = int(birth_date)
    birth_date_month = int((birth_date - birth_date_year) * 12) + 1  
    if birth_date_month > 12:
        birth_date_month = 12
    birth_date_obj = datetime(birth_date_year, birth_date_month, 1)
    age = (today_date - birth_date_obj).days // 365  
    print(f"Edad: {age}, Nacimiento: {birth_date_year}-{birth_date_month}")   

def password(length=16):
    import random
    import string
    characters = string.ascii_letters + string.digits + "@#$%@$!%*?&"
    for i in range(10):
        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"Generated Password: {password}")
