import pandas as pd
from sodapy import Socrata


def obtener_informacion(limiteRegistros):
    
    client = Socrata("www.datos.gov.co", None)
    results = client.get("ch4u-f3i5", limit= limiteRegistros)
    resultsDf = pd.DataFrame.from_records(results)

    return resultsDf
    
    
    



