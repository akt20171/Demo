def get_average(grades):
    return sum(grades) / len(grades)

def print_result(name, grades):
    avg = get_average(grades)
    print(name + " average: " + str(avg))