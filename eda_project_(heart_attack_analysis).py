# -*- coding: utf-8 -*-
"""EDA_Project_(Heart_Attack_Analysis).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WBBFUHzpewV5FYpheVLSiKVBk4aPy5N6

# EDA Assignment

---

**EDA Project Instructions**

1. **Read Each Task Carefully**: Understand each task’s requirements before starting your analysis.

2. **Perform the Analysis**: For each task, you’ll find a description in the code cell. Write your code directly in the provided cells to perform the necessary analysis using the Heart Attack dataset.

3. **Visualize and Interpret**: Create visualizations and interpret the results as needed. Ensure your analysis addresses the specific questions and insights required.

4. **Complete All Tasks**: Make sure you address each task. Each task is designed to test different aspects of data analysis and visualization.

5. **Download Your Notebook**: After completing and reviewing your analysis, download your notebook file (.ipynb) by selecting `File > Download > Download .ipynb`.

6. **Submit Your Work**: Upload the downloaded `.ipynb` file to the designated platform for submission.

7. **Verify Your Submission**: Ensure that you have submitted the correct file and that it is not corrupted. If needed, resubmit the file.

Good luck, and happy analyzing!

---

## Dataset Information :
<ul style= "color:#137667;
            font-size:12px;">
    <li> age : age of the patient</li>
    <li> sex : sex of the patient (0 - Male, 1 - Female)</li>
    <li> cp : Chest Pain type</li>
    0: typical angina <br>
    1: atypical angina <br>
    2: non-anginal pain <br>
    3: asymptomatic <br>
    <li> trtbps : resting blood pressure (in mm Hg)</li>
    <li> fbs : (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)</li>
    <li> chol : cholestoral in mg/dl fetched via BMI sensor</li>
    <li> rest_ecg : resting electrocardiographic results</li>
  0:normal <br>
  1:having ST-T wave abnormality(T wave inversions and/or ST elevation or depression of>0.05 mV) <br>
  2:showing probable or definite left ventricular hypertrophy by Estes' criteria
    <li> thalachh : maximum heart rate achieved</li>
    <li> exng : exercise induced angina (1 = yes; 0 = no)</li>
    <li> oldpeak : Previous peak</li>
    <li> slp : ST/HR Slope </li>
    <li> caa : number of major vessels (0-4)</li>
    <li> thall : Thal rate</li>
    <li> output : 0= less chance of heart attack 1= more chance of heart attack</li>
</ul>
"""

# Commented out IPython magic to ensure Python compatibility.
# Run this code cell for initial setup
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

mpl.style.use('ggplot')

import warnings
warnings.filterwarnings('ignore')

# %matplotlib inline

# load the data to colab
data = pd.read_csv('heart.csv')
data.head(10)

data.info()

"""---
---
**1. Check the presence of duplicate values and deal with them.**
"""

# write your code here
data.duplicated().sum()

"""---
---
**2.Check the presence of missing values and deal with them.**
"""

# write your code here
# chol column (continuous numerical)
# thalachh (continuous numerical)
# exng (categorical)
data.isnull().sum()

data['chol'].fillna(data['chol'].mean(), inplace=True)

data['thalachh'].fillna(data['thalachh'].median(), inplace=True)

data['exng'].fillna(data['exng'].mode()[0], inplace=True)

data.isnull().sum()

"""---
---
**3.Determine mean, standard deviation and quartiles(q1,q2,q3) for following columns:**
   - age
   - trtbps
   - chol
   - thalachh
"""

# write your code here
age_mean = data['age'].mean()
age_std = data['age'].std()
age_q1 = data['age'].quantile(0.25)
age_q2 = data['age'].quantile(0.50)
age_q3 = data['age'].quantile(0.75)

trtbps_mean = data['trtbps'].mean()
trtbps_std = data['trtbps'].std()
trtbps_q1 = data['trtbps'].quantile(0.25)
trtbps_q2 = data['trtbps'].quantile(0.50)
trtbps_q3 = data['trtbps'].quantile(0.75)

chol_mean = data['chol'].mean()
chol_std = data['chol'].std()
chol_q1 = data['chol'].quantile(0.25)
chol_q2 = data['chol'].quantile(0.50)
chol_q3 = data['chol'].quantile(0.75)

thalachh_mean = data['thalachh'].mean()
thalachh_std = data['thalachh'].std()
thalachh_q1 = data['thalachh'].quantile(0.25)
thalachh_q2 = data['thalachh'].quantile(0.50)
thalachh_q3 = data['thalachh'].quantile(0.75)

"""---
---
**4.Analyse whether males or females are at a higher risk of heart attack.**
"""

# write your code here
# Calculate proportion of heart attacks by sex
plt.figure(figsize=(8,5))
sns.countplot(x='sex', hue='output', data=data)
plt.xticks([0,1], ['Female', 'Male'])
plt.xlabel('Sex')
plt.ylabel('Count')
plt.title('Heart Attack Cases by Sex')
plt.legend(title='Heart Attack', labels=['No (0)', 'Yes (1)'])
plt.show()

"""**5.Patients with which type of chest pain are at highest risk of heart attack.**"""

cp_risk = data.groupby('cp')['output'].mean().reset_index()


cp_labels = {
    0: 'Typical Angina',
    1: 'Atypical Angina',
    2: 'Non-Anginal Pain',
    3: 'Asymptomatic'
}
cp_risk['cp_label'] = cp_risk['cp'].map(cp_labels)


# Plot the proportions
plt.figure(figsize=(8,5))
sns.barplot(x='cp_label', y='output', data=cp_risk, palette='muted')

plt.xlabel('Chest Pain Type')
plt.ylabel('Proportion with Heart Attack')
plt.title('Heart Attack Risk by Chest Pain Type')
plt.ylim(0, 1)

plt.show()

"""---
---
**6.Analyse the effect of age on heart attack risk.**
"""

# write your code here
plt.figure(figsize=(8,6))
sns.boxplot(x='output', y='age', data=data, palette='Set2')

plt.xticks([0,1], ['No Heart Attack', 'Heart Attack'])
plt.xlabel('Heart Attack Status')
plt.ylabel('Age')
plt.title('Age Distribution by Heart Attack')

plt.show()

"""---
---
**7.A higher risk of heart attack is associated more with low fasting blood sugar levels or high fasting blood sugar levels.**
"""

fbs_risk = data.groupby('fbs')['output'].mean().reset_index()
fbs_risk['fbs_label'] = fbs_risk['fbs'].map({0: 'Low FBS (<=120)', 1: 'High FBS (>120)'})
plt.figure(figsize=(6,4))
sns.barplot(x='fbs_label', y='output', data=fbs_risk, palette='coolwarm')
plt.ylabel('Proportion with Heart Attack')
plt.xlabel('Fasting Blood Sugar Level')
plt.title('Heart Attack Risk by Fasting Blood Sugar')
plt.ylim(0,1)

plt.show()

"""---
---
**8.How the risk of heart atack can be determined from resting electrocardiographic results?**
"""

restecg_risk = data.groupby('restecg')['output'].mean().reset_index()
restecg_labels = {
    0: 'Normal',
    1: 'ST-T Wave Abnormality',
    2: 'Left Ventricular Hypertrophy'
}
restecg_risk['restecg_label'] = restecg_risk['restecg'].map(restecg_labels)
plt.figure(figsize=(8,5))
sns.barplot(x='restecg_label', y='output', data=restecg_risk, palette='viridis')
plt.title('Heart Attack Risk by Resting ECG Results')
plt.xlabel('Resting ECG Category')
plt.ylabel('Proportion with Heart Attack')
plt.ylim(0,1)

plt.show()

"""---
---
**9. Is resting blood presure a significant factor for detrmining risk of a heart attack?**
"""

# write your code here
plt.figure(figsize=(8,6))
sns.boxplot(x='output', y='trtbps', data=data, palette='Set3')

plt.xticks([0,1], ['No Heart Attack', 'Heart Attack'])
plt.xlabel('Heart Attack Status')
plt.ylabel('Resting Blood Pressure (trtbps)')
plt.title('Resting Blood Pressure by Heart Attack Status')
plt.show()

"""---
---
**10.Is heart attack risk asociated with a higher heart rate?**
"""

# write your code here
plt.figure(figsize=(8,6))
sns.boxplot(x='output', y='thalachh', data=data, palette='coolwarm')

plt.xticks([0,1], ['No Heart Attack', 'Heart Attack'])
plt.xlabel('Heart Attack Status')
plt.ylabel('Maximum Heart Rate Achieved')
plt.title('Heart Rate Distribution by Heart Attack Status')
plt.show()

"""---
---
**11. Determine whether ST/HR (ST segment and Heart rate ratio) is a singificant factor in determining heart attack risk.**
"""

data['st_hr_ratio'] = data['oldpeak'] / data['thalachh']

# write your code here
plt.figure(figsize=(8,6))
sns.boxplot(x='output', y='st_hr_ratio', data=data, palette='Set1')

plt.xticks([0,1], ['No Heart Attack', 'Heart Attack'])
plt.xlabel('Heart Attack Status')
plt.ylabel('ST/HR Ratio')
plt.title('ST/HR Ratio by Heart Attack Status')
plt.show()

"""## End!"""