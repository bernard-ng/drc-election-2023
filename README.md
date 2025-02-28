# Reconstructing and verifying the 2023 presidential election results in the Democratic Republic of Congo: A data-driven analysis


```tex
@misc {bernard_ngandu_2025,
	author       = { {Bernard Ngandu} },
	title        = { drc-elections-2023 (Revision dcb13ea) },
	year         = 2025,
	url          = { https://huggingface.co/datasets/bernard-ng/drc-elections-2023 },
	doi          = { 10.57967/hf/4635 },
	publisher    = { Hugging Face }
}
```

**Dataset is available on Hugging Face Datasets: [drc-elections-2023](https://huggingface.co/datasets/bernard-ng/drc-elections-2023)**

---

## Introduction

The Democratic Republic of Congo (DRC) held its presidential elections in December 2023, with official results announced shortly thereafter by the Independent National Electoral Commission (CENI). This research study aims to validate the accuracy and transparency of these results by independently reproducing the vote counts using publicly available data. The study collected election-related data through web scraping of CENI's official website, followed by data cleaning, processing, and analysis. Statistical methods were applied to compare the reconstructed results to the official figures. The research highlights potential discrepancies or confirms the consistency of the published election outcomes. By utilizing transparent and reproducible data-driven methodologies, this study seeks to promote electoral accountability and contribute to the discourse on election integrity in the DRC.

## Methodology

### 1. Data Collection via Web Scraping

- Data Source: All relevant election data were collected from the official website of the Independent National Electoral Commission (CENI). This included polling station-level results, aggregated regional tallies, and total vote counts.
Web Scraping Tools: Automated scraping scripts were developed using Python with libraries such as BeautifulSoup and Scrapy to efficiently extract structured data from the CENI web pages.
- Data Storage: Extracted data were stored in a structured format (e.g., CSV/SQL database) for ease of analysis. Multiple snapshots of the website were taken to account for potential changes over time.
- Data Cleaning: The data were pre-processed to remove duplicates, handle missing or incomplete records, and standardize the format for all entries.

### 2. Data Analysis

- Aggregation and Comparison: Vote counts from individual polling stations were aggregated to higher administrative levels (e.g., regional or national) and compared to official results published by CENI.
- Statistical Methods: Statistical consistency checks, outlier detection, and regression analysis were applied to identify any potential irregularities in the vote distributions.
- Visualization: Graphical representations of voting patterns and discrepancies, if any, were generated to provide an intuitive view of the results.

## Acknowledgment:
The dataset provided in these CSV files originates from the Commission Électorale Nationale Indépendante (CENI), the National Independent Electoral Commission of the Democratic Republic of Congo (DRC). CENI is responsible for overseeing electoral processes in the country, ensuring fairness, transparency, and accuracy in elections.

The compilation and curation were conducted by Tshabu Ngandu Bernard with the primary objective of facilitating research and analysis related to the Democratic Republic of Congo.

I dot not claim ownership of the original data, and all rights and responsibilities regarding the accuracy and integrity of the dataset remain with CENI. The dataset is provided for research and educational purposes only, and any further use or dissemination should adhere to the relevant legal and ethical guidelines.
