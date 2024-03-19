import streamlit as st
import numpy as np
import joblib

clf = joblib.load('rf_classifier')



features = ['country', 'year', 'location_type', 'cellphone_access',
       'household_size', 'age_of_respondent', 'gender_of_respondent',
       'relationship_with_head', 'marital_status', 'education_level',
       'job_type']


# with st.sidebar:
#     for i in features:
#         st.number_input(i, 2,10)

st.title('Customer Churn Predictor by  Green White Broods')

st.image('Examine.png', width=300)

test_features = []
with st.sidebar:
    country = st.selectbox('Choose The country value', ['Rwanda', 'Uganda','Tanzania','Kenya'])
    if country == 'Rwanda':
       test_features.append(1)
    elif country == 'Tanzania':
       test_features.append(2)
    elif country == 'Kenya':
       test_features.append(0)
    elif country == 'Uganda':
       test_features.append(3)
    
    year = st.selectbox('Year', [2016, 2017, 2018])
    test_features.append(year)

    location_type = st.selectbox('Choose your preffered location', ['Rural', 'Urban'])
    if location_type == 'Rural':
       test_features.append(0)
    else:
       test_features.append(1)
       
    cellphone_access = st.selectbox('Access to Cell Phone',['Yes', 'No'])
    if cellphone_access == 'Yes':
       test_features.append(1)
    else:
       test_features.append(0)


    household_size = st.number_input('Enter the size of your House hold', 1,9)
    test_features.append(household_size)


    age_of_respondent = st.number_input('Enter the age of respondents', 16,81)
    test_features.append(age_of_respondent)


    gender_of_respondent = st.selectbox('Gender',['Male', 'Female'])
    if gender_of_respondent == 'Male':
       test_features.append(1)
    else:
       test_features.append(0)

    relationship = {'Head of Household': 1,
                    'Spouse': 5,
                    'Child': 0,
                    'Parent': 4,
                    'Other relative': 3,
                    'Other non-relatives': 2}
    relationship_with_head = st.selectbox("What's your  relationship with the head?", [x for x in relationship.keys()])
    test_features.append(relationship[relationship_with_head])
    
    status = {'Married/Living together': 2,
              'Single/Never Married': 3,
              'Widowed': 4,
              'Divorced/Seperated': 0,
              'Dont know': 1}
    marital_status  = st.selectbox("What is your marital status? ", [x for x in status.keys()])
    test_features.append(status[marital_status])


    edu = {'Primary education': 2,
           'No formal education': 0,
           'Secondary education': 3,
           'Tertiary education': 4,
           'Vocational/Specialised training': 5,
           'Other/Dont know/RTA': 1}
    
    educational_level = st.selectbox("What is your Educational Level? ", [x for x in edu.keys()])
    test_features.append(edu[educational_level])

    jobs = {'Self employed': 9,
            'Informally employed': 5,
            'Farming and Fishing': 1,
            'Remittance Dependent': 8,
            'Formally employed Private': 3,
            'Other Income': 7,
            'No Income': 6,
            'Formally employed Government': 2,
            'Government Dependent': 4,
            'Dont Know/Refuse to answer': 0
            }
    
    job_type = st.selectbox("What is your Job type", [x for x in jobs.keys()])
    test_features.append(jobs[job_type])

user_input = np.array(test_features)

if st.button('Predict'):
   Prediction = clf.predict(user_input.reshape(1,-1))
   if Prediction == 0:
      st.write('No')
   else:
      st.success('Yes')

def add(a,b):
   result = a+ b
   return result


    