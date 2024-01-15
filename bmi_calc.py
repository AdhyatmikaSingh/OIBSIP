# Taking input from the users  
height = float(input("Enter the height in cm: "))  
weight = float(input("Enter the weight in kg: "))  
# calculating  BMI  
BMI = weight / (height/100)**2  
# printing  BMI  
print("Your Body Mass Index is", BMI)  
# using the if-elif-else conditions  
if BMI <= 18.5:  
    print("Oops! You are underweight.")  
elif BMI <= 24.9:  
    print("Awesome! You are healthy.")  
elif BMI <= 29.9:  
    print("Eee! You are over weight.")  
else:  
    print("Seesh! You are obese.")
