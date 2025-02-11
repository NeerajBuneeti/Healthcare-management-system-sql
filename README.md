# Healthcare Management System


## 📌 Overview

This Healthcare Management System is a comprehensive software solution designed to streamline and optimize healthcare processes. Developed as part of the Database Organization (CS425) coursework at Illinois Institute of Technology, this system manages patient records, appointment scheduling, billing, healthcare plans, lab tests, medical records, medications, and overall patient care within healthcare departments.

## 🎯 Objectives

- Improve the quality of patient care
- Enhance communication among healthcare professionals
- Ensure regulatory compliance
- Optimize healthcare processes

## 🗂️ Database Schema

The system utilizes the following tables:

| Table Name | Primary Key | Notable Fields |
|------------|-------------|-----------------|
| Patient | PID | Pname, DOB, Gender, Address |
| Hospital | HID | Hname, Haddress, HCPlan |
| MedicalStaff | SID | Sname, Specialist, Designation |
| Appointment | AID | PID, SID, ADate, Comment |
| MedicalRecord | RID | PID, SID, Diagno, Treat |
| Billing | BID | PID, MID, AID, Amt, PayStatus |
| Medication | MID | Mname, PID, SID, Instructions |
| Healthcareprovider | HPID | HPName, PLNID, HID |
| Healthcareplan | PLNID | PID, HPID, PlnName, PlnSdate |
| LabTest | TID | PID, SID, TName, TResults |

## 🛠️ Features and Operations

1. **CRUD Operations**
   - Create, Read, Update, Delete records in all tables

2. **Advanced Queries**
   - Average, Count, Minimum, Maximum
   - Union and Intersect
   - NTile and Cumulative Distribution
   - OLAP Group By and Rollup

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- SQLite3

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/healthcare-management-system.git
   ```

2. Navigate to the project directory:
   ```
   cd healthcare-management-system
   ```

3. Run the database setup script:
   ```
   python database.py
   ```

4. Launch the main application:
   ```
   python Final_Deliverable.py
   ```

## 🖥️ Usage

1. Select a table from the main menu (1-10)
2. Choose an operation to perform (1-15)
3. Follow the prompts to input data or view results

## 🎥 Demo

Watch our [CRUD operations demo video](https://www.loom.com/share/8fe231c70aae45e7bd8a17d04ec104af?sid=ec2b5509-4df3-4894-a794-51f81cb065d3) to see the system in action.

## 🧪 Testing

We've conducted extensive testing, including:
- Positive and negative test cases for all operations
- Error handling and user-friendly error messages

## 🙏 Acknowledgments

- Illinois Institute of Technology,
- Professor Gerald Balekaki

---
