def sum_csv(input):
    file = open('shampoo_sales.csv','r')
    values = []

    for line in file :
        elements = line.split(',')
        
        if elements[0] != 'Date' :
            values = elements[1]
            values.append(float(value))
    file.close()
    
    if(len(values) == 0):
        return None
    else:
        return sum(values)