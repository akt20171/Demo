def get_average(grades):
    return sum(grades) / len(grades)

def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def print_result(name, grades):
    avg = get_average(grades)
    print(name + " average: " + str(avg))
    print(name + " letter grade: " + get_letter_grade(avg))