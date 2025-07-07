def calculatebmi(weight,height):
    return weight/(height**2)
def bmimeter(indx):
    if indx < 18.5:
        return "underweight"
    elif 18.5<=indx <24.5:
        return "normal body mass index"
    elif indx>24.5:
        return "overweight"
    else:
        return "obese"
print(f"WELCOME TO THE BMI CALCULATOR!") 
weight=float(input("enter the wieght: "))
height=float(input("enter the height: "))
bmi=calculatebmi(weight,height)
meter=bmimeter(indx)
print(f"enter the bmi {bmi:.2f} ({meter})")