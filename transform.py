'''
    File name: data_transform_test.py
    Author: Cheylea Hopkinson
    Python Version: 3.9.12
'''
# Extracting Feature Columns #
# =============================================================================

# Import Packages
import numpy as np
import pandas as pd
from sklearn import preprocessing
import seaborn as sns # for data visualization
import matplotlib.pyplot as plt # for data visualization

# Import Data
data = pd.read_csv('datasets\df_merged_RoadTrafficData_Emissions.csv', encoding='utf-8')


# Count of unique values for discrete columns
data_group_discrete = data.groupby(['rtd_grid_exactcut_id'])[['rtd_toid',
                                                              'rtd_location_exactcut',
                                                              'rtd_boroughname_exactcut',
                                                              'rtd_tlrn',
                                                              'rtd_motorwaynumber']].agg(pd.Series.nunique)
print(data_group_discrete.head())

# Check whether or not a grid contains any discrete values
dummies_location_exactcut = pd.get_dummies(data['rtd_location_exactcut'], prefix='rtd_location_exactcut')
dummies_boroughname_exactcut = pd.get_dummies(data['rtd_boroughname_exactcut'], prefix='rtd_boroughname_exactcut')
dummies_tlrn = pd.get_dummies(data['rtd_tlrn'], prefix='rtd_tlrn')
dummies_motorwaynumber = pd.get_dummies(data['rtd_motorwaynumber'], prefix='rtd_motorwaynumber')

data_group_dummies = data['rtd_grid_exactcut_id']
data_group_dummies = pd.concat([data_group_dummies, dummies_location_exactcut, dummies_boroughname_exactcut, dummies_tlrn, dummies_motorwaynumber], axis=1)
data_group_dummies = data_group_dummies.groupby(['rtd_grid_exactcut_id']).agg('max')

print(data_group_dummies.head())

# Calculate various aggregations of numerical data
data_group_numeric = data.groupby(['rtd_grid_exactcut_id'])[['rtd_aadt_motorcycle',
                                                              'rtd_aadt_taxi',
                                                              'rtd_aadt_pcar',
                                                              'rtd_aadt_dcar',
                                                              'rtd_aadt_plgv',
                                                              'rtd_aadt_dlgv',
                                                              'rtd_aadt_ltbus',
                                                              'rtd_aadt_coach',
                                                              'rtd_aadt_rigid2axle',
                                                              'rtd_aadt_rigid3axle',
                                                              'rtd_aadt_rigid4axle',
                                                              'rtd_aadt_artic3axle',
                                                              'rtd_aadt_artic5axle',
                                                              'rtd_aadt_artic6axle',
                                                              'rtd_aadt_electriccar',
                                                              'rtd_aadt_electriclgv',
                                                              'rtd_aadt_total',
                                                              'rtd_speed_(kph)',
                                                              'rtd_length_(m)',]].agg(['mean', 'sum', 'min', 'max'])

data_group_numeric.columns = data_group_numeric.columns.map('_'.join)
print(data_group_numeric.head())

# Normalise count of unique values for discrete columns
for column in data_group_discrete:
    values = data_group_discrete[column].values
    values = values.reshape(-1, 1)
    values_n = preprocessing.MinMaxScaler().fit_transform(values)
    data_group_discrete[column] = pd.DataFrame(values_n)

print(data_group_discrete.head())

# Normalise various aggregations of numerical data
for column in data_group_numeric:
    values = data_group_numeric[column].values
    values = values.reshape(-1, 1)
    values_n = preprocessing.MinMaxScaler().fit_transform(values)
    data_group_numeric[column] = pd.DataFrame(values_n)

print(data_group_numeric.head())


# Join all Dataframes containing potential features
data_new = pd.concat([data_group_discrete, data_group_dummies, data_group_numeric], axis=1)
print(data_new.head())


# Get labelled column to train on
data_new['total'] = data[['ebl_ebl_ebl_total_emissions_co2',
                          'ebl_ebl_ebl_total_emissions_nox',
                          'ebl_ebl_ebl_total_emissions_pm10_brake',
                          'ebl_ebl_ebl_total_emissions_pm10_exhaust',
                          'ebl_ebl_ebl_total_emissions_pm10_resusp',
                          'ebl_ebl_ebl_total_emissions_pm10_tyre',
                          'ebl_ebl_ebl_total_emissions_pm25_brake',
                          'ebl_ebl_ebl_total_emissions_pm25_exhaust',
                          'ebl_ebl_ebl_total_emissions_pm25_resusp',
                          'ebl_ebl_ebl_total_emissions_pm25_tyre',]].sum(axis=1)

# Export final dataset read for Machine Learning examination
data_new.to_csv('datasets\data_transformed.csv')

# Feature Examination #
# =============================================================================

# Generate correlation heatmap
data_new_heat = data_new.corr()
sns.heatmap(data_new_heat,annot=True,cmap='coolwarm')