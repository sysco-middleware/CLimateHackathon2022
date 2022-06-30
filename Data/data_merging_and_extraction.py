import glob
import json
import pandas as pd

def ConcatenateFiles():

    '''
    It merged the output json files coming from the Logic app create by Vinay & Pål
    '''

    data=[]

    for f in glob.glob("./WithCoordinates_Finnyeardata_WholeNorway/*.json"):
        with open(f) as infile:
            data.extend(json.load(infile))
            print(f)

    with open("merged_files.json",'w') as outfile:
        json.dump(data, outfile)

    print(len(data))

    #return data


def SelectPropertyType():
    '''
    -1- Keeps only the property types: Leilighet, Enebolig, Rekkehus, Tomannsbolig as
    they are the ones highly populated and with a very high correlation with the energy labels ( 80/90 %)    
    '''
    
    
    df = pd.read_json('./merged_files.json')
    for element in ['Gårdsbruk/Småbruk', 'Bygård/Flermannsbolig', 'Andre',
                    'Produksjon/Industri', 'Annet fritid', 'Garasje/Parkering']:
        df.drop(df[df['property_type_description'] == element].index, inplace=True)



    df.to_parquet('output_data_process.parquet')



if __name__ == '__main__':
    ConcatenateFiles()
    SelectPropertyType()

    print('you rock')