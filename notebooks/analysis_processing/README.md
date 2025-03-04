# Impact Analysis of Monkeypox Case Study - Analysis_Processing

---

This comprehensive data analysis project focuses on the Monkeypox outbreak. Utilizing a Jupyter notebook, it provides insights and visualizations to help understand the spread, trends, and impacts of the Monkeypox virus globally. By employing data analysis techniques and visualizations, this project aims to facilitate a deeper understanding of the outbreak and deliver informative results to support public health efforts.

## Business Understanding

**The Monkeypox outbreak**, though not as widespread as other pandemics, poses significant public health challenges globally, especially in regions where the virus is most prevalent. As governments and health organizations strive to contain the spread, there is a need to **analyze Monkeypox data to extract actionable insights** that can aid in **public health responses and policy formation**. The objective of this project is to analyze global Monkeypox data, particularly focusing on regional trends, severity, and demographic impacts to support **strategic interventions**. The key aspects of this analysis will include:

1. **Epidemiologic Trends**: Investigating the spread of Monkeypox across different regions, focusing on factors such as new cases, total cases, and mortality rates.

2. **Regional Comparisons**: Comparing various countries and regions to understand how Monkeypox affects different areas, identifying regions with high transmission and high mortality rates.

3. **Demographic Trends**: Analyzing the impact of Monkeypox based on available demographic data (e.g., countries or regions) to highlight vulnerable groups or areas requiring urgent attention.

4. **Temporal Analysis**: Examining how the outbreak has evolved over time, identifying any patterns or spikes in infections and deaths that could guide future preventive measures.

5. **Identification of High-risk Regions**: Identifying "hotspots" can support public health officials in prioritizing these areas for immediate attention and interventions.

## Problem Points

Although Monkeypox is not as popular as other pandemics, its spread still poses significant challenges to global public health, especially in countries where the virus is more prevalent. Some of the key issues that need to be analyzed from this data are:

1. Identification of Spread Trends: How is Monkeypox spreading in different regions and countries? Are there regions that are more susceptible to this spread?
2. Correlation between Cases and Deaths: Is there a significant relationship between the number of new cases and the number of deaths in each country?
3. Regional Comparison: Which countries or regions have the highest number of cases and deaths, and how has this evolved over time?
4. Temporal Analysis: Are there any patterns or spikes in the spread of Monkeypox based on time of day, e.g. in certain seasons or certain time periods of the year?
5. Case Fatality Ratio Analysis: Which regions have the highest case fatality ratios? Do these regions also have a high number of cases or fewer but higher fatality rates?

---

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

<!-- **Data Description**

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
14. new_deaths_smoothed_per_million: Rata-rata jumlah kematian baru harian yang dihaluskan per satu juta penduduk.
15. suspected_cases_cumulative: Jumlah kasus Monkeypox yang dicurigai hingga tanggal tertentu (jika data tersedia).
16. annotation: Catatan tambahan atau informasi terkait laporan data pada tanggal tertentu (misalnya, revisi atau koreksi data).

**Data Grouping**

1. Total Kasus dan Kematian per Negara/Wilayah: Menghitung jumlah total kasus dan kematian Monkeypox di setiap negara atau wilayah.
2. Perkembangan Kasus per Hari: Mengelompokkan data berdasarkan tanggal untuk melihat tren penyebaran harian.
3. Distribusi Kasus Baru per Wilayah: Melihat distribusi kasus baru berdasarkan lokasi dan waktu untuk memahami wilayah yang terkena dampak paling parah dalam periode tertentu.
4. Analisis Rasio Fatalitas Kasus (Case Fatality Ratio): Menghitung rasio fatalitas kasus (CFR) sebagai jumlah total kematian dibagi jumlah total kasus di setiap negara/wilayah untuk mengidentifikasi wilayah dengan tingkat fatalitas yang tinggi. -->
