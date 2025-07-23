def welcome_message():
    print("="*30) 
    print("Welcome to the Grade calculator") 
    print("="*30)


def get_test_scores(): 
      
    score_1 = float(input("ask user what is my score if i got 10/10: "))
    score_2 = float(input("ask user what is my score if i got: ")    )
    score_3 = float(input("ask user what is my score if i got: "))
    return score_1,score_2,score_3


def calculate_average(score_1,score_2,score_3):
    scores = score_1 + score_2 + score_3 
    average = scores/3
    return average
    print(f"the average is {average :.2f}") 

def get_letter_grade(average): 

    if average >= 90: 
      return "A" 
    elif average >= 80:   
         return "B"   
    elif average >= 70:
         return "C" 
    elif average >= 60:   
         return "D" 
    elif average <= 59:   
         return "F"
    else:
        print("Try aging i know you can do better!")






def display_resault(test1, test2, test3, avrage, letter_grade):
    """Function to display grade results"""
    print("/nYour Resaults:") 
    print(f"Test 1: {test1}")
    print(f"Test 2: {test2}")
    print(f"Test 3: {test3}")
    print(f"Average: {avrage:.1f}")
    print(f"Grade: {letter_grade}")


# Calculater average

# Get letter grade 




# You better run me be a good boy! 
def main():
    welcome_message()

    test1,test2,test3 = get_test_scores()

    avg = calculate_average(test1,test2,test3)

    grade = get_letter_grade(avg)

    # Display result
    display_resault(test1,test2,test3, avg,grade) 

    print("/n you are to yong get of the calculator buddy we all know your smart!!!!😎")
    

if __name__ == "__main__":
    main()



