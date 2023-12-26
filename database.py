import sqlite3

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('Healthcare.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the 'Patient' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Patient (
  PatientID INTEGER PRIMARY KEY,
  Patient_firstname VARCHAR(25),
  Patient_lastname VARCHAR(25),
  Patient_DateofBirth DATE,
  Patient_Gender VARCHAR(6),
  Patient_address VARCHAR(50),
  Patient_phonenumber VARCHAR(15),
  Patient_email VARCHAR(50)
);
''')

# Insert values into the 'Patient' table
cursor.executemany('''
INSERT INTO Patient (PatientID, Patient_firstname, Patient_lastname, Patient_DateofBirth, Patient_Gender, Patient_address, Patient_phonenumber, Patient_email) VALUES (?, ?, ?, ?, ?, ?, ?, ?);
''', [
    (1, 'Maxwell', 'Longstreeth', '2008-11-17', 'M', '2851 Talisman Drive', '845 866 3572', 'mlongstreeth0@live.com'),
    (2, 'Johnathan', 'Hazlewood', '1992-05-07', 'M', '26 La Follette Point', '143 764 2212', 'jhazlewood1@skyrock.com'),
    (3, 'Natala', 'Shackell', '2009-09-23', 'F', '4 Duke Point', '379 692 6948', 'nshackell2@tuttocitta.it'),
    (4, 'Kareem', 'Gathercole', '2000-04-09', 'M', '0 Merchant Junction', '102 769 4217', 'kgathercole3@phpbb.com'),
    (5, 'Quillan', 'Pierrepoint', '2001-06-19', 'M', '28 Heath Drive', '520 326 6798', 'qpierrepoint4@phpbb.com'),
    (6, 'Shantee', 'Mainston', '1997-01-09', 'F', '4 Cascade Junction', '146 639 7710', 'smainston5@skype.com'),
    (7, 'Ronda', 'Easterfield', '1997-04-25', 'F', '1 Jenna Park', '194 204 4719', 'reasterfield6@tiny.cc'),
    (8, 'Mora', 'Harpham', '2010-06-19', 'F', '90 Kedzie Avenue', '394 921 9045', 'mharpham7@loc.gov'),
    (9, 'Mord', 'Batt', '2018-04-26', 'M', '449 Scofield Trail', '146 460 4194', 'mbatt8@timesonline.co.uk'),
    (10, 'Wilbur', 'Kordt', '1982-05-11', 'M', '51 Fulton Avenue', '621 892 3239', 'wkordt9@paypal.com'),
    (11, 'Ab', 'Macauley', '1986-05-27', 'M', '54 Toban Lane', '260 921 9022', 'amacauleya@nature.com'),
    (12, 'Rafaelita', 'Minger', '2012-09-11', 'F', '696 Stuart Court', '855 577 2785', 'rmingerb@mac.com'),
    (13, 'Daron', 'Gabitis', '2015-04-04', 'M', '6159 Novick Junction', '378 431 2001', 'dgabitisc@reddit.com'),
    (14, 'Ysabel', 'Purselow', '2005-05-28', 'F', '3865 Kropf Circle', '881 635 8524', 'ypurselowd@zdnet.com'),
    (15, 'Tove', 'Grabbam', '2004-09-03', 'F', '4 Green Alley', '766 609 3291', 'tgrabbame@friendfeed.com')
])

# Create the 'Healthcareprovider' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Healthcareprovider (
  HealthcareproviderID INTEGER PRIMARY KEY,
  Healthcareprovider_name VARCHAR(25),
  Healthcareprovider_address VARCHAR(50),
  Healthcareprovider_contactno VARCHAR(15),
  Healthcareprovider_email VARCHAR(30)
);
''')

# Insert values into the 'Healthcareprovider' table
cursor.executemany('''
INSERT INTO Healthcareprovider (HealthcareproviderID, Healthcareprovider_name, Healthcareprovider_address, Healthcareprovider_contactno, Healthcareprovider_email) VALUES (?, ?, ?, ?, ?);
''', [
    (118, 'Zooveo', 'Room 1568', '404 449 3090', 'elissandri0@scribd.com'),
    (141, 'Kimia', 'Suite 16', '315 232 3707', 'aedgeson1@epa.gov'),
    (136, 'Oloo', 'Apt 1830', '505 755 5629', 'cgreystoke2@livejournal.com'),
    (124, 'Wikibox', 'Apt 93', '860 256 9031', 'mpopov3@hatena.ne.jp'),
    (115, 'Midel', 'PO Box 81000', '686 590 2388', 'mharverson4@devhub.com'),
    (112, 'Talane', 'Suite 18', '537 560 3520', 'mazema5@google.es'),
    (117, 'Rhynoodle', 'Room 1481', '471 867 2827', 'bguillard6@nytimes.com'),
    (135, 'Avamba', 'PO Box 88510', '464 995 3708', 'chartfleet7@ucsd.edu'),
    (133, 'Aimbu', '12th Floor', '689 428 3300', 'abarthel8@prweb.com'),
    (147, 'Linktype', 'Suite 87', '223 146 8810', 'wgurnee9@state.gov'),
    (145, 'Skiptube', 'Apt 618', '734 815 7255', 'rbenjafielda@theguardian.com'),
    (120, 'Oyondu', 'Room 1883', '509 222 7841', 'cjennionsb@hibu.com'),
    (132, 'Voolia', 'Apt 6', '367 301 4186', 'aclimie@bandcamp.com'),
    (121, 'Zoomlounge', 'Suite 83', '935 845 7864', 'fsnodgrassf@amazon.de'),
    (142, 'Lazz', 'Room 1202', '216 766 3289', 'pflowerdewg@hibu.com'),
    (130, 'Livetube', 'Apt 51', '944 202 7135', 'lpagelh@home.pl'),
    (146, 'Thoughtsphere', 'Suite 116', '227 713 5533', 'wraffertyi@plala.or.jp'),
    (119, 'Livepath', 'PO Box 588', '384 243 8934', 'fmarkesj@archive.org'),
    (143, 'Voolith', 'Room 1409', '314 115 9381', 'hpostlek@shareasale.com'),
    (116, 'Kwideo', 'Apt 8', '676 761 2323', 'llorand@aboutads.info')
])

# Create the 'Healthcareplan' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Healthcareplan (
  HealthcareplanID integer PRIMARY KEY,
  PatientID integer,
  HealthcareproviderID integer,
  Healthcareplan_name varchar(25),
  Healthcareplan_startdate date, 
  Healthcareplan_enddate date, 
  FOREIGN KEY(PatientID) REFERENCES Patient(PatientID),
  FOREIGN KEY(HealthcareproviderID) REFERENCES Healthcareprovider(HealthcareproviderID)
);
''')

# Insert values into the 'Healthcareplan' table
cursor.executemany('''
INSERT INTO Healthcareplan (HealthcareplanID, PatientID, Healthcareplan_name, Healthcareplan_startdate, Healthcareplan_enddate, HealthcareproviderID) VALUES (?, ?, ?, ?, ?, ?);
''', [
    (202, 6, 'Goldner Inc', '2022-07-28', '2023-12-21', 118),
    (241, 6, 'Schmeler LLC', '2022-09-12', '2022-12-03', 136),
    (245, 8, 'Dibbert-Beer', '2023-07-17', '2023-12-18', 141),
    (212, 7, 'Friesen and Sipes', '2022-12-19', '2023-03-05', 136),
    (206, 9, 'O''Keefe-Cassin', '2023-08-12', '2023-12-18', 124),
    (201, 3, 'Harber, Kuphal', '2022-07-28', '2023-12-21', 112),
    (248, 4, 'Cassin-Stark', '2022-07-16', '2023-11-14', 128),
    (250, 5, 'Bernier Inc', '2023-04-02', '2023-12-29', 133),
    (289, 3, 'Rosenbaum and Ritchie', '2023-01-15', '2023-11-14', 135),
    (242, 12, 'Denesik and Sons', '2022-02-17', '2023-04-16', 117),
    (203, 9, 'Tromp Inc', '2023-08-31', '2023-02-23', 147),
    (244, 1, 'Smith Inc', '2022-07-18', '2023-11-05', 145)
])

# Create the 'Hospital' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Hospital (
  HospitalID integer PRIMARY KEY,
  Hospital_name varchar(25),
  Hospital_address varchar(50),
  HealthcareplanID integer,
  FOREIGN KEY(HealthcareplanID) REFERENCES Healthcareplan(HealthcareplanID)
);
''')

# Insert values into the 'Hospital' table
cursor.executemany('''
INSERT INTO Hospital (HospitalID, Hospital_name, Hospital_address, HealthcareplanID) VALUES (?, ?, ?, ?);
''', [
    (385, 'Toy Inc', '89 Nova Point', 250),
    (310, 'Smith and Sons', '9 Moose Lane', 289),
    (378, 'Hansen and Sons', '596 Springview Plaza', 202),
    (335, 'Schulist LLC', '96730 Northport Avenue', 201),
    (361, 'Mann Inc', '562 Anzinger Lane', 203),
    (323, 'Runte-Kulas', '62067 Emmet Way', 212),
    (334, 'Blick LLC', '7591 Helena Alley', 245),
    (386, 'Sipes and Considine', '42350 Declaration Crossing', 250),
    (311, 'Bergstrom-Grimes', '29684 Prentice Terrace', 241),
    (313, 'Hackett and Macejkovic', '43425 Arapahoe Road', 289),
    (306, 'Weimann, Larkin and Koss', '67953 Forest Avenue', 203),
    (325, 'Monahan, Huel and Kling', '8 Arkansas Road', 212),
    (357, 'Grant-Deckow', '4898 Fair Oaks Alley', 206),
    (344, 'Kuvalis-Runolfsson', '4229 Carpenter Way', 244)
])

# Create the 'Medicalstaff' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Medicalstaff (
  MedicalstaffID integer PRIMARY KEY,
  Medicalstaff_firstname varchar(25),
  Medicalstaff_lastname varchar(25),
  Medicalstaff_specialty varchar(25),
  Medicalstaff_phonenumber varchar(15),
  Medicalstaff_email varchar(30),
  Medicalstaff_designation varchar(20)
);
''')

# Insert values into the 'Medicalstaff' table
cursor.executemany('''
INSERT INTO Medicalstaff (MedicalstaffID, Medicalstaff_firstname, Medicalstaff_lastname, Medicalstaff_specialty, Medicalstaff_phonenumber, Medicalstaff_email, Medicalstaff_designation) VALUES (?, ?, ?, ?, ?, ?, ?);
''', [
    (451, 'Dotty', 'Railton', 'Anesthesiology', '7568949499', 'drailton0@google.de', 'surgeons'),
    (488, 'Leicester', 'Sudell', 'Plastic Surgery', '5189280478', 'lsudell1@miitbeian.gov.cn', 'Physical Therapist'),
    (401, 'Constancia', 'Stuchbury', 'General Surgery', '3234516447', 'cstuchbury2@barnesandnoble.com', 'surgeons'),
    (481, 'Matthus', 'Digle', 'Cardiology', '1417577727', 'mdigle3@purevolume.com', 'doctors'),
    (446, 'Nydia', 'Tadman', 'Anesthesiology', '7739657831', 'ntadman4@xing.com', 'Medical Receptionist'),
    (425, 'Bucky', 'MacAdam', 'Cardiology', '4271884242', 'bmacadam5@about.com', 'Medical Receptionist'),
    (493, 'Rennie', 'Chinnick', 'Allergy and Immunology', '9427987575', 'rchinnick6@biglobe.ne.jp', 'Nurse Practitioner'),
    (480, 'Micaela', 'Boylan', 'General Surgery', '1685265510', 'mboylan7@abc.net.au', 'nurses'),
    (430, 'Dare', 'Insoll', 'General Surgery', '2416098768', 'dinsoll8@aol.com', 'surgeons'),
    (455, 'Carlotta', 'Rushton', 'Cardiology', '9338157717', 'crushton9@auda.org.au', 'nurses'),
    (427, 'Frederigo', 'Morde', 'Emergency Medicine', '6122171984', 'fmordea@mail.ru', 'nurses'),
    (465, 'Eziechiele', 'Snell', 'Emergency Medicine', '6157216219', 'esnellb@gmpg.org', 'surgeons'),
    (416, 'Marchall', 'Alfonsetti', 'Plastic Surgery', '3733228583', 'malfonsettid@lulu.com', 'doctors'),
    (413, 'Kriste', 'Kohnert', 'Emergency Medicine', '7205840488', 'kkohnerte@jalbum.net', 'Nurse Practitioner')
])

# Create the 'Appointment' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Appointment (
  AppointmentID integer PRIMARY KEY,
  PatientID integer,
  HospitalID integer,
  MedicalstaffID integer,
  Appointment_date date,
  Notes varchar(255),
  FOREIGN KEY(PatientID) REFERENCES Patient(PatientID),
  FOREIGN KEY(MedicalstaffID) REFERENCES Medicalstaff(MedicalstaffID),
  FOREIGN KEY(HospitalID) REFERENCES Hospital(HospitalID)
);
''')

# Insert values into the 'Appointment' table
cursor.executemany('''
INSERT INTO Appointment (AppointmentID, PatientID, HospitalID, MedicalstaffID, Appointment_date, Notes) VALUES (?, ?, ?, ?, ?, ?);
''', [
    (536, 12, 306, 401, '2013-02-24', 'Unilateral primary osteoarthritis of first carpometacarpal joint'),
    (518, 1, 310, 413, '2017-06-11', 'Presence of (intrauterine) contraceptive device'),
    (596, 11, 311, 416, '2020-09-09', 'Nondisplaced osteochondral fracture of right patella'),
    (503, 15, 313, 425, '2019-08-12', 'Maternal care for disproportion due to outlet contraction of pelvis'),
    (521, 3, 323, 427, '2023-07-30', 'Nondisplaced avulsion fracture of left ischium'),
    (534, 8, 325, 430, '1989-07-01', 'Nondisplaced fracture of the posterior column of the right acetabulum'),
    (588, 6, 334, 446, '2020-01-23', 'Burn of the first degree of multiple sites of an unspecified wrist and hand'),
    (594, 13, 335, 451, '2021-02-15', 'Person boarding or alighting a three-wheeled motor vehicle injured'),
    (532, 14, 344, 455, '1923-12-12', 'Sprain of the interphalangeal joint of the right great toe'),
    (547, 9, 357, 480, '1998-04-17', 'Corrosion of unspecified degree of an unspecified site of the left lower limb'),
    (525, 10, 361, 465, '1999-08-20', 'Laceration of unspecified muscles, fascia, and tendons at forearm level'),
    (584, 7, 378, 481, '1965-03-23', 'Irritant contact dermatitis due to food in contact with skin'),
    (578, 4, 385, 488, '1947-08-15', 'Retinopathy of prematurity, stage 5'),
    (564, 2, 386, 493, '2022-06-19', 'Unspecified fracture of the shaft of the unspecified fibula')
])

# Create the 'MedicalRecord' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS MedicalRecord (
  MedicalRecordID integer PRIMARY KEY,
  PatientID integer,
  MedicalstaffID integer,
  MedicalRecord_date date,
  MedicalRecord_diagnosis varchar(100),
  MedicalRecord_treatment varchar(100),
  MedicalRecord_prescription varchar(100),
  FOREIGN KEY(PatientID) REFERENCES Patient(PatientID),
  FOREIGN KEY(MedicalstaffID) REFERENCES Medicalstaff(MedicalstaffID)
);
''')

# Insert values into the 'MedicalRecord' table
cursor.executemany('''
INSERT INTO MedicalRecord (MedicalRecordID, PatientID, MedicalstaffID, MedicalRecord_date, MedicalRecord_diagnosis, MedicalRecord_treatment, MedicalRecord_prescription) VALUES (?, ?, ?, ?, ?, ?, ?);
''', [
    (689, 7, 416, '2023-07-05', 'Colorectal Cancer', 'Cognitive Behavioral Therapy', 'Levothyroxine 50mcg'),
    (683, 15, 401, '2023-07-08', 'Coronary Artery Disease', 'Thrombolytics', 'Lipitor 40mg'),
    (649, 12, 488, '2023-04-09', 'Major Depressive Disorder', 'Antivirals', 'Lipitor 40mg'),
    (639, 10, 430, '2023-08-21', 'Borderline Personality Disorder', 'Dialysis', 'Warfarin 5mg'),
    (695, 8, 465, '2022-12-18', 'Obsessive-Compulsive Disorder', 'Radiation Oncology', 'Albuterol Inhaler'),
    (699, 1, 427, '2022-10-17', 'Schizophrenia', 'Statins', 'Lisinopril 10mg'),
    (668, 2, 427, '2023-05-10', 'Heart Failure', 'Medication Management', 'Lisinopril 10mg'),
    (663, 11, 493, '2023-04-17', 'Type 1 Diabetes', 'Antifungals', 'Sertraline 50mg'),
    (697, 11, 425, '2023-01-07', 'Gestational Diabetes', 'Antifungals', 'Ibuprofen 400mg'),
    (614, 10, 413, '2023-07-15', 'Diabetes', 'Radiation Oncology', 'Omeprazole 20mg'),
    (652, 15, 446, '2023-08-05', 'Tension Headache', 'Anticoagulants', 'Omeprazole 20mg'),
    (647, 1, 451, '2023-03-09', 'Migraine', 'Physical Therapy', 'Lipitor 40mg'),
    (637, 8, 455, '2022-10-24', 'Asthma', 'Physical Therapy', 'Omeprazole 20mg'),
    (655, 5, 480, '2022-12-23', 'Schizophrenia', 'Antiplatelet Agents', 'Amoxicillin 500mg'),
    (650, 6, 481, '2023-02-07', 'Multiple Sclerosis', 'Dialysis', 'Warfarin 5mg')
])


# Create the 'Billing' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS BILLING (
  BillingID integer PRIMARY KEY,
  PatientID integer,
  MedicalstaffID integer,
  AppointmentID integer,
  Billing_date date,
  Billing_amount integer,
  Billing_paymentstatus varchar(10),
  FOREIGN KEY(PatientID) REFERENCES Patient(PatientID),
  FOREIGN KEY(MedicalstaffID) REFERENCES Medicalstaff(MedicalstaffID),
  FOREIGN KEY(AppointmentID) REFERENCES Appointment(AppointmentID)
);
''')

# Insert values into the 'Billing' table
cursor.executemany('''
INSERT INTO BILLING (BillingID, PatientID, MedicalstaffID, AppointmentID, Billing_date, Billing_amount, Billing_paymentstatus) VALUES (?, ?, ?, ?, ?, ?, ?);
''', [
    (760, 10, 481, 518, '2023-09-14', '440.17', 'completed'),
    (774, 3, 488, 578, '2023-07-25', '758.43', 'completed'),
    (794, 1, 493, 594, '2023-07-21', '525.66', 'pending'),
    (766, 15, 480, 596, '2023-09-17', '307.88', 'pending'),
    (775, 10, 465, 518, '2023-07-11', '237.13', 'pending'),
    (715, 4, 455, 588, '2023-09-24', '144.18', 'pending'),
    (732, 3, 451, 564, '2023-07-18', '231.34', 'completed'),
    (724, 12, 446, 547, '2023-08-25', '935.54', 'completed'),
    (729, 2, 416, 578, '2023-07-25', '957.86', 'pending'),
    (780, 13, 430, 503, '2023-07-10', '124.26', 'pending'),
    (757, 9, 401, 521, '2023-10-05', '458.45', 'completed'),
    (762, 7, 488, 532, '2023-08-21', '898.91', 'pending'),
    (717, 2, 427, 534, '2023-07-14', '7.62', 'pending'),
    (703, 12, 425, 547, '2023-09-25', '924.09', 'completed')
])


# Create the 'Medication' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Medication (
  MedicationID integer PRIMARY KEY,
  Medication_name varchar(50),
  PatientID integer,
  MedicalstaffID integer,
  Medication_description text COMMENT 'Content of the post',
  Medication_instructions varchar(100),
  FOREIGN KEY(PatientID) REFERENCES Patient(PatientID),
  FOREIGN KEY(MedicalstaffID) REFERENCES Medicalstaff(MedicalstaffID)
);
''')

# Insert values into the 'Medication' table
cursor.executemany('''
INSERT INTO Medication (MedicationID, Medication_name, PatientID, MedicalstaffID, Medication_description, Medication_instructions) VALUES (?, ?, ?, ?, ?, ?);
''', [
    (835, 'Jakubowski', 6, 488, 'Octinoxate', 'Acetaminophen'),
    (804, 'Schiller-Kilback', 14, 493, 'Isopropyl Alcohol', 'Citalopram Hydrobromide'),
    (867, 'Mayert-Emmerich', 8, 413, 'Zinc Oxide and Octinoxate', 'Cocoa butter, Phenylephrine HCl, Shark liver oil'),
    (833, 'Hermann-Hudson', 15, 401,'amlodipine besylate', 'sweet potato'),
    (865, 'Kassulke and Sanford', 7, 451, 'Ethinyl estradiol', 'Air'),
    (844, 'Langworth-Crooks', 11, 455, 'Aluminum Zirconium', 'methylcellulose'),
    (894, 'Bechtelar Inc', 13, 465,'Benztropine Mesylate', 'Oxycodone and Aspirin'),
    (886, 'Konopelski-Wuckert', 11, 493, 'AZITHROMYCIN', 'Chaetomium'),
    (859, 'Connell and Anderson', 10, 430, 'Methyl Salicylate', 'Bambusa Aesculus'),
    (856, 'Mayer, Huel and Bailey', 7, 427, 'Thalidomide', 'MENTHOL'),
    (884, 'Rodriguez and Sons', 5, 425, 'Alcohol', 'AP and Deo'),
    (828, 'Bahringer Group', 4, 416,'Quetiapine fumarate', 'ribavirin'),
    (860, 'Bailey-Champlin', 2, 455,'CEFTRIAXONE', 'Benzalkonium'),
    (820, 'Connelly and Terry', 11, 413, 'Desipramine Hydrochloride', 'Metoprolol tartrate')
])


# Create the 'Labtest' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS LabTest (
  LabtestID integer PRIMARY KEY,
  PatientID integer,
  MedicalstaffID integer,
  Labtest_date date,
  Labtest_name varchar(100),
  Labtest_results varchar(100),
  Labtest_referencerange varchar(255),
  FOREIGN KEY(PatientID) REFERENCES Patient(PatientID),
  FOREIGN KEY(MedicalstaffID) REFERENCES Medicalstaff(MedicalstaffID)
);
''')

# Insert values into the 'Labtest' table
cursor.executemany('''
INSERT INTO LabTest (LabtestID, PatientID, MedicalstaffID, Labtest_date, Labtest_name, Labtest_results, Labtest_referencerange) VALUES (?, ?, ?, ?, ?, ?, ?);
''', [
    (954, 9, 425, '2023-9-27', 'X-ray', 'positive', '70 to 99 milligrams per deciliter Less than 200 mg-dL'),
    (957, 2, 451, '2023-9-9', 'Magnetic Resonance Imaging (MRI)', 'positive', '150,000 to 450,000 platelets per microliter'),
    (964, 6, 425, '2023-4-4', 'Thyroid Function Test (TFT)', 'negative', '12.0 to 16.0 grams per deciliter'),
    (969, 10, 480, '2023-2-14', 'Magnetic Resonance Imaging (MRI)', 'positive', '150,000 to 450,000 platelets per microliter'),
    (945, 9, 493, '2022-10-12', 'Computed Tomography (CT) Scan', 'negative', '12.0 to 16.0 grams per deciliter'),
    (941, 5, 401, '2023-4-16', 'Electroencephalogram (EEG)', 'positive', '4,500 to 11,000 cells per microliter'),
    (971, 6, 413, '2022-10-9', 'Liver Function Tests (LFTs)', 'negative', '12.0 to 16.0 grams per deciliter'),
    (956, 2, 416, '2022-11-7', 'Magnetic Resonance Imaging (MRI)', 'negative', '70 to 99 milligrams per deciliter Less than 200 mg-dL'),
    (992, 10, 446, '2022-11-19', 'Thyroid Function Test (TFT)', 'negative', '12.0 to 16.0 grams per deciliter'),
    (997, 7, 451, '2023-6-11', 'Magnetic Resonance Imaging (MRI)', 'positive', '150,000 to 450,000 platelets per microliter'),
    (959, 4, 427, '2023-1-2', 'Bone Density Scan (DEXA)', 'negative', '12.0 to 16.0 grams per deciliter'),
    (916, 13, 425, '2023-3-8', 'Liver Function Tests (LFTs)', 'negative', '70 to 99 milligrams per deciliter Less than 200 mg-dL'),
    (999, 14, 480, '2023-7-30', 'Computed Tomography (CT) Scan', 'negative', '70 to 99 milligrams per deciliter Less than 200 mg-dL'),
    (944, 15, 430, '2023-9-13', 'Electroencephalogram (EEG)', 'positive', '4,500 to 11,000 cells per microliter'),
    (936, 2, 455, '2022-11-21', 'Thyroid Function Test (TFT)', 'positive', '12.0 to 16.0 grams per deciliter')
])

conn.commit()
conn.close()

