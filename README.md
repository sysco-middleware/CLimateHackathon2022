# CLimateHackathon2022


### goal 

Further develops the concept developed during the hackathon to a MVP for the meeting with DNB on the 18.08.

### deliverable

A dashboard with the area of interests for DNB with contextualisation of the area ( type of heating, socioeconomic info of the neighborhood). 


## the dataset 

The data have been taken from Finn.no 

### Cleaning of the data

#### type of ads 

Removing of 'Gårdsbruk/Småbruk', 'Bygård/Flermannsbolig', 'Andre','Produksjon/Industri', 'Annet fritid', 'Garasje/Parkering'

**=> keeping of only 'Leilighet', 'Enebolig', 'Rekkehus', 'Tomannsbolig' due to high correlation and high population**

#### Energy label population in the dataset

![Energy label population](/illustrations/nr_ads_by_energetic_labels.png) 



#### Building year 

The baseline correlation between the energy label and the building year is ≈73%. BVy categorizing the ads according to the TEK laws it increases to ≈82% and it is even higher when considering specific type of ads after the TEK categorization (coef fig).


![](/illustrations/nr_ads_by_TEK_cat.png)

![](/illustrations/correlation_by_type_building.png)

The correlation with the energy label is even higher when considering specific type of ads after the TEK categorization (coef fig above).

##### Anomalies? 

![](/illustrations/nr_ads_by_TEK_and_labels.png)
*to understand (TEK category, energy label)*

- {0:'no TEK',1:'TEK69',2:'TEK87',3:'TEK97',4:'TEK07',5:'TEK10',6:'TEK17'}

- {1:A,2:B,3:C,4:D,5:E,6:F,7:G}


The distribution of the ads by TEk category and energy label is somehow similar to the [energy report](https://www.energimerking.no/no/energimerking-bygg/energimerkestatistikk/#mainContent) provided by ENOVA page 9. 


*But* 
In the category "no TEK" there are some goods qualified as energy effective, they have been renovated. On the contrary, there are goods in the category TEK17 but still but energy label such as F or G, 2 cases:
1. either the building is effectively >2017 and no well isolated
2. Apartment renovated and the real estate agency used the date of the renovation and not of the building



### Feature Selection


#### features selection 
List of the features selected for the next step: **modelling**


**Features         Correlation**

lat                  0.052593
lon                  0.065122
size_from            0.099158
byggear_cat         -0.824377
ownership_cat        0.067418
property_type_cat    0.105778
energy_label         1.000000


*extra:*
ad_id            0.036030   <- to keep track of it.



