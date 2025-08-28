
# Workers Salary Prediction Model

This repository contains a machine learning project for predicting workers' salaries based on various demographic and job-related features. The project uses Python, pandas, scikit-learn, and seaborn for data analysis, preprocessing, visualization, and modeling.

## Project Overview

The goal is to predict the salary of workers given the following features:
- Age
- Gender
- Education Level
- Job Title
- Years of Experience

The project workflow includes:
- Data loading and cleaning
- Exploratory data analysis (EDA)
- Data preprocessing (handling missing values, duplicates, encoding)
- Model training (Linear Regression)
- Model evaluation (R², MSE, MAE)
- Visualization of results

## Notebooks

The main analysis is performed in the Jupyter notebook `sal.ipynb`.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/<your-username>/<your-repo>.git
    cd <your-repo>
    ```
2. Install dependencies using pip:
    ```bash
    pip install -r requirements.txt
    ```
    Or manually install the main packages:
    ```bash
    pip install pandas numpy scikit-learn seaborn matplotlib jupyter
    ```

## Usage

1. Place your dataset file (e.g., `Salary Data.csv`) in the project directory.
2. Open the notebook:
    ```bash
    jupyter notebook sal.ipynb
    ```
3. Run the notebook cells in order to follow the workflow from data loading to model evaluation.

## Project Structure

```
.
├── sal.ipynb         # Main Jupyter notebook
├── Salary Data.csv   # Example dataset (not included)
├── README.md         # This file
└── requirements.txt  # Python dependencies (optional)
```

## Results

The model provides predictions for workers' salaries and includes visualizations showing relationships between salary and other features, such as education level and years of experience.

## Visualizations

The notebook includes:
- Bar plots of average salary by education level and gender
- Scatter plots and line plots of salary against job title, years of experience, and age

## License

This project is licensed under the MIT License.

## Acknowledgements

- [pandas](https://pandas.pydata.org/)
- [scikit-learn](https://scikit-learn.org/)
- [seaborn](https://seaborn.pydata.org/)
- [matplotlib](https://matplotlib.org/)

---

Feel free to use or modify this project for your own salary prediction tasks!
````# salary-prediction-webapp
