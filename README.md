# CLimateHackathon2022


### goal 

Further develops the concept developed during the hackathon to a MVP for the meeting with DNB on the 18.08.

### deliverable

A dashboard with the area of interests for DNB with contextualisation of the data. 


## the dataset 

The data have been taken from house ads from Finn.no 

### Cleaning of the data

#### type of ads 

Removing of 'Gårdsbruk/Småbruk', 'Bygård/Flermannsbolig', 'Andre','Produksjon/Industri', 'Annet fritid', 'Garasje/Parkering'

**=> keeping of only 'Leilighet', 'Enebolig', 'Rekkehus', 'Tomannsbolig' due to high correlation and high population**

#### Energy label population in the dataset

![Energy label population](/illustrations/nr_ads_by_energetic_labels.png) 


#### Building year 

The baseline correlation between the energy label and the building year is ≈73%. BVy categorizing the ads according to the TEK laws it increases to ≈82% and it is even higher when considering specific type of ads after the TEK categorization (coef fig).


![](/illustrations/nr_ads_by_TEK_cat.png)

![](/illustrations/nr_ads_by_TEK_and_labels.png)

The distribution of the ads by TEk category and energy label is somehow similar to the [energy report] (https://www.energimerking.no/no/energimerking-bygg/energimerkestatistikk/#mainContent) provided by ENOVA page 9

![](/illustrations/correlation_by_type_building.png)

The correlation with the energy label is even higher when considering specific type of ads after the TEK categorization (coef fig above).

### Modelling

#### removing features

- removing of 'from_year','to_year','number_of_bedrooms','ad_type','owner_type_description','local_area_name'

#### feature selection 
List of the features selected for the next step: modelling
ad_id            0.036030
energy_label     1.000000
lat              0.052593
lon              0.065122
size_from        0.099158
byggear_cat     -0.824377
ownership_cat    0.067418
elevation        0.026815


