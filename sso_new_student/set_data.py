from pathlib import Path
import pandas as pd

# # Function to get a valid input from the user and convert it to uppercase
# def get_input(prompt, options):
#     while True:
#         value = input(f"{prompt} ({', '.join(options)}): ").upper()
#         if value in options:
#             return value
#         else:
#             print(f"Invalid input. Please choose from {options}.")
#
# # Options for input
# campus_options = ['EMC', 'IDC', 'KBC', 'MFC']
# year_options = ['6', '7', '8', '9', '10', '11']
# cg_options = ['N5', 'N4', 'N3', 'N2']
#
# # User inputs with predefined options
# campus = get_input("Select future campus", campus_options)
# stu_id = input("Enter Student ID: ")
# y = get_input("Select current year level", year_options)
# cg = get_input("Select CG", cg_options)


def make_dataframe(
        campus: str,
        stu_id: str,
        y: str,
        cg: str,
        output_directory: Path
        ) -> dict[str, pd.DataFrame]:




    # .........................................................................
    # Data  ...................................................................
    # .........................................................................

    # Define the columns
    columns = [
        'StuID', 'ACOMU12', 'ACPU12', 'AENG', 'AMAT1', 'AMAT2', 'ARA', 'ARA1', 'ARA2', 'ARA3',
        'ARDE', 'ATUR', 'ATUR1', 'ATUR2', 'ATUR3', 'BIOU12', 'BIOU34', 'BMU12', 'BMU34', 'CART',
        'CC', 'CERT2WS', 'CG', 'CHEU12', 'DATAU34', 'DEBRO', 'DES', 'DESIL', 'DIG', 'DPS', 'DRA1',
        'DRA2', 'DRA3', 'DRPA', 'EB', 'ECOU12', 'ELANU12', 'ENG', 'ENG1', 'ENG2', 'ENG3', 'ENG4',
        'ENGU12', 'FATT', 'FI', 'FP', 'FRE', 'FRE3', 'FT', 'GMATU12', 'GMATU34', 'GRDE', 'HHDU12',
        'HHDU34', 'HIS1', 'HIS2', 'HISU12', 'HPE', 'HPE1', 'HPE2', 'HPE3', 'HPE4', 'HUM', 'HUM1',
        'HUM2', 'IMAT1', 'IMAT2', 'IMAT3', 'INN', 'LEGU12', 'LITU12', 'LTR', 'MAT', 'MAT1', 'MAT2',
        'MATMU12', 'MED', 'MUS1', 'MUS2', 'MUS3', 'NUM', 'PART', 'PEU12', 'PHO', 'PHYU12', 'PRO',
        'PSYU12', 'PSYU34', 'RMAT', 'ROB1', 'ROB2', 'RS', 'RSC1', 'RSC2', 'RSCI2', 'RSPO', 'RV',
        'RV1', 'RV2', 'RV3', 'SCI1', 'SCI2', 'SCI3', 'SCI4', 'SCME', 'SCPR', 'SDEVU34', 'SMATU12',
        'STEM', 'SVF', 'TEX', 'TUR', 'TUR1', 'TUR2', 'TUR3', 'TURU12', 'TURU34', 'VA1', 'VA2',
        'VCDU12', 'WDCS', 'XAINN', 'Y'
    ]

    # Create an empty DataFrame with the specified columns
    res = pd.DataFrame(columns=columns)




    # # For testing
    # campus = 'EMC'
    # stu_id = '38000'
    # y = '11'
    # cg = 'N5'

    # Create a dictionary for the new row
    new_row = {
        'StuID': stu_id,
        'Y': int(y),
        'CG': cg
    }

    # Convert the dictionary to a DataFrame
    new_row_df = pd.DataFrame([new_row], columns=columns)

    # Use concat to add the new row to the DataFrame
    res = pd.concat([res, new_row_df], ignore_index=True)

    res.fillna('', inplace=True)

    # # Display the DataFrame
    # print(res)



    # Define the columns
    columns = [
        'Student ID', 'Name', 'Campus', 'Current Year', 'CG',
        'Accounting U12', 'Accounting U34', 'Advanced English',
        'Advanced Mathematics 1', 'Advanced Mathematics 2', 'Applied Computing U12',
        'Arabic 1', 'Arabic 2', 'Arabic 3', 'Architecture and Design',
        'Art Creative Practice U12', 'Art Creative Practice U34', 'Biology U12',
        'Biology U34', 'Business Management U12', 'Business Management U34',
        'Certificate II in Workplace Skills', 'Chemistry U12', 'Chemistry U34',
        'Civics and Citizenship', 'Data Analytics U34', 'Debating and Public Speaking',
        'Design and Technologies', 'Digital Technologies', 'Drama 1', 'Drama 2',
        'Drama 3', 'Drama U12', 'Drama U34', 'Drawing and Painting',
        'Duke of Edinburgh', 'Economics and Business', 'Economics U12',
        'Economics U34', 'English 1', 'English 2', 'English 3', 'English 4',
        'English Language U12', 'English Language U34', 'English U12',
        'English U34', 'Extended Mathematics', 'Fashion and Textile Trends',
        'Food and the Food Industry', 'Food Technology', 'General Mathematics U12',
        'General Mathematics U34', 'Geography 1', 'Geography 2', 'Graphic Design',
        'Health and Human Development U12', 'Health and Human Development U34',
        'Health and Physical Education 1', 'Health and Physical Education 2',
        'Health and Physical Education 3', 'Health and Physical Education 4',
        'History 1', 'History 2', 'History U12', 'History U34', 'Humanities 1',
        'Humanities 2', 'Humanities Inquiries 1', 'Innovation',
        'Intermediate Mathematics 1', 'Intermediate Mathematics 2',
        'Intermediate Mathematics 3', 'Legal Studies U12', 'Legal Studies U34',
        'Literacy Foundations 1', 'Literacy Foundations 2', 'Literacy Foundations 3',
        'Literacy Foundations 4', 'Literature U12', 'Literature U34',
        'Mathematical Methods U12', 'Mathematical Methods U34', 'Mathematics 1',
        'Mathematics 2', 'Media', 'Music 1', 'Music 2', 'Music 3',
        'Numeracy Foundations 1', 'Numeracy Foundations 2', 'Numeracy Foundations 3',
        'Numeracy Foundations 4', 'Photography', 'Physical Education U12',
        'Physical Education U34', 'Physics U12', 'Physics U34', 'Programming',
        'Psychology U12', 'Psychology U34', 'Recreational Fitness',
        'Recreational Mathematics', 'Religion and Values 1', 'Religion and Values 2',
        'Religion and Values 3', 'Religion Studies', 'Research Science 1',
        'Research Science 2', 'Robotics 1', 'Robotics 2', 'Science 1',
        'Science 2', 'Science 3', 'Science 4', 'Screen and Media',
        'Sculpture and Printmaking', 'Social Values in Film', 'Software Development U34',
        'Specialist Mathematics U12', 'Specialist Mathematics U34',
        'Texts and Traditions U12', 'Textiles', 'Turkish 1', 'Turkish 2',
        'Turkish 3', 'Turkish 4', 'Turkish 5', 'Turkish 6', 'Turkish 7',
        'Turkish U12', 'Turkish U34', 'VCE VET Business U12',
        'VCE VET Sport and Recreation U12', 'Visual Arts 1', 'Visual Arts 2',
        'Visual Communication Design U12', 'Visual Communication Design U34',
        'Volunteering Skills', 'Web Design and Cyber Security'
    ]

    # Create an empty DataFrame with the specified columns
    df = pd.DataFrame(columns=columns)

    # Create a dictionary for the new row
    new_row2 = {
        'Student ID': stu_id,
        'Name': 'new student',
        'Campus': campus,
        'Current Year': int(y),
        'CG': cg
    }

    # Convert the dictionary to a DataFrame
    new_row2_df = pd.DataFrame([new_row2], columns=columns)

    # Use concat to add the new row to the DataFrame
    df = pd.concat([df, new_row2_df], ignore_index=True)

    # Ensure all other columns are set to NaN where data is not provided
    df = df.reindex(columns=columns)

    # # Display the DataFrame
    # print(df)


    # .........................................................................
    # Definitions .............................................................
    # .........................................................................
    new5 = res['CG'].isin(['N5'])
    new4 = res['CG'].isin(['N4','N5'])
    new3 = res['CG'].isin(['N3','N4','N5'])
    new = res['CG'].isin(['N2','N3','N4','N5'])
    cgtop3 = res['CG'].isin(['B+','A','A+'])
    cgtop4 = res['CG'].isin(['B','B+','A','A+'])
    y6 = (res['Y'] == 6)
    y7 = (res['Y'] == 7)
    y8 = (res['Y'] == 8)
    y9 = (res['Y'] == 9)
    y10 = (res['Y'] == 10)
    y11 = (res['Y'] == 11)
    y12 = (res['Y'] == 12)
    early_VCE = (res['Y'] == 9) & ((res['CG'].isin(['D+','C','C+','B','B+','A','A+'])) | new3)
    early_VCE_high = (res['Y'] == 9) & ((res['CG'].isin(['A','A+'])) | new5)
    art_high = (res['Y'] == 9) & res['CG'].isin(['B+','A','A+']) & ((res['ARDE'].isin(['A','A+'])) | (res['DRPA'].isin(['A','A+'])) | (res['GRDE'].isin(['A','A+'])) | (res['PHO'].isin(['A','A+'])) | (res['SCME'].isin(['A','A+'])) | (res['SCPR'].isin(['A','A+'])))
    hum_high = (res['Y'] == 9) & res['CG'].isin(['B+','A','A+']) & ((res['HIS1'].isin(['A','A+'])) | (res['RV3'].isin(['A','A+'])) | (res['EB'].isin(['A','A+'])))
    mat_high = (res['Y'] == 9) & res['CG'].isin(['B+','A','A+']) & ((res['AMAT1'].isin(['A+'])) | new5)
    sci_high = (res['Y'] == 9) & res['CG'].isin(['B+','A','A+']) & ((res['RSC1'].isin(['A','A+'])) | new5)
    pe_high = (res['Y'] == 9) & res['CG'].isin(['B+','A','A+']) & ((res['HPE3'].isin(['A','A+'])) | (res['DEBRO'].isin(['A','A+'])) | (res['DESIL'].isin(['A','A+'])) | (res['FP'].isin(['A','A+'])) | (res['RSPO'].isin(['A','A+'])))
    mat_high10 = (res['Y'] == 10) & ((res['IMAT2'].isin(['A+']) & (res['IMAT3'] == 'S2')) | (res['AMAT2'].isin(['B+','A','A+'])))
    mat_mid10 = (res['Y'] == 10) & ((res['IMAT2'].isin(['C+','B','B+','A','A+']) & (res['IMAT3'] == 'S2')) | (res['AMAT2'].isin(['C+','B','B+','A','A+'])))
    # both below contains extra 3 OR's
    sci_mid10 = (res['Y'] == 10) & ((res['SCI4'].isin(['C+','B','B+','A','A+'])) | (res['RSC1'].isin(['C+','B','B+','A','A+'])) | res['BIOU12'].isin(['B+','A','A+']) | res['PSYU12'].isin(['B+','A','A+']))
    sci_min10 = (res['Y'] == 10) & ((res['SCI4'].isin(['C','C+','B','B+','A','A+'])) | (res['RSC1'].isin(['C','C+','B','B+','A','A+'])) | res['BIOU12'].isin(['B+','A','A+']) | res['PSYU12'].isin(['B+','A','A+']))



    # .........................................................................
    # Year 7 ..................................................................
    # .........................................................................
    mask = y6
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Design and Technologies'] = df['Student ID'].isin(valid_students).astype(int)
    df['Digital Technologies'] = df['Student ID'].isin(valid_students).astype(int)
    df['Drama 1'] = df['Student ID'].isin(valid_students).astype(int)
    df['English 1'] = df['Student ID'].isin(valid_students).astype(int)
    df['Health and Physical Education 1'] = df['Student ID'].isin(valid_students).astype(int)
    df['Humanities 1'] = df['Student ID'].isin(valid_students).astype(int)
    df['Mathematics 1'] = df['Student ID'].isin(valid_students).astype(int)
    df['Music 1'] = df['Student ID'].isin(valid_students).astype(int)
    df['Religion and Values 1'] = df['Student ID'].isin(valid_students).astype(int)
    df['Science 1'] = df['Student ID'].isin(valid_students).astype(int)
    df['Visual Arts 1'] = df['Student ID'].isin(valid_students).astype(int)

    # print(len(valid_students))

    mask = y6 & ((res['ARA'].isin(['C5','C4','C3','C2','C1','B2','B1','A'])) | new)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Arabic 1'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (y6 | y7 | y8) & new
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Turkish 1'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (y6 & (res['TUR'] != '')) | (y7 & (res['TUR1'] != ''))
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Turkish 2'] = df['Student ID'].isin(valid_students).astype(int)

    mask = y6 & (res['ATUR'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Turkish 5'] = df['Student ID'].isin(valid_students).astype(int)

    # print(len(valid_students))
    # df.columns[df.isna().all()].tolist()

    # .........................................................................
    # Year 8 ..................................................................
    # .........................................................................
    mask = y7
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Drama 2'] = df['Student ID'].isin(valid_students).astype(int)
    df['English 2'] = df['Student ID'].isin(valid_students).astype(int)
    df['Food Technology'] = df['Student ID'].isin(valid_students).astype(int)
    df['Health and Physical Education 2'] = df['Student ID'].isin(valid_students).astype(int)
    df['Humanities 2'] = df['Student ID'].isin(valid_students).astype(int)
    df['Mathematics 2'] = df['Student ID'].isin(valid_students).astype(int)
    df['Media'] = df['Student ID'].isin(valid_students).astype(int)
    df['Music 2'] = df['Student ID'].isin(valid_students).astype(int)
    df['Programming'] = df['Student ID'].isin(valid_students).astype(int)
    df['Religion and Values 2'] = df['Student ID'].isin(valid_students).astype(int)
    df['Robotics 1'] = df['Student ID'].isin(valid_students).astype(int)
    df['Science 2'] = df['Student ID'].isin(valid_students).astype(int)
    df['Textiles'] = df['Student ID'].isin(valid_students).astype(int)
    df['Visual Arts 2'] = df['Student ID'].isin(valid_students).astype(int)

    # print(len(valid_students))

    mask = (res['ARA1'] != '') | (y7 & new)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Arabic 2'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['ATUR1'] != '') & y7
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Turkish 6'] = df['Student ID'].isin(valid_students).astype(int)

    # print(len(valid_students))
    # df.columns[df.isna().all()].tolist()


    # .........................................................................
    # Year 9 ..................................................................
    # .........................................................................
    mask = y8
    valid_students = res.loc[mask, 'StuID'].unique()
    df['English 3'] = df['Student ID'].isin(valid_students).astype(int)
    df['Health and Physical Education 3'] = df['Student ID'].isin(valid_students).astype(int)
    df['History 1'] = df['Student ID'].isin(valid_students).astype(int)
    df['Intermediate Mathematics 1'] = df['Student ID'].isin(valid_students).astype(int)
    df['Religion and Values 3'] = df['Student ID'].isin(valid_students).astype(int)
    df['Science 3'] = df['Student ID'].isin(valid_students).astype(int)

    mask = y8 & ((res['MAT2'].isin(['A','A+'])) | new5)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Advanced Mathematics 1'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['ARA2'] != '') | (y8 & new)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Arabic 3'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['ARDE'] == '') & (y8 | y9)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Architecture and Design'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['CC'] == '') & (y8 | y9)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Civics and Citizenship'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['DPS'] == '') & (y8 | y9)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Debating and Public Speaking'] = df['Student ID'].isin(valid_students).astype(int)

    mask = y8 | y9
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Drama 3'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['DRPA'] == '') & (y8 | y9)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Drawing and Painting'] = df['Student ID'].isin(valid_students).astype(int)

    mask = y8 | y9
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Duke of Edinburgh'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['EB'] == '') & (y8 | y9)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Economics and Business'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['FATT'] == '') & (y8 | y9)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Fashion and Textile Trends'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['FI'] == '') & (y8 | y9)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Food and the Food Industry'] = df['Student ID'].isin(valid_students).astype(int)

    mask = y8 | y9 # to be used for 2026 | (res['GEO1'] == '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Geography 1'] = df['Student ID'].isin(valid_students).astype(int)

    # mask = (res['GEO2'] == '') & (y8 | y9)
    # valid_students = res.loc[mask, 'StuID'].unique()
    # df['Geography 2'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['GRDE'] == '') & (y8 | y9)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Graphic Design'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['INN'] == '') & (y8 | y9)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Innovation'] = df['Student ID'].isin(valid_students).astype(int)

    mask = y8 | y9
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Music 3'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['PHO'] == '') & (y8 | y9)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Photography'] = df['Student ID'].isin(valid_students).astype(int)

    mask = y8 | y9
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Recreational Fitness'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['RMAT'] == '') & (y8 | y9)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Recreational Mathematics'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (y8 & ((res['SCI2'].isin(['B+','A','A+'])) | new4)) | (y9 & ((res['SCI3'].isin(['C','C+','B','B+','A','A+'])) | new4))
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Research Science 1'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (y8 & ((res['SCI2'].isin(['B+','A','A+'])) | new4))
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Research Science 2'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['ROB2'] == '') & (y8 | y9)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Robotics 2'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['SCME'] == '') & (y8 | y9)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Screen and Media'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['SCPR'] == '') & (y8 | y9)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Sculpture and Printmaking'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['SVF'] == '') & (y8 | y9)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Social Values in Film'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['TUR2'] != '') & y8
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Turkish 3'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['ATUR2'] != '') & y8
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Turkish 7'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (y8 | y9) #2026 onwards (res['VS'] == '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Volunteering Skills'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['WDCS'] == '') & (y8 | y9)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Web Design and Cyber Security'] = df['Student ID'].isin(valid_students).astype(int)

    # print(len(valid_students))
    # df.columns[df.isna().all()].tolist()


    # .........................................................................
    # Year 10 .................................................................
    # .........................................................................

    mask = y9
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Certificate II in Workplace Skills'] = df['Student ID'].isin(valid_students).astype(int)
    df['English 4'] = df['Student ID'].isin(valid_students).astype(int)
    df['Health and Physical Education 4'] = df['Student ID'].isin(valid_students).astype(int)
    df['History 2'] = df['Student ID'].isin(valid_students).astype(int)
    df['Intermediate Mathematics 2'] = df['Student ID'].isin(valid_students).astype(int)
    df['Intermediate Mathematics 3'] = df['Student ID'].isin(valid_students).astype(int)
    df['Religion Studies'] = df['Student ID'].isin(valid_students).astype(int)
    df['Science 4'] = df['Student ID'].isin(valid_students).astype(int)

    # print(len(valid_students))

    mask = y9 & (((res['ENG3'].isin(['B','B+','A','A+'])) & cgtop4) | new4)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Advanced English'] = df['Student ID'].isin(valid_students).astype(int)

    mask = y9 & ((res['AMAT1'].isin(['C','C+','B','B+','A','A+'])) | (res['IMAT1'].isin(['A','A+'])) | new5)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Advanced Mathematics 2'] = df['Student ID'].isin(valid_students).astype(int)

    mask = y9 & ((res['AMAT1'].isin(['C','C+','B','B+','A','A+'])) | (res['IMAT1'].isin(['A','A+'])) | new5)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Extended Mathematics'] = df['Student ID'].isin(valid_students).astype(int)

    # print(len(valid_students))
    # df.columns[df.isna().all()].tolist()


    # .........................................................................
    # Unit 1-2 ................................................................
    # .........................................................................
    mask = y10
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Drama U12'] = df['Student ID'].isin(valid_students).astype(int)
    df['English Language U12'] = df['Student ID'].isin(valid_students).astype(int)
    df['English U12'] = df['Student ID'].isin(valid_students).astype(int)
    df['General Mathematics U12'] = df['Student ID'].isin(valid_students).astype(int)
    df['Literature U12'] = df['Student ID'].isin(valid_students).astype(int)
    df['VCE VET Business U12'] = df['Student ID'].isin(valid_students).astype(int)
    df['VCE VET Sport and Recreation U12'] = df['Student ID'].isin(valid_students).astype(int)

    mask = y10 | early_VCE_high | art_high
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Art Creative Practice U12'] = df['Student ID'].isin(valid_students).astype(int)
    df['Visual Communication Design U12'] = df['Student ID'].isin(valid_students).astype(int)

    mask = y10 | early_VCE_high | hum_high
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Accounting U12'] = df['Student ID'].isin(valid_students).astype(int)
    df['Economics U12'] = df['Student ID'].isin(valid_students).astype(int)
    df['History U12'] = df['Student ID'].isin(valid_students).astype(int)
    df['Legal Studies U12'] = df['Student ID'].isin(valid_students).astype(int)
    df['Texts and Traditions U12'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (y10 & (sci_mid10 | new4)) | (early_VCE_high & sci_high) | (new5 & (y9 | y10)) #increased RSC1 cutoff
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Chemistry U12'] = df['Student ID'].isin(valid_students).astype(int)
    df['Physics U12'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['ACOMU12'] == '') & (y10 | early_VCE)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Applied Computing U12'] = df['Student ID'].isin(valid_students).astype(int)

    #cgtop4 is used instead of cgtop3
    mask = (y9 & cgtop4 & ((res['SCI3'].isin(['B+','A','A+'])) | (res['RSC1'] != ''))) | (y9 & new4) | (y10 & new4) | (y10 & sci_min10 & (res['BIOU12'] == ''))
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Biology U12'] = df['Student ID'].isin(valid_students).astype(int)

    #Humanities elective condition for early entry removed
    mask = (res['BMU12'] == '') & (y10 | early_VCE)
    # mask = (res['BMU12'] == '') & (y10 | (y9 & new4) | (early_VCE & ((res['CC'] != '') | (res['EB'] != '')))) # to be used for 2026 | (res['GEO1'] != '') | (res['GEO2'] != '')))
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Business Management U12'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['HHDU12'] == '') & (y10 | early_VCE)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Health and Human Development U12'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (y10 & (mat_mid10 | new4)) | (early_VCE_high & mat_high) | (new5 & (y9 | y10)) #increased IMAT2 cutoff
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Mathematical Methods U12'] = df['Student ID'].isin(valid_students).astype(int)

    mask = y10 | early_VCE_high | pe_high
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Physical Education U12'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (y9 & cgtop4 & ((res['SCI3'].isin(['B','B+','A','A+'])) | (res['RSC1'] != ''))) | (y9 & new4) | (y10 & new4) | (y10 & sci_min10 & (res['PSYU12'] == ''))
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Psychology U12'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (y10 & (mat_high10 | new4)) | (early_VCE_high & mat_high) | (new5 & (y9 | y10))
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Specialist Mathematics U12'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (y9 | y10) & (res['ATUR3'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Turkish U12'] = df['Student ID'].isin(valid_students).astype(int)

    # print(len(valid_students))
    # df.columns[df.isna().all()].tolist()

    # .........................................................................
    # Unit 3-4 ................................................................
    # .........................................................................
    # mask = (res['ACCU12'] != '')
    # valid_students = res.loc[mask, 'StuID'].unique()
    # df['Accounting U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['ACPU12'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Art Creative Practice U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['BIOU12'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Biology U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['BMU12'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Business Management U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['CHEU12'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Chemistry U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['ACOMU12'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Data Analytics U34'] = df['Student ID'].isin(valid_students).astype(int)
    df['Software Development U34'] = df['Student ID'].isin(valid_students).astype(int)

    # mask = (res['DRAU12'] != '')
    # valid_students = res.loc[mask, 'StuID'].unique()
    # df['Drama U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['ECOU12'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Economics U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['ELANU12'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['English Language U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['ENGU12'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['English U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['GMATU12'] != '') | ((res['IMAT2'].isin(['B+','A','A+'])) & (res['IMAT3'] != '')) | ( res['AMAT2'].isin(['C+','B','B+','A','A+'])) | (y10 & new4)
    valid_students = res.loc[mask, 'StuID'].unique()
    df['General Mathematics U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['HHDU12'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Health and Human Development U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['HISU12'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['History U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['LEGU12'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Legal Studies U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['LITU12'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Literature U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['MATMU12'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Mathematical Methods U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['PEU12'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Physical Education U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['PHYU12'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Physics U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['PSYU12'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Psychology U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['SMATU12'] != '') | (res['MATMU12'].isin(['B+','A','A+']))
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Specialist Mathematics U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['TURU12'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Turkish U34'] = df['Student ID'].isin(valid_students).astype(int)

    mask = (res['VCDU12'] != '')
    valid_students = res.loc[mask, 'StuID'].unique()
    df['Visual Communication Design U34'] = df['Student ID'].isin(valid_students).astype(int)

    # .........................................................................
    # Sheet Export ............................................................
    # .........................................................................


    df_melted = df.melt(id_vars=df.columns[:5], value_vars=df.columns[5:], var_name='Eligible Subject', value_name='Value')
    df_filtered = df_melted[df_melted['Value'] == 1]
    dfeligible = df_filtered.drop(columns='Value')
    dfeligible = dfeligible.reset_index(drop=True)
    # dfeligible

    # In Google colab dfeligible is empty, however results has 31 rows. In a local Python install both results and dfeligible are empty. Explain why this is ocurring and how it can be fixed AI?
    results = dfeligible.copy()
    results['PreReqResult'] = ''
    results = results.rename(columns={'Student ID': 'StudentCode', 'Eligible Subject': 'PreReqCode'})

    # Add Y
    new_rows = results[['StudentCode', 'Campus', 'Current Year']].drop_duplicates().copy()
    new_rows['PreReqCode'] = 'Y'
    new_rows['PreReqResult'] = new_rows['Current Year']

    # Add CG
    cg_rows = results[['StudentCode', 'Campus', 'CG']].drop_duplicates().copy()
    cg_rows['PreReqCode'] = 'CG'
    cg_rows['PreReqResult'] = cg_rows['CG']

    # Combine the DataFrames
    new_rows = pd.concat([new_rows, cg_rows], ignore_index=True)

    results = pd.concat([results, new_rows], ignore_index=True)
    results_sorted = results.sort_values(by='StudentCode', ascending=True)
    results_sorted['PreReqCode'] = results_sorted['PreReqCode'].str.replace(' ', '', regex=False)

    campuses = results_sorted['Campus'].unique()

    dfs = {}

    print(campuses)
    for campus in campuses:
        df_campus = results_sorted[results_sorted['Campus'] == campus]
        df_campus = df_campus.drop(columns=['Name', 'Campus', 'Current Year', 'CG'])
        dfs[f'newresults{campus}'] = df_campus



    # for campus, df_campus in dfs.items():
    #     filename = output_directory / f'{campus}.csv'  # File name for the CSV
    #     df_campus.to_csv(filename, index=False)  # Save the DataFrame as a CSV file

    return dfs
