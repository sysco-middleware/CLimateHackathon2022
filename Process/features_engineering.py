import pandas as pd
from prompt_toolkit import prompt
import requests

GOOGLE_API= ""
with open("Google_api_key.txt", 'r') as f:
            # It's assumed our file contains a single line,
            # with our API key
            GOOGLE_API = f.read().strip()

####function 

def CategoriseBuilding(year):

    '''Categorise what TEK a property follows based on the year of the building
In Norway the laws for the buildings were: TEK69 TEK87, TEK97,TEK07,TEK10, TEK17. Before 1969: No TEK

{0:'no TEK',1:'TEK69',2:'TEK87',3:'TEK97',4:'TEK07',5:'TEK10',6:'TEK17'}'''
    
    if year < 1969:
        byggear_cat = 0
    elif year < 1987:
        byggear_cat = 1
    elif year < 1997:
        byggear_cat = 2
    elif year < 2007:
        byggear_cat = 3
    elif year < 2010:
        byggear_cat = 4
    elif year < 2017:
        byggear_cat = 5
    elif year >= 2017:
        byggear_cat = 6

    return byggear_cat


def GetElevation(coordinates):
    lat, lon = coordinates.split(',')
    url = f"https://maps.googleapis.com/maps/api/elevation/json?locations={lat},{lon}&key={GOOGLE_API}"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    #print(response.text)
    response=response.json()
    return response['results'][0]['elevation']    



def FeaturesEngineering():
    #load the data 
    df = pd.read_parquet('Data/output_data_process.parquet')

    #Fix NaN
    df = df.drop(['local_area_name'], axis = 1)
    df = df.dropna(axis=0)

    null_values = df.isnull().sum().sum()
    print(f'In the dataset there are {null_values} null values')
    #building years as nominal TEK category
    df['byggear_cat'] = df['to_year'].apply(lambda x: CategoriseBuilding(x))

    #ownership as nominal category
    dict_ownership = {'Eier (Selveier)':1,'Andel':2,'Aksje':3,'Obligasjon':4}
    df['ownership_cat'] = df['owner_type_description'].map(dict_ownership)


    #property type as nominal 
    dict_property_type_cat = {'Leilighet':1,'Enebolig':2,'Rekkehus':3,'Tomannsbolig':4}
    df['property_type_cat']= df['property_type_description'].map(dict_property_type_cat)

    #GetElevation
    df['lat,lon'] = df['lat'].astype(str)+','+ df['lon'].astype(str)
    
    #RUN ONLY if needed, takes 20min ( 8 ads per seconds)
    #df['elevation'] = df['lat,lon'].apply(lambda x: GetElevation(x))


    #select the features and save output
    
    df.to_parquet('Process/output_engineering.parquet')
    print('hello world, you are done')








if __name__ == '__main__':
    FeaturesEngineering()