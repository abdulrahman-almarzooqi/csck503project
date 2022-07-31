# csck503project

This repository was created for the masters group assignment within the Machine Learning in Practice university module at the University of Liverpool.

Project Team Members:
- AbdulRahman AlMarzooqi
- Cheylea Hopkinson
- Alfredo Papaseit

The purpose of this project is to examine the datasets found on the [London Atmospheric Emmissions Inventory](https://data.london.gov.uk/dataset/london-atmospheric-emissions-inventory-2013) website and analyse and derive predictive insight from the year 2013, predicting at a micro-level.

## Scenario
> You have been engaged as a contract data scientist by Athana Data Science Services (ADSS), a small company specialising in the provision of data science consultancy services to public and private sector organisations. ADSS have just been awarded a contract by a government department (the Department of Environment) to help with the development of machine learning-based models for predicting atmospheric emissions (and pollution) from data gathered by various borough and county environment monitoring units. Your team leader wants you to assist with this project, and you will be required to carry out a number of tasks using the Anaconda/Scikit-Learn Python ML framework and its components.


## Directory
The full assignment can be found within the jupyter notebook `LAEI_PREDICT_ATMOSPHERIC_EMISSIONS.ipynb` This file can also be visualised using https://nbviewer.org/ and the repository link.

This repository contains the main jupyter notebook file alongside a datasets folder, `README.md` and `requirements.txt` files.

```bash
C:.
├───LICENSE
├───README.md
├───LAEI_PREDICT_ATMOSPHERIC_EMISSIONS.ipynb
├───requirements.txt
└───datasets
```

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.
```bash
python -m pip install -r requirements.txt
```

## Preparing the datasets
In order to run this notebook, you require two datasets from the [London Atmospheric Emmissions Inventory](https://data.london.gov.uk/dataset/london-atmospheric-emissions-inventory-2013)
These are large files available for download directly from the site.

**Step One:** Download and extract the following files:
- LAEI2013_2013_AADT-VKM.xlsx found in `1 - Supporting Information`
- LAEI2013_MajorRoads_EmissionsbyLink_2013 found in `3 - Detailed Road Transport`

**Step Two:** Add the files into the datasets folder in the project folder.

## Contributing
Pull requests permitted with full documentation.