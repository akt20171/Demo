def get_average(grades):
    total = 0
    for g in grades:
        total = total + g
    return total / len(grades)

def print_result(name, grades):
    avg = get_average(grades)
    print(name + " average: " + str(avg))