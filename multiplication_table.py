def print_multiplication_table(table,start,end):
    for i in range(start,end ):
        print (f"{table} * {i} = {table * i }")
	print (" {0} * {1} = {2} ".format(table,i,table+i))

print_multiplication_table(5,1,11)

