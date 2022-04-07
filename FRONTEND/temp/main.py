import csv

# field names will be assigned to the csv file
fields = ['Date', 'Time', 'Name', 'Room_Temp' ,'Body_Temp' , 'Oxy_Sat' , 'Heart_rate']
 
 #variables that will store the data of the scanner
v_date = "April 7 ,2022"
v_time = "10 AM"
v_name = "John Eric"
v_rt = 30
v_bt = 37.2
v_oxs = 99
v_hr = 120

data = [[v_date , v_time ,v_name , v_rt , v_bt , v_oxs , v_hr]]
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
        if line_no == 2:
            
            d_data = (line[0])
            t_data = (line[1])
            n_data = (line[2])
            rt_data = (line[3])
            bt_data = (line[4])
            os_data = (line[5])
            hr_data = (line[6])
            
            print(n_data)
