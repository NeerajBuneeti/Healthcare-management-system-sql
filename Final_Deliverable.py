# GROUP N Deliverable-4
# To create an application / command line program to perform Create, Read, Update, Delete (CRUD) Operations on our database

import sqlite3

# To create a connection to database (Our database name is Healthcare)
conn = sqlite3.connect('Healthcare.db')
cursor = conn.cursor()

#To get column names of a table
def get_column_names(table_name):
    cursor.execute(f'PRAGMA table_info({table_name})')
    schema = cursor.fetchall()
    
    if not schema:
        return None 
    else:
        column_names = [column[1] for column in schema]
        return column_names


# CREATE operation
def create_record(table_name, data):
    try: 
        query = f'INSERT INTO {table_name} VALUES ({",".join(["?"] * len(data))})'
        cursor.execute(query, data)
        print(f'Record created successfully in the {table_name} table.')
    
    except Exception as e:
        print(e)
    
    finally:
        conn.commit()

#-------------------------------------------------------------------------------------------------------------------------------------
# READ operation
from prettytable import PrettyTable

def read_records(table_name):
    try:
        cursor.execute(f'SELECT * FROM {table_name}')
        records = cursor.fetchall()

        column_names = get_column_names(table_name)

        if column_names:
            print(f"\nTable: {table_name}")
            table = PrettyTable(column_names)
            
            if records:
                for record in records:
                    table.add_row(record)
                
                print(table)
            else:
                print("No records found.")
        else:
            print(f"No records found in the {table_name} table.")
    
    except Exception as e:
        print(e)


#-------------------------------------------------------------------------------------------------------------------------------------
# UPDATE operation
def update_record(table_name, record_id, update_data):
    try: 
        placeholders = ", ".join([f"{column} = ?" for column in update_data.keys()])
        query = f'UPDATE {table_name} SET {placeholders} WHERE {table_name}ID = ?'
        cursor.execute(query, list(update_data.values()) + [record_id])
        if cursor.rowcount > 0:
            print(f'Record with ID {record_id} updated in the {table_name} table.')
        else:
            print(f'Record with ID {record_id} not found in the {table_name} table.')

    except Exception as e:
        print(e)

    finally:
        conn.commit()
#-------------------------------------------------------------------------------------------------------------------------------------
# DELETE operation
def delete_record(table_name, record_id):
    try:
        cursor.execute(f'DELETE FROM {table_name} WHERE {table_name}ID = ?', (record_id,))
        if cursor.rowcount > 0:
            print(f'Record with ID {record_id} deleted from the {table_name} table.')
        else:
            print(f'Record with ID {record_id} not found in the {table_name} table.')
    except Exception as e:
        print(e)

    finally:
        conn.commit()
#-------------------------------------------------------------------------------------------------------------------------------------
# AVERAGE value
def compute_average(table_name, column_name):
    # Check if the column contains numeric data
    try:
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns_info = cursor.fetchall()
        target_column_info = [col for col in columns_info if col[1] == column_name]

        target_column_type = target_column_info[0][2].upper()

        if 'INT' not in target_column_type and 'REAL' not in target_column_type:
            print(f"Average value cannot be computed for column '{column_name}' as it does not contain numeric data.")
            return

        cursor.execute(f"SELECT AVG({column_name}) FROM {table_name}")
        average_value = cursor.fetchone()[0]
        average_value = round(average_value, 2)

        if average_value is not None:
            print(f"\nAverage value of '{column_name}' in the {table_name} table: {average_value}")
        else:
            print(f"No records found in the {table_name} table.")
    
    except Exception as e:
        print(e)
#-------------------------------------------------------------------------------------------------------------------------------------
# COUNT value
def count_records(table_name, column_name, value):
    try:
        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} = ?", (value,))
        count = cursor.fetchone()[0]
        print(f"Count of '{value}' records in {table_name} {column_name} is: {count}")
        return count
    except Exception as e:
        print(e)
#-------------------------------------------------------------------------------------------------------------------------------------
# MIN value
def compute_min(table_name, column_name):
    try:
        cursor.execute(f"SELECT MIN({column_name}) FROM {table_name}")
        min_value = cursor.fetchone()[0]

        if min_value is not None:
            print(f"\nMinimum value of '{column_name}' in the {table_name} table: {min_value}")
        else:
            print(f"No records found in the {table_name} table.")
    except Exception as e:
        print(e)
#-------------------------------------------------------------------------------------------------------------------------------------
# MAX value
def compute_max(table_name, column_name):
    try:
        cursor.execute(f"SELECT MAX({column_name}) FROM {table_name}")
        max_value = cursor.fetchone()[0]

        if max_value is not None:
            print(f"\nMaximum value of '{column_name}' in the {table_name} table: {max_value}")
        else:
            print(f"No records found in the {table_name} table.")
    except Exception as e:
        print(e)
#-------------------------------------------------------------------------------------------------------------------------------------
def get_unique_values(table_name, column_name):
    try:
        cursor.execute(f"SELECT DISTINCT {column_name} FROM {table_name}")
        unique_values = cursor.fetchall()
        unique_values = [str(value[0]) for value in unique_values]
        return unique_values
    except Exception as e:
        print(e)
#-------------------------------------------------------------------------------------------------------------------------------------
def print_ids(table_name):
    try:
        cursor.execute(f"SELECT {table_name}ID FROM {table_name} WHERE {table_name}ID IS NOT NULL")
        ids = cursor.fetchall()

        if ids:
            ids_str = ', '.join(str(record_id[0]) for record_id in ids)
            print(f"\nIDs in the {table_name} table: {ids_str}")
    except Exception as e:
        print(e)
#-------------------------------------------------------------------------------------------------------------------------------------

def rollup(table_name):
    try:
        if table_name == 'Billing':
            query = f""" SELECT PatientID, MedicalStaffID, AppointmentID, SUM(CAST(Billing_amount AS INTEGER)) AS TotalAmount
                FROM {table_name}
                GROUP BY PatientID, MedicalStaffID, AppointmentID
                UNION
                SELECT PatientID, NULL, NULL, SUM(CAST(Billing_amount AS INTEGER)) AS TotalAmount
                FROM {table_name}
                GROUP BY PatientID
                UNION
                SELECT NULL, NULL, NULL, SUM(CAST(Billing_amount AS INTEGER)) AS TotalAmount
                FROM {table_name};"""
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(row)
        else:
            print("Cant compute rollup for the follwoing table")
    except:
        print("Error has occured, please try again") 
#-------------------------------------------------------------------------------------------------------------------------------------
def cube(table_name):
    try:
        if table_name == 'Billing':
            query = '''
                SELECT 
                    PatientID, MedicalstaffID, Billing_paymentstatus, 
                    SUM(CAST(Billing_amount AS FLOAT)) AS TotalAmount
                FROM 
                    BILLING
                GROUP BY 
                    PatientID, MedicalstaffID, Billing_paymentstatus
                '''
            cursor.execute(query)
            results = cursor.fetchall()
            for row in results:
                print(row)
        else:
            print("Cant compute cube for the follwoing table")
    except:
        print("Error has occured, please try again") 

#-------------------------------------------------------------------------------------------------------------------------------------
def cummulative_distribution(table_name):
    try:
        if table_name == 'Billing':
            cursor.execute("SELECT * FROM BILLING")
            overall_billing_data = cursor.fetchall()
            billing_ID = [i[0] for i in overall_billing_data]

            total = len(billing_ID)
            cdf = [i / total for i in range(total)]
            print("billing ID, Cummualtive distribution")
            for i,j in list(zip(billing_ID,cdf)):
                print(i, '~>', j)
        else:
            print(f"Cant compute cummulative distribution for the {table_name} table")
    except:
        print("Error has occured, please try again") 
#-------------------------------------------------------------------------------------------------------------------------------------
def ntile(table_name,ntile_number):
    try:
        if table_name == 'Billing':
            query = f"""SELECT PatientID, MedicalstaffID , AppointmentID, Billing_amount,
            NTILE({ntile_number}) OVER (ORDER BY Billing_amount) as 'ntile{ntile_number}' FROM billing;
            """
            # Execute the query
            cursor.execute(query)

            # Fetch the results
            results = cursor.fetchall()
            print(f"PatientID, MedicalstaffID , AppointmentID, Billing_amount, Ntile({ntile_number})")
            # Displaying the results
            for row in results:
                print(row)
        else:
            print(f"Cant compute NTILE for the {table_name} table")
    except:
        print("Error has occured, please try again") 

#-------------------------------------------------------------------------------------------------------------------------------------
def OLAP(table_name):
    try:
        if table_name == 'Billing':
            query = '''
                SELECT
                MedicalstaffID,
                Billing_date,
                SUM(CAST(Billing_amount AS DECIMAL(10, 2))) AS total_billing_amount
            FROM
                BILLING
            GROUP BY
                MedicalstaffID,
                Billing_date
            ORDER BY
                MedicalstaffID,
                Billing_date;

                '''
            cursor.execute(query)
            results = cursor.fetchall()
            print("MedicalstaffID, Billing_date, Total_billing_amount")
            for row in results:
                print(row)
        else:
            print(f"Cant compute OLAP for the {table_name} table")
    except:
        print("Error has occured, please try again") 
#-------------------------------------------------------------------------------------------------------------------------------------
 # UNION operation
def Union_record(table_name1, table_name2):
       
    try:    
        cursor.execute(f'''
        SELECT * FROM {table_name1}
        UNION
        SELECT * FROM {table_name2};
        ''')
    except:
        print("Choose the tables with same number of columns")
    # Fetch and print the results
    result = cursor.fetchall()
    for row in result:
        print(row)
#-------------------------------------------------------------------------------------------------------------------------------------
# INTERSECT operation
def Intersect_record(table_name1, table_name2):

    try:
        cursor.execute(f'''
        SELECT * FROM {table_name1}
        INTERSECT
        SELECT * FROM {table_name2};
        ''')
    except:
        print(f"There are no common rows in {table_name1} and {table_name2}")
    # Fetch and print the results
    result = cursor.fetchall()
    for row in result:
        print(row)
#-------------------------------------------------------------------------------------------------------------------------------------


# MENU to display the tables present in the database
if __name__ == "__main__":
    while True:
        print("\nSelect a table to perform the operations:")
        print("1. Patient")
        print("2. Healthcareprovider")
        print("3. Healthcareplan")
        print("4. Hospital")
        print("5. Medicalstaff")
        print("6. Appointment")
        print("7. MedicalRecord")
        print("8. Billing")
        print("9. Medication")
        print("10. LabTest")
        print("11. Quit")

        choice = input("Enter the number of the table: ")

        if choice == "11":
            print("Group N Program Exited, Goodbye!")
            break

        if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            table_name = [
                "Patient",
                "Healthcareprovider",
                "Healthcareplan",
                "Hospital",
                "Medicalstaff",
                "Appointment",
                "MedicalRecord",
                "Billing",
                "Medication",
                "LabTest",
            ][int(choice) - 1]

            print(f"Selected table: {table_name}")

            while True:
                print("\nOptions:") # Operations Menu Create, Read, Update, Delete (CRUD)
                print("1. Create a record")
                print("2. Read a record")
                print("3. Update a record")
                print("4. Delete a record")
                print("5. Average value of a column")
                print("6. Count appearances in a column")
                print("7. Minimun value of a column")
                print("8. Maximum value of a column")
                print("9. Union Operation")
                print("10. Intersect Operation")
                print("11. NTile")
                print("12. Cumulative Distribution")
                print("13. OLAP")
                print("14. Cube")
                print("15. Rollup")      

                operation_choice = input("Enter your choice: ")

                if operation_choice == "1":
                    while True:
                        data = []
                        column_names = get_column_names(table_name)
                        
                        if column_names:
                            print(f"Enter data in this order:\n {', '.join(column_names)}")
                            values = input("Enter values (comma-separated):\n ").split(',')
                            
                            if len(values) != len(column_names):
                                print("Invalid Entry!!! \n Number of values entered does not match the number of columns \n Enter Again")
                                continue  
                            else:
                                data = values
                                break  
                        else:
                            print(f"Table {table_name} does not exist.")
                            break  
                    create_record(table_name, data)
                    break

                elif operation_choice == "2":
                    read_records(table_name)
                    break

                elif operation_choice == "3":
                    while True:
                        record_id = int(input(f"Enter the ID of the record you want to update in {table_name}: "))
                        
                        # Check the ID exists in table
                        cursor.execute(f'SELECT * FROM {table_name} WHERE {table_name}ID = ?', (record_id,))
                        if cursor.fetchone():
                            break  # Exit for invalid ID
                        else:
                            print(f"Record with ID {record_id} does not exist in the {table_name} table. Please enter a valid ID from.")
                            print_ids(table_name)

                    while True:
                        column_name = input("Enter the name of the column you want to update: ")
                        if column_name not in get_column_names(table_name):
                            print(f"Column '{column_name}' does not exist in the {table_name} table\nPlease enter a valid column name from the following\n")
                            print(get_column_names(table_name))
                        else:
                            new_value = input(f"Enter the new value for the {column_name} column: ")
                            update_data = {column_name: new_value}
                            update_record(table_name, record_id, update_data)
                            break                    
                    break

                elif operation_choice == "4":
                    record_id = int(input(f"Enter the ID of the record you want to delete from {table_name}: "))
                    delete_record(table_name, record_id)
                    break

                elif operation_choice == "5":
                    while True:
                        column_name = input("Enter the name of the column to compute the average value: ")
                        if column_name not in get_column_names(table_name):
                            print(f"Column '{column_name}' does not exist in the {table_name} table\nPlease enter a valid column name from the following\n")
                            print(get_column_names(table_name))
                        else:
                            compute_average(table_name, column_name)
                            break
                    break

                elif operation_choice == "6":
                        # Count records
                        while True:
                            column_name = input("Enter the name of the column to count records: ")
                            if column_name not in get_column_names(table_name):
                                print(f"Column '{column_name}' does not exist in the {table_name} table\nPlease enter a valid column name from the following\n")
                                print(get_column_names(table_name))
                            else:
                                while True:
                                    value_to_count = input(f"Enter the value to count in the {column_name} column: ")
                                    count = count_records(table_name, column_name, value_to_count)
                                    if count == 0:
                                        print(f"No records found with the value '{value_to_count}' in the {column_name} column. Please enter a valid value.")
                                        unique_values = get_unique_values(table_name, column_name)
                                        print(f"Unique values in {table_name} {column_name}: {', '.join(unique_values)}")
                                    else:
                                        break
                                break
                        break
                
                elif operation_choice == "7":
                    while True:
                        column_name = input("Enter the name of the column to compute the minimum value: ")
                        if column_name not in get_column_names(table_name):
                            print(f"Column '{column_name}' does not exist in the {table_name} table\nPlease enter a valid column name from the following\n")
                            print(get_column_names(table_name))
                        else:
                            compute_min(table_name, column_name)
                            break
                    break

                elif operation_choice == "8":
                    while True:
                        column_name = input("Enter the name of the column to compute the maximum value: ")
                        if column_name not in get_column_names(table_name):
                            print(f"Column '{column_name}' does not exist in the {table_name} table\nPlease enter a valid column name from the following\n")
                            print(get_column_names(table_name))
                        else:
                            compute_max(table_name, column_name)
                            break
                    break

                elif operation_choice == "9":

                    choice = int(input('Enter the second table to execute Union operation: '))
                    if 1 <= choice <= 10:
                        table_name2 = [
                            "Patient",
                            "Healthcareprovider",
                            "Healthcareplan",
                            "Hospital",
                            "Medicalstaff",
                            "Appointment",
                            "MedicalRecord",
                            "Billing",
                            "Medication",
                            "LabTest",
                        ][choice - 1]
                    Union_record(table_name, table_name2)
                    break
                
                elif operation_choice == "10":
                    choice = int(input('Enter the second table to execute Intersect operation: '))
                    if 1 <= choice <= 10:
                        table_name2 = [
                            "Patient",
                            "Healthcareprovider",
                            "Healthcareplan",
                            "Hospital",
                            "Medicalstaff",
                            "Appointment",
                            "MedicalRecord",
                            "Billing",
                            "Medication",
                            "LabTest",
                        ][choice - 1]
                    Intersect_record(table_name, table_name2)
                    break
                
                elif  operation_choice == '11':
                    ntile_number = int(input(f"Enter the Ntile Number you want to perform on {table_name}: "))
                    ntile(table_name,ntile_number)
                    break
                
                elif  operation_choice == '12':
                    cummulative_distribution(table_name)
                    break

                elif  operation_choice == '13':
                    OLAP(table_name)
                    break
                
                elif  operation_choice == '14':
                    cube(table_name)
                    break
                
                elif  operation_choice == '15':
                    rollup(table_name)
                    break

                else:
                    print("Invalid Operation Choice.\nPlease enter choice from 1 to 15\n")             

        else:
            print("Invalid table choice \n Enter Again from 1 to 11")

