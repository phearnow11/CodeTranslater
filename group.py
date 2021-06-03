import random 
import mathbyme

def rangroup(members, rows):
    columns = mathbyme.GCD(members. rows)
    table = []
    for i in range(0,rows):
        table.append([])
        for j in range(0, columns):
            table[i].append(random.randint(0,members))
    return table
