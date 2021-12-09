import datetime
import xlwt
from datetime import date
from xlwt import Workbook

# Workbook is created
wb = Workbook()

# add sheet
sheet1 = wb.add_sheet('Temperature Scans')

sheet1.write(0, 0, 'First Name')
sheet1.write(0, 1, 'Last Name')
sheet1.write(0, 2, 'Date')
sheet1.write(0, 3, 'Temperature')

Normal = 98.6

Recording = int(input("Are you Recording Temperature Today? 1 if yes; 0 if no: "))

counter = 0
while Recording == 1 and counter < 1000:
        Employee_First = input("Enter First Name: ")
        Employee_Last = input("Enter Last Name: ")
        Temp = float(input("Input Scanned Temperature (Example if 99 degrees enter 99): "))
        if Temp > Normal:
                print("Elevated Temperature Detected! Entrance Not Permitted")
        else:
                print("Temperature Within Acceptable Limits. Entrance Permitted")
        Date = datetime.datetime.today().strftime("%m/%d/%y")

        counter = counter + 1
        
        for i in range(1, 15000):
                sheet1.write(counter, 0, Employee_First)
                sheet1.write(counter, 1, Employee_Last)
                sheet1.write(counter, 2, Date)
                sheet1.write(counter, 3, Temp)
		
                Day = datetime.datetime.today().strftime("%d")
                Month = datetime.datetime.today().strftime("%m")
                Year = datetime.datetime.today().strftime("%y")

                StringDate = Month + Day + Year + ' Temp Scans.csv'
		
                wb.save(StringDate)

                break

        Recording = int(input("Are you Recording Temperature Today? 1 if yes; 0 if no: "))

        if Recording == 1:
                continue
        else:
                break    
           
                
                        



	


        

	
	
                
        

        
	
	
	
	
	
	
	
	
	
	
	
	
	

