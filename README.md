# Data Analyst - Impact Analysis of Monkeypox Case Study

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
├── notebooks/                                                 # Directory for jupyter notebooks code
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
