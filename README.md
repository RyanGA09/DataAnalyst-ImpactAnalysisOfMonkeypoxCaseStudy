# 🧪 Data Analyst - Impact Analysis of Monkeypox Case Study

[![License: MIT License with Commons Clause](https://img.shields.io/badge/license-MIT%20License%20with%20Commons%20Clause-blue?style=for-the-badge)](LICENSE) [![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&style=for-the-badge)](https://www.python.org/) [![Made with Jupyter Notebook](https://img.shields.io/badge/Made%20with-Jupyter%20Notebook-orange?logo=jupyter&style=for-the-badge)](https://jupyter.org/)

This project was developed as part of my data analyst portfolio to demonstrate my skills in data preprocessing, exploratory data analysis (EDA), and data visualization using a real-world public health dataset. The case study focuses on the impact and spread of Monkeypox across regions, aiming to extract actionable insights from time-series and geographical patterns.

## 🚀 Features

- **Data Preprocessing**: Loading, cleaning, and transforming raw data for analysis.
- **Descriptive Statistics**: Overview and statistical description of Monkeypox cases by country and region.
- **Data Visualization**: Time-series plots, Bar charts, Line plots, Annotated visualizations, and Tables to visualize trends and distributions.

## 🛠️ Technologies Used

[![Pandas](https://img.shields.io/badge/Pandas-DataFrame-black?logo=pandas&style=for-the-badge)](https://pandas.pydata.org/) [![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blue?logo=matplotlib&style=for-the-badge)](https://matplotlib.org/) [![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-lightblue?logo=seaborn&style=for-the-badge)](https://seaborn.pydata.org/) [![Pathlib](https://img.shields.io/badge/Pathlib-Path%20Handling-green?style=for-the-badge)](https://docs.python.org/3/library/pathlib.html) [![OS](https://img.shields.io/badge/OS-Utilities-yellow?style=for-the-badge)](https://docs.python.org/3/library/os.html) [![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&style=for-the-badge)](https://python.org)

## ▶️ How to Use the Program

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/RyanGA09/DataAnalyst-ImpactAnalysisOfMonkeypoxCaseStudy.git
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:

   - On Windows:

   ```bash
   venv\Scripts\activate
   ```

   - On macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

4. **Install Required Packages**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Filter Data**

   Before working on the notebooks, filter the datasets using the provided Python script. You can execute the script by running:

   ```bash
   python filter_monkeypox_data.py
   ```

   This will process the raw data and generate the necessary filtered datasets for further analysis.

6. **Open the Jupyter Notebook**:

   - To perform business understanding, gather data, and data cleaning, open the notebook located in the analysis_processing directory, which focuses on data processing tasks:

     ```bash
     jupyter notebook notebooks/analysis_processing/{start_year}_{start_month}_to_{end_year}_{end_month}/Notebook.ipynb
     ```

   - To conduct Exploratory Data Analysis (EDA) and data visualization, open the notebook in the visualization subdirectory, which is focused on further analysis and visual representation of the data:

     ```bash
     jupyter notebook notebooks/visualization/Notebook_visualization_{start_year}_{start_month}_to_{end_year}_{end_month}.ipynb
     ```

7. **Run the Cells**:

   - In the analysis_processing notebooks, execute each cell sequentially to perform data cleaning, data preparation, and business understanding steps.
   - In the visualization notebooks, run each cell to conduct exploratory data analysis (EDA), and create data visualizations based on the processed data.

## 📊 Dataset Information

### 🔗 Data Source

The dataset used for this project is available in the `data/raw/original` directory or can be downloaded from the [Monkeypox Data Source](https://ourworldindata.org/mpox).

### 📥 Downloading and Placing the Data

1. Download Data: If you choose to download the data, you can obtain it from the [Monkeypox Data Source](https://ourworldindata.org/mpox).
2. Placing the Data: After downloading, ensure that the data file is placed in the `data/raw/original/` directory. This is where the original, unprocessed data should be stored before any filtering or processing takes place.

### Data Filtering Process

Once the original data file is stored in the `data/raw/original` directory, it will be processed and filtered as per the requirements of the analysis. The filtered data will be saved in the `data/raw/filtered` directory. The filtering process includes:

- Removing irrelevant or incomplete data
- Selecting relevant subsets of data for further analysis
- Optimizing the data format and quality to meet the needs of the project

### 🔎 Data Processing and Analysis

After the filtered data is prepared in the `data/filtered` directory, it will undergo further processing and analysis. The processed data, which is used for Exploratory Data Analysis (EDA) and visualization, will be stored in the `data/processed` directory. This stage includes:

- Conducting exploratory data analysis (EDA) to uncover patterns, trends, and insights
- Cleaning the data further, if needed, for visualization and statistical analysis
- Generating data visualizations to better understand the trends and relationships in the dataset

## 🗂️ Project Structure

```bash
ImpactAnalysisOfMonkeypoxCaseStudy/
│
├── data/                                                      # Contains the datasets
│   ├── processed/                                             # Contains the processed data, used for EDA and visualization.
│   └── raw/                                                   # Contains the original and filtered data directory
│        ├── filtered/                                         # Contains the filtered data, ready for analysis.
│        └── original/                                         # Contains the original, unfiltered & unprocessed data.
├── notebooks/                                                 # Contains the jupyter notebooks code
├── filter_monkeypox_data.py                                   # Python code for filtering dataset
├── README.md                                                  # Project documentation and usage instructions
└── requirements.txt                                           # List of required Python libraries
```

## 📖 Read More

Check out my article on [Medium](https://medium.com/@ryangadingabdullah):

[![Medium](https://img.shields.io/badge/Medium-Article-000000?logo=medium&style=for-the-badge)](https://medium.com/@ryangadingabdullah/article)

You can check the visualization result from my [Tableau](https://public.tableau.com/app/profile/ryanga09/vizzes) Dashboard on the badge below:

[![Tableau](https://img.shields.io/badge/Tableau-View-orange?logo=tableau&style=for-the-badge)](https://public.tableau.com/app/profile/ryanga09/vizzes)

## ☕ Support Me

This is a non-commercial project. If you find it useful and would like to support the development of this project, you can donate via the links below. Your support helps improve the project, but it does not grant any commercial rights over the project itself.

[![Saweria](https://img.shields.io/badge/Saweria-Support-orange?logo=saweria&style=for-the-badge)](https://saweria.co/RyanGA09)

<!-- [![PayPal](https://img.shields.io/badge/PayPal-Donate-00457C?logo=paypal&style=for-the-badge)](https://www.paypal.me/ryangading) -->

## 📜 License

This project is licensed under the MIT License with Commons Clause. It is for personal, academic, and non-commercial use only.
Any commercial use is prohibited without explicit written permission from the author.

See the [LICENSE](LICENSE) file for more details.

Copyright &copy; 2024 Ryan Gading Abdullah. All rights reserved.

## 📧 Contact

For commercial inquiries, please contact:

[![Gmail](https://img.shields.io/badge/Gmail-Contact-D14836?logo=gmail&style=for-the-badge)](mailto:ryangadinga90@gmail.com)

Or reach me on LinkedIn:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin&style=for-the-badge)](https://www.linkedin.com/in/ryan-gading-abdullah/)
