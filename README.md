# StocksDataAnalytics
Using Hadoop and Python, we analyze Tunisian stock market data to deduce insights.

## Data

### Overview

This directory contains the data source for our future analysis.

### Data Preparation

1. **Download Data:**  
   - Download the `Historique Cotation` for the last four years (2020, 2021, 2022, 2023) from the [BVMT website](https://www.bvmt.com.tn/fr/content/historique-des-données).
  
2. **Data Directory:**  
   - Place the downloaded files in the `data` directory.

## Data Processing

To generate the merged dataset that we will work with, execute the following Python script:

```bash
python mergeData.py
