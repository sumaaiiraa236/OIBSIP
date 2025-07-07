def calculatebmi(weight,height):
    return weight/(height**2)
def bmimeter(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5<=bmi<24.5:
        return "normal body mass index"
    elif bmi>24.5:
        return "overweight"
    else:
        return "obese"
print(f"WELCOME TO THE BMI CALCULATOR!") 
weight=float(input("enter the wieght in kgs: "))
height=float(input("enter the height in m: "))
bmi=calculatebmi(weight,height)
meter=bmimeter(bmi)
print(f"your the bmi {bmi:.2f} ({meter})")