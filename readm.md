# Causal Inference for Prize Impact Analysis

This project analyzes the causal impact of winning literary prizes (e.g., Hugo Award, Booker Prize, Nobel Prize) on Goodreads reviews and ratings. Using advanced causal inference techniques, we estimate the **Average Treatment Effect (ATE)** of winning a prize by comparing prize-winning books to matched control groups.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Methodology](#methodology)
4. [Dependencies and Datasets](#dependencies)
5. [License](#license)

---

## Overview

The goal of this project is to determine whether winning a literary prize has a measurable impact on book success metrics. By leveraging the causal inference method propensity score weighting and k-nearest neighbors (kNN) matching, we ensure robust and interpretable results.

Key questions addressed:
- Does winning a prize lead to increased reviews?
    Answer: yes, depending on the prize only a few extra reviews up to multiple thousands.
- Are there cases where winning a prize has a negative effect?
    Answer: A small but statsitically significant negative effect of winning a prize on review score was found.

---

## Features

- **Causal Inference**: Uses state-of-the-art causal inference techniques to estimate treatment effects using the doWhy package.
- **Robust Matching**: Matches prize-winning books to similar non-winning books using kNN and propensity weigthing.
- **Handling Missing Data**: Implements strategies to handle missing values (`NaN`) and avoid biased estimates.
- **Scalable**: Designed to handle large datasets with multiple prize categories and time periods. Datasets used consists of 15 Million reviews.
- **Visualization**: Includes tools for visualizing outcomes.

---

## Methodology

1. **Data Preprocessing**:
   - Remove unneeded data columns and transform into more efficient binary (parquet) representation.
   - Handle missing data by replacing `0` with `NaN` for rows with insufficient reviews.

2. **Matching**:
   - Use kNN matching to find comparable control books based on pre-treatment features (cumulative reviews and slopes at time of prize winning).
   - Normalize features using `MinMaxScaler` and `LogTransform` for consistent comparisons in the kNN.

3. **Causal Estimation**:
   - Compute the **Average Treatment Effect (ATE)** using propensity score weighting.
   - Validate results with confidence intervals and sensitivity analyses.

4. **Statistical Outcome Analysis**:
   - Groups and analyzes the outcomes for every individual price and for all combined.



---

## Dependencies

This project requires the following Python libraries:

- `numpy`
- `pandas`
- `scikit-learn`
- `dowhy` (for causal inference)
- `matplotlib` and `seaborn` (for visualization)

To install these dependencies, run the following command:

```bash
pip install numpy pandas scikit-learn dowhy matplotlib seaborn
```
Python 3.10 was used for the analysis.

The Datasets were provided by the University of California San Diego and can be found here:
https://cseweb.ucsd.edu/~jmcauley/datasets/goodreads.html, accessed February 2025.
Mengting Wan, Julian McAuley, "Item Recommendation on Monotonic Behavior Chains", in RecSys'18.
Mengting Wan, Rishabh Misra, Ndapa Nakashole, Julian McAuley, "Fine-Grained Spoiler Detection from Large-Scale Review Corpora", in ACL'19.

The Datsets was scraped from public Goodreads profiles in 2017; they contain 2,3 Million books and 15 Million reviews with ratings.
The Dataset includes more data but this is what was used for this analysis; see files goodreads_books.json.gz, goodreads_reviews_dedup.json.gz on the webpage.

## License

The Impact of Literature Prizes on Goodreads Geviews.
Copyright (C) <2025>  <Matthias Edthofer and Rosa Wittwehr>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.