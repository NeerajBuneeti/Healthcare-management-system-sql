# Healthcare-management-system
Project: Healthcare Managment System, This project is part of my coursework on Database organization(CS425) at Illinois Institute of technology.

A Healthcare Management System is a comprehensive software solution designed to streamline and optimize healthcare processes. It encompasses patient records, appointment 	scheduling, billing, Healthcareplan, labtest, Medicalrecord, Medications and overall patient care within healthcare departments. These systems aim to improve the quality of 	patient care, enhance communication among healthcare professionals, and ensure regulatory compliance.

How to build and run the code:

--> We are using PYTHON interface to build and run our code.
--> At First run database.py file, it creates a database (called Healthcare.db) and tables.
--> To verify all the operations into the command line tool, run Final_Deliverable.py file


All tables and schema used in this project:
--------------------------------------------

	● Patient(PID, Pname[Fname , Lname ], DOB , Gender , address , ContactNo , PEmail )
	● Hospital( HID , Hname , Haddress ,HCPlan)
	● MedicalStaff( SID , Sname [Fname , Lname ], Specialist ,ContactNo , SEmail , Designation )
	● Appointment( AID , PID , SID , ADate , Comment,HID )
	● MedicalRecord( RID , PID , SID , Rdate , Diagno, Treat , Presc)
	● Billing( BID , PID , MID, Pname[Fname,Lname] , SID , sname[Lname,fname], AID, BillDate , Amt , payStatus , Pmethod)
	● Medication( MID , Mname, PID , SID , desc , Instructions )
	● Healthcareprovider ( HPID , HPName , HPAdd , HPCNO , HPEmail, PLNID, HID )
	● Healthcareplan ( PLNID , PID , HPID , PlnName , PlnSdate , PlnEdate )
	● LabTest( TID , PID, SID , Tdate , TName , TResults , Range )


All operation is performed in this project:
-------------------------------------------

1. Create
2. Read
3. Update
4. Delete
5. Average
6. Count
7. Minimum
8. Maximum
9. Union
10. Intersect
11. NTile
12. Cummulative Distribution
13. OLAP_Groupby
15. Rollup


First we have create database Healthcare.db. and within that database we have created all tables and inserted data successfully.

Then we have written PYTHON code to perfom all operation for selected tables as mentioned above. First we have to select table and then select options to perform any operations.

All Tables options:

	1. Patient
	2. Healthcareprovider
	3. Healthcareplan
	4. Hospital
	5. MedicalStaff
	6. Appointment
	7. MedicalRecord
	8. Billing
	9. Medication
	10. LabTest
	11. Quit

After selecting tables, We have to select operations options as below one by one:

Option-1:

	CREATE operation: The CREATE TABLE statement is used to create a new table/records in a database.


Option-2:

	READ operation: The READ or SELECT statement is used to retrieve or read data from database.

Option-3 :

	UPDATE operation: The UPDATE statement is used to modify the existing records in a table.

Option-4:

	DELETE operation: The DELETE statement is used to delete existing records in a table.

Option-5:

	AVERAGE oepration: The AVG() function returns the average value of a numeric column.

Option-6:

	COUNT oepration: The COUNT() function returns the number of rows that matches a specified criterion.

Option-7:

	MINIMUM oepration: The MIN() function returns the smallest value of the selected column.

Option-8:

	MAXIMUM oepration: The MAX() function returns the largest value of the selected column.

Option-9:

	UNION oepration: The UNION operator is used to combine the result-set of two or more SELECT statements.

Option-10:

	INTERSECT oepration: The INTERSECTION operator is used to perform or returns only the common rows between two or more sets.

Option-11:

	NTile Operation: The NTile operator is used to divide the result set into a specified number of roughly equal parts (or "tiles") based on a specified column's values. 

Option-12:

	CUMMULATIVE DISTRIBUTION oepration: The CUMMULATIVE DISTRIBUTION operator is used to calculate the cumulative distribution of a set of values within a partition of the result set. 

Option-13:

	OLAP_Groupby oepration: The "GROUP BY" operation in OLAP is used to group data based on specific dimensions or attributes.

Option-14:

	ROLLUP oepration: The ROLLUP operator is used to provide a summarized view of data at higher levels of a hierarchy, aggregating data from lower levels.



We have executed many testcases (postive and negative ) for all these operations and It's executing as expected.

Also We have written Error Handling code like exception or Print particular and understanable error for all the operations.

Example: except Exception as e:
        	print(e)


Errors: If we select any random number or character which is not valid for the tables or choice we get error like

		"Invalid Table choice
		Enter again from 1 to 11"




CRUD operation Video: Link for the loom video: https://www.loom.com/share/8fe231c70aae45e7bd8a17d04ec104af?sid=ec2b5509-4df3-4894-a794-51f81cb065d3

