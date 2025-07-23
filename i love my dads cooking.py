# Create a varuble for
age = 17

# Basic if statment - only runs if condition is if conditions is true
if age >= 16:
    print(f"you are{age} years old. ") 
    print("you can dirve ") 



print()

print("section 2")
print("="* 30)


temp = 75

if temp >= 80:
    print("its {temp} degrees outside.")
    print("its hot outside")
else:
    print(f"its {temp} degrees outside.")
    print("its cold outside you are a kid so you canot play out side hahahahahaha")


print("Section 2")

student_grade = 85

# If-elif-els statment - multipul condetions 
if student_grade >=90:
    print(f"your grade is {student_grade}") 
    print("Exellent! you got an A!") 
elif student_grade >= 80:
    print(f"your grade is {student_grade}") 
    print("Exellent! you got an B!")
else:
    print(f"your grade is {student_grade}") 
    print("Keep studying! you can do better!") 



score = 90

if score != 100: 
    print(f"your score is {score}")
    print(f"Almost perfect, But not quite 100!") 




# Using QR operator - true if ANY condition is true 

day = "sunday"

if day =="saterday" or day == "sunday": 
    print(f"Today is {day}") 
    print("its the weekend") 
else:
    print(f"Today is {day}") 
    print("its a weekday. Time for shool or work!")
