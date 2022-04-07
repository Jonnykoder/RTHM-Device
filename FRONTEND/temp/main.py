import csv
import numpy as np 
# field names
fields = ['Date', 'Time', 'Name', 'Room_Temp' ,'Body_Temp' , 'Oxy_Sat' , 'Heart_rate']
 
# data rows of csv file
data = [ ['March 21', '10 am', 'john', '30' , '36.6' , '95' ,'129']]
filename = "temp_user_data.csv"
with open(filename, 'w') as f:
    # creating a csv writer object
    csvwriter = csv.writer(f)
    # writing the fields
    csvwriter.writerow(fields)
    # writing the data rows
    csvwriter.writerows(data)
    
    
#reading csv file
with open(filename, 'r') as r:
    csv_reader = csv.reader(r)
    for line_no , line in enumerate(csv_reader , 1):
        if line_no == 1:
           """
            print('Header:')
            print(line[0])
            print('data:')
            """
            
        else:
            d_data = (line[0])
            t_data = (line[1])
            n_data = (line[2])
            rt_data = (line[3])
            bt_data = (line[4])
            os_data = (line[5])
            hr_data = (line[6])
            
            print(d_data)
    