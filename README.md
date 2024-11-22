# Impact Analysis of Monkeypox Case Study

This comprehensive data analysis project focuses on the Monkeypox outbreak. Utilizing a Jupyter notebook, it provides insights and visualizations to help understand the spread, trends, and impacts of the Monkeypox virus globally. By employing data analysis techniques and visualizations, this project aims to facilitate a deeper understanding of the outbreak and deliver informative results to support public health efforts.

## Features

- **Data Preprocessing**: Loading, cleaning, and transforming raw data for analysis.
- **Descriptive Statistics**: Overview and statistical description of Monkeypox cases by country and region.
- **Data Visualization**: Time-series plots, histograms, and bar charts to visualize trends and distributions.

## Technologies Used

- Python (3.x)
- Jupyter Notebook
- Pandas
- Matplotlib
- Seaborn

## How to Use

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/RyanGA09/DataAnalyst-ImpactAnalysisOfMonkeypoxCaseStudy.git
   ```

2. Create a Virtual Environment:

   ```bash
   python -m venv venv
   ```

3. Activate the Virtual Environment:

   - On Window:

   ```bash
   venv\Scripts\activate
   ```

   - On macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

4. Install Required Packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Open the Jupyter Notebook:

   ```bash
   jupyter notebook Notebook.ipynb
   ```

6. Run the Cells: Execute each cell sequentially in the notebook to perform data analysis and visualize results.

## Dataset

The dataset used for this project is included in the `data/` directory or can be downloaded from [Monkeypox Data Source](https://ourworldindata.org/mpox). If you Download the data from [Monkeypox Data Source](https://ourworldindata.org/mpox) Ensure the data file is placed in the `data/` directory before running the notebook.

## Project Structure

```bash
ImpactAnalysisOfMonkeypoxCaseStudy/
│
├── data/                                                  # Directory for datasets
│   │   ├── original/                                      # Original dataset folder
│   │   │   └── monkeypox.csv                              # Raw data file
│   │   ├── filtered/                                      # Filtered datasets folder by year and month
│   │   │   └── monkeypox_2022_5_to_2024_11_filtered.csv   # Raw filtered data file
│   │   └── processed/                                     # processed datasets folder
│   │       └── monkeypox_2022_5_to_2024_11_processed.csv  # Cleaned Data file
├── Notebook_Analyzing.ipynb                               # Jupyter notebook containing the analysis code
├── Notebook_Science.ipynb                                 # Jupyter notebook containing the data science
├── filter_monkeypox_data.py                               # Python code for filtering dataset
├── README.md                                              # Project documentation and usage instructions
└── requirements.txt                                       # List of required Python libraries
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
