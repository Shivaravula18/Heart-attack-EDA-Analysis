# Heart Attack Analysis – Exploratory Data Analysis Project

## 📌 Project Overview
This project focuses on performing exploratory data analysis (EDA) on a heart attack dataset to identify key risk factors associated with heart disease. The analysis includes statistical measures, visualizations, and interpretations to extract insights that could help in early diagnosis and better understanding of cardiovascular conditions.

---

## 📁 Dataset Description
The dataset contains medical attributes of patients along with an output column indicating the likelihood of a heart attack. Below are the primary features:

- `age`: Age of the patient
- `sex`: Sex (0 = Male, 1 = Female)
- `cp`: Chest pain type (0-3)
- `trtbps`: Resting blood pressure (mm Hg)
- `chol`: Serum cholesterol (mg/dl)
- `fbs`: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
- `restecg`: Resting electrocardiographic results (0-2)
- `thalachh`: Maximum heart rate achieved
- `exng`: Exercise-induced angina (1 = yes; 0 = no)
- `oldpeak`: ST depression induced by exercise
- `slp`: Slope of the peak exercise ST segment
- `caa`: Number of major vessels (0–4)
- `thall`: Thalassemia (0–3)
- `output`: 0 = less chance of heart attack, 1 = more chance

---

## ✅ Tasks Performed

1. **Duplicate Value Handling**  
   - Checked and removed duplicate entries.

2. **Missing Value Handling**  
   - Imputed missing values using mean, median, and mode as appropriate.

3. **Descriptive Statistics**  
   - Computed mean, standard deviation, and quartiles for key numerical features (`age`, `trtbps`, `chol`, `thalachh`).

4. **Gender-wise Risk Analysis**  
   - Used count plots to compare heart attack rates between males and females.

5. **Chest Pain Type Analysis**  
   - Identified the chest pain type most associated with higher heart attack risk.

6. **Age Impact Analysis**  
   - Used box plots to analyze how age correlates with heart attack likelihood.

7. **Fasting Blood Sugar Risk Analysis**  
   - Compared heart attack risk in patients with high vs. low fasting blood sugar.

8. **ECG Results Analysis**  
   - Assessed how different resting ECG results affect heart attack risk.

9. **Resting Blood Pressure Significance**  
   - Visualized its distribution and compared across heart attack outcomes.

10. **Maximum Heart Rate Effect**  
   - Studied relationship between `thalachh` and heart attack.

11. **ST/HR Ratio Impact**  
   - Created and analyzed a derived feature `st_hr_ratio` (oldpeak / thalachh).

---

## 📊 Libraries Used
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`

---

## 🧠 Insights
- Males tend to have a higher heart attack rate in this dataset.
- Asymptomatic chest pain is linked to the highest risk.
- High heart rate and ST/HR ratio may be significant indicators.
- Fasting blood sugar was not a strong differentiator in this dataset.

---

## 📝 How to Run
1. Open the `.ipynb` file in Google Colab or Jupyter Notebook.
2. Ensure the `heart.csv` dataset is uploaded or properly linked.
3. Run all cells sequentially to reproduce the full analysis.


