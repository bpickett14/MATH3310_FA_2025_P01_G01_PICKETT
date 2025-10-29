# MATH 3310: Analyzing Murder Rate in Relation to Socioeconomic and Demographic Variables

**Course:** Data Mining & Text Analytics (MATH 3310)  
**Instructor:** Dr. Jishan Ahmed  
**Semester:** Fall 2025  
**Group:** 01
**Repository:** MATH3310_FA_2025_P01_G01_PICKETT

---

## Project Overview
This project investigates the relationship between murder rates across U.S. states and various socioeconomic and demographic factors. Using both classical statistics and machine learning approaches, we explore which factors contribute most to variations in murder rates and assess the predictive power of our models.

The dataset `crime.csv` includes variables such as income, education, unemployment, and region. The state variable is treated as a subject identifier and is not used as a predictor. 

---

## Project Structure
├── data/
│ └── raw/
│ └── crime.csv # Original dataset
├── notebooks/
│ └── first_project.ipynb # Main analysis notebook
├── README.md # This file
└── requirements.txt # Python packages used


---

## Methods

### Part 1: Classical Statistics Approach
- Multiple linear regression using `statsmodels`  
- ANOVA comparisons to evaluate nested models and identify significant predictors  
- Diagnostics including residual plots, Q-Q plots, and time series analysis  
- Calculated RMSE for model evaluation  

**Key variables included in final model:**  
- `single_parent`  
- `metropolitan`  
- `high_school`  

---

### Part 2: Machine Learning Approach
- Linear Regression using `scikit-learn`  
- Train/test split (80/20) and 5-fold cross-validation  
- Pipelines and `ColumnTransformer` used for scaling and preprocessing  
- Evaluated model using R² and visualized predictions  

---

## Results

**Classical Statistics:**  
- Full model Adjusted R²: 0.6191567906134434
- Reduced model RMSE: 1.649644176815288
- Significant predictors: `single_parent`, `metropolitan`, `high_school`  

**Machine Learning:**  
- Train R²: 0.7162247626538154 
- Test R²: 0.2725910727718007
- Cross-validation average R²: 0.35275094205763685  


---

## Contributions
| Team Member      | Contributions |
|------------------|---------------|
| Brenna Pickett   | Majority of coding, data preprocessing, model building, diagnostics, plotting, writing analysis and discussion. |
| Dante Smith      | Contributed initial draft answers for Question 2; work was refined and incorporated into final notebook. |

---

## Reflection & Recommendations
- Classical approach provides interpretability for variable relationships; machine learning approach provides predictive accuracy.  
- Future analyses could include more granular data by state or county for improved prediction.  
- Policymakers can use the findings to target interventions in areas with higher single-parent households, metropolitan areas, or lower high school graduation rates.  
- A Tableau dashboard could help visualize correlations and trends across regions.  

---

## Requirements
- Python 3.9+  
- pandas  
- numpy  
- matplotlib  
- scikit-learn  
- statsmodels  

Install packages using:

```bash
pip install -r requirements.txt

