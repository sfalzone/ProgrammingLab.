values = []

my_file = open ('shampoo_sales.csv'. 'r')
for line in my_file:

    elements = line.splip(',')

    if elements[0] != 'Date' :

        date = elements[0]
        value = elements[1]

        values.appened(value)