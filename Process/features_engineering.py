import pandas as pd



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





def FeaturesEngineering():
    
    df = pd.read_parquet('Data/output_data_process.parquet')
    df['byggear_cat'] = df['to_year'].apply(lambda x: CategoriseBuilding(x))

    print('hello world')








if __name__ == '__main__':
    FeaturesEngineering()