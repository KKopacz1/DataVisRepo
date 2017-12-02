import os
import csv
import pandas as pd 

#Grab info
file = 'employee_data1.csv'
employee_data = pd.read_csv(file)

#split names into new columns
employee_data['First Name'], employee_data['Second Name'] = zip(*employee_data['Name'].map(lambda x: x.split(' ')))

#change date
employee_data['DOB'] = pd.to_datetime(employee_data['DOB']).apply(lambda x: x.strftime('%d/%m/%Y'))

#change state names
employee_data.loc[employee_data['State'] == 'Alabama', 'State'] = "AL"
employee_data.loc[employee_data['State'] == 'Alaska', 'State'] = "AK"
employee_data.loc[employee_data['State'] == 'Arizona', 'State'] = "AZ"
employee_data.loc[employee_data['State'] == 'Arkansas', 'State'] = "AR"
employee_data.loc[employee_data['State'] == 'California', 'State'] = "CA"
employee_data.loc[employee_data['State'] == 'Colorado', 'State'] = "CO"
employee_data.loc[employee_data['State'] == 'Connecticut', 'State'] = "CT"
employee_data.loc[employee_data['State'] == 'Delaware', 'State'] = "DE"
employee_data.loc[employee_data['State'] == 'Florida', 'State'] = "FL"
employee_data.loc[employee_data['State'] == 'Georgia', 'State'] = "GA"
employee_data.loc[employee_data['State'] == 'Hawaii', 'State'] = "HI"
employee_data.loc[employee_data['State'] == 'Idaho', 'State'] = "ID"
employee_data.loc[employee_data['State'] == 'Illinois', 'State'] = "IL"
employee_data.loc[employee_data['State'] == 'Indiana', 'State'] = "IN"
employee_data.loc[employee_data['State'] == 'Iowa', 'State'] = "IA"
employee_data.loc[employee_data['State'] == 'Kansas', 'State'] = "KS"
employee_data.loc[employee_data['State'] == 'Kentucky', 'State'] = "KY"
employee_data.loc[employee_data['State'] == 'Louisiana', 'State'] = "LA"
employee_data.loc[employee_data['State'] == 'Maine', 'State'] = "ME"
employee_data.loc[employee_data['State'] == 'Maryland', 'State'] = "MD"
employee_data.loc[employee_data['State'] == 'Massachusetts', 'State'] = "MA"
employee_data.loc[employee_data['State'] == 'Michigan', 'State'] = "MI"
employee_data.loc[employee_data['State'] == 'Minnesota', 'State'] = "MN"
employee_data.loc[employee_data['State'] == 'Missisippi', 'State'] = "MI"
employee_data.loc[employee_data['State'] == 'Missouri', 'State'] = "MO"
employee_data.loc[employee_data['State'] == 'Montana', 'State'] = "MT"
employee_data.loc[employee_data['State'] == 'Nebraska', 'State'] = "NE"
employee_data.loc[employee_data['State'] == 'Nevada', 'State'] = "NV"
employee_data.loc[employee_data['State'] == 'New Hampshire', 'State'] = "NH"
employee_data.loc[employee_data['State'] == 'New Jersey', 'State'] = "NJ"
employee_data.loc[employee_data['State'] == 'New Mexico', 'State'] = "NM"
employee_data.loc[employee_data['State'] == 'New York', 'State'] = "NY"
employee_data.loc[employee_data['State'] == 'North Carolina', 'State'] = "NC"
employee_data.loc[employee_data['State'] == 'North Dakota', 'State'] = "ND"
employee_data.loc[employee_data['State'] == 'Ohio', 'State'] = "OH"
employee_data.loc[employee_data['State'] == 'Oklahoma', 'State'] = "OK"
employee_data.loc[employee_data['State'] == 'Oregon', 'State'] = "OR"
employee_data.loc[employee_data['State'] == 'Pennsylvania', 'State'] = "PA"
employee_data.loc[employee_data['State'] == 'Rhode Island', 'State'] = "RI"
employee_data.loc[employee_data['State'] == 'South Carolina', 'State'] = "SC"
employee_data.loc[employee_data['State'] == 'South Dakota', 'State'] = "SD"
employee_data.loc[employee_data['State'] == 'Tennessee', 'State'] = "TN"
employee_data.loc[employee_data['State'] == 'Texas', 'State'] = "TX"
employee_data.loc[employee_data['State'] == 'Utah', 'State'] = "UT"
employee_data.loc[employee_data['State'] == 'Vermont', 'State'] = "VT"
employee_data.loc[employee_data['State'] == 'Virginia', 'State'] = "VA"
employee_data.loc[employee_data['State'] == 'Washington', 'State'] = "WA"
employee_data.loc[employee_data['State'] == 'West Virginia', 'State'] = "WV"
employee_data.loc[employee_data['State'] == 'Wisconsin', 'State'] = "WI"
employee_data.loc[employee_data['State'] == 'Wyoming', 'State'] = "WY"

#update SSN
updated_SSN = employee_data['SSN'].str[-4:]
employee_data['SSN'] = "*** - ** - " + updated_SSN

# delete name column
del employee_data['Name']

print(employee_data)