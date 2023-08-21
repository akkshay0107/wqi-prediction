## Comparison of Machine Learning Techniques in prediction of Water Quality Index (WQI)

A study on usage of machine learning techniques for predicting water quality with reduced information. 
This study only includes data from Indian lakes.Data has been collected from collected from the CPCB website under NWMP data.
Data is available to download from https://www.kaggle.com/datasets/akkshaysr/nwmp-water-quality-data-for-indian-lakes or `/data/csv` in repository.

All code used for the project is available within `/notebooks`.
* `WQI_Prediction.ipynb` is the main notebook and contains the methods used for prediction of WQI
* `effect_of_data_imbalance.ipynb` and `benchmarks.ipynb` are notebooks containing additional details used in the project.

The following python packages have been used in the code and are required to run/modify the code:
```text
pandas==1.5.3
numpy==1.23.5
matplotlib==3.6.3
seaborn==0.12.2
scikit-learn==1.2.1
torch==2.0.1
statsmodels==0.14.0
```