# Data Analyst - Impact Analysis of Monkeypox Case Study

---

This comprehensive data analysis project focuses on the Monkeypox outbreak. Utilizing a Jupyter notebook, it provides insights and visualizations to help understand the spread, trends, and impacts of the Monkeypox virus globally. By employing data analysis techniques and visualizations, this project aims to facilitate a deeper understanding of the outbreak and deliver informative results to support public health efforts.

## Business Understanding

**The Monkeypox outbreak**, though not as widespread as other pandemics, poses significant public health challenges globally, especially in regions where the virus is most prevalent. As governments and health organizations strive to contain the spread, there is a need to **analyze Monkeypox data to extract actionable insights** that can aid in **public health responses and policy formation**. The objective of this project is to analyze global Monkeypox data, particularly focusing on regional trends, severity, and demographic impacts to support **strategic interventions**. The key aspects of this analysis will include:

1. **Epidemiologic Trends**: Investigating the spread of Monkeypox across different regions, focusing on factors such as new cases, total cases, and mortality rates.

2. **Regional Comparisons**: Comparing various countries and regions to understand how Monkeypox affects different areas, identifying regions with high transmission and high mortality rates.

3. **Demographic Trends**: Analyzing the impact of Monkeypox based on available demographic data (e.g., countries or regions) to highlight vulnerable groups or areas requiring urgent attention.

4. **Temporal Analysis**: Examining how the outbreak has evolved over time, identifying any patterns or spikes in infections and deaths that could guide future preventive measures.

5. **Identification of High-risk Regions**: Identifying "hotspots" can support public health officials in prioritizing these areas for immediate attention and interventions.

## Problem Statement

Although Monkeypox is not as popular as other pandemics, its spread still poses significant challenges to global public health, especially in countries where the virus is more prevalent. Some of the key issues that need to be analyzed from this data are:

1. Identification of Spread Trends: How is Monkeypox spreading in different regions and countries? Are there regions that are more susceptible to this spread?
2. Correlation between Cases and Deaths: Is there a significant relationship between the number of new cases and the number of deaths in each country?
3. Regional Comparison: Which countries or regions have the highest number of cases and deaths, and how has this evolved over time?
4. Temporal Analysis: Are there any patterns or spikes in the spread of Monkeypox based on time of day, e.g. in certain seasons or certain time periods of the year?
5. Case Fatality Ratio Analysis: Which regions have the highest case fatality ratios? Do these regions also have a high number of cases or fewer but higher fatality rates?

## Data Understanding

### Data Description

1. location: The name of the country or region that reported the data.
2. date: The date the data was reported in YYYY-MM-DD format.
3. new_cases: The number of new cases of Monkeypox reported on that date in the country/region.
4. new_deaths: The number of new deaths reported on that date in a country/region.
5. total_cases: The cumulative number of Monkeypox cases recorded in a country/region up to that date.
6. total_deaths: The cumulative number of deaths recorded in a country/region up to that date.
7. new_cases_per_million: The number of new cases per one million population in the region as of the given date.
8. total_cases_per_million: The cumulative number of cases per one million population up to the given date.
9. new_deaths_per_million: The number of new deaths per one million population in the region as of the given date.
10. total_deaths_per_million: The cumulative number of deaths per one million population up to the given date.
11. new_cases_smoothed: The smoothed average daily number of new cases over the given time period.
12. new_deaths_smoothed: The smoothed average daily number of new deaths over the given time period.
13. new_cases_smoothed_per_million: Average daily smoothed number of new cases per one million population.
14. new_deaths_smoothed_per_million: Average daily smoothed number of new deaths per one million population.
15. suspected_cases_cumulative: Number of suspected Monkeypox cases up to a certain date (if data is available).
16. annotation: Additional notes or information related to the data report on a specific date (for example, data revisions or corrections).

### Data Grouping

1. Total Cases and Deaths per Country/Region: Counts the total number of Monkeypox cases and deaths in each country or region.
2. Case Progression by Day: Categorize the data by date to see the trend of daily spread.
3. Distribution of New Cases by Region: View the distribution of new cases by location and time to understand the most severely affected regions in a given period.
4. Case Fatality Ratio Analysis: Calculate the case fatality ratio (CFR) as the total number of deaths divided by the total number of cases in each country/region to identify areas with high fatality rates.

---

## Features

- **Data Preprocessing**: Loading, cleaning, and transforming raw data for analysis.
- **Descriptive Statistics**: Overview and statistical description of Monkeypox cases by country and region.
- **Data Visualization**: Time-series plots, Bar charts, Line plots, Annotated visualizations, and Tables to visualize trends and distributions.

## Technologies Used

- Python (3.x)
- Jupyter Notebook
- Pandas
- Matplotlib
- Seaborn

## How to Use the Program

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/RyanGA09/DataAnalyst-ImpactAnalysisOfMonkeypoxCaseStudy.git
   ```

2. **Create a Virtual Environment**:

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:

   - On Window:

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

5. **Open the Jupyter Notebook**:

   - To perform business understanding, gather data, and data cleaning, open the notebook in the main directory which focuses on data processing:

     ```bash
     jupyter notebook Notebook.ipynb
     ```

   - To conduct Exploratory Data Analysis (EDA) and data visualization, open the notebook in the /visualization subdirectory, which focuses on further analysis and visual representation of the data:

     ```bash
     jupyter notebook /visualization/Notebook_visualization_{start_year}_{start_month}_to_{end_year}_{end_month}.ipynb
     ```

6. **Run the Cells**:

   Execute each cell sequentially in the notebook to perform data analysis and visualize results.

## Dataset

The dataset used for this project is included in the `data/` directory or can be downloaded from [Monkeypox Data Source](https://ourworldindata.org/mpox). If you Download the data from [Monkeypox Data Source](https://ourworldindata.org/mpox) Ensure the data file is placed in the `data/` directory before running the notebook.

## Project Structure

```bash
ImpactAnalysisOfMonkeypoxCaseStudy/
│
├── data/                                                      # Directory for datasets
│     ├── processed/                                           # Original dataset folder
│     │     └── monkeypox_2022_5_to_2024_11_processed.csv      # Cleaned Data file
│     └── raw/                                                 # Original dataset folder
│           ├── filtered/                                      # Filtered datasets folder by year and month
│           │     └── monkeypox_2022_5_to_2024_11_filtered.csv # Raw filtered data file
│           └── original/                                      # processed datasets folder
│                 └── monkeypox_2022_5_to_2024_11.csv          # Raw data file
├── notebooks/                                                 # Directory for notebooks code
│     ├── visualization/                                       # Directory for EDA & Data Visualization
│     │     └── Notebook_visualization_2022_5_to_2024_11.ipynb # Jupyter notebook containing the EDA & Visualization code
│     └── Notebook.ipynb                                       # Jupyter notebook containing the analysis code
├── filter_monkeypox_data.py                                   # Python code for filtering dataset
├── README.md                                                  # Project documentation and usage instructions
└── requirements.txt                                           # List of required Python libraries
```

## Read More

Check out my article on [Medium](https://medium.com/@ryangadingabdullah):

<div align="center">
   <a href="https://medium.com/@ryangadingabdullah/article" target="blank">
      <img src="https://img.shields.io/badge/Medium-Article-000000?logo=medium&style=for-the-badge" alt="Article on Medium" />
   </a>
</div>

<br>

You can check the visualization result from my [Tableau](https://public.tableau.com/app/profile/ryanga09/vizzes) Dashboard on the badge below:
<br>

<div align="center">
   <a href="https://public.tableau.com/app/profile/ryanga09/viz/ImpactAnalysisofMonkeypoxCaseStudy/ImpactAnalysisofMonkeypoxCaseStudy" target="blank">
        <img src="https://img.shields.io/badge/Tableau-View-orange?logo=tableau&style=for-the-badge" alt="View on Tableau" />
    </a>
</div>

## License

[MIT LICENSE](LICENSE)

&copy;2024 Ryan Gading Abdullah. All rights reserved.
