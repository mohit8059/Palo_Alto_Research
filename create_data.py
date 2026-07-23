import pandas as pd

# Original Data URL or path
data = {
    'Department': ['R&D', 'Sales', 'HR', 'R&D', 'Sales'] * 294,
    'OverTime': ['Yes', 'No', 'Yes', 'No', 'Yes'] * 294,
    'WorkLifeBalance': [1, 3, 2, 4, 2] * 294,
    'JobInvolvement': [2, 3, 4, 1, 3] * 294,
    'JobSatisfaction': [3, 4, 2, 3, 4] * 294,
    'EnvironmentSatisfaction': [2, 4, 3, 2, 3] * 294,
    'RelationshipSatisfaction': [4, 3, 2, 1, 3] * 294,
    'Attrition': [1, 0, 1, 0, 0] * 294
}

df = pd.DataFrame(data)
# Calculate Engagement Index
cols = ['JobInvolvement', 'JobSatisfaction', 'EnvironmentSatisfaction', 'RelationshipSatisfaction']
df['Engagement_Index'] = df[cols].mean(axis=1)
# Calculate Burnout Risk
df['Burnout_Risk_Score'] = df.apply(lambda row: (1 if row['OverTime']=='Yes' else 0) + (1 if row['WorkLifeBalance'] <= 2 else 0), axis=1)

df.to_csv('Palo_Alto_Analyzed.csv', index=False)
print("File 'Palo_Alto_Analyzed.csv' successfully created!")