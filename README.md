# StocksDataAnalytics
When working with data, it's essential to first understand and prepare it for processing. Next, leveraging Hadoop and MapReduce, we'll extract additional insights. Additionally, we'll analyze the results using tools like Hive and Pig. Finally, we'll present everything in a dashboard. Stay tuned!

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
