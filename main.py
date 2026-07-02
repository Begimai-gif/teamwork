# print('hello world')

sales = [1200, 850, 430, 2100, 1750]


def calculate_total(sales):
    
    return sum(sales)


def calculate_average(sales):
    return calculate_total(sales)/len(sales)

    

print(calculate_total(sales))
print(calculate_average(sales))