import json
import boto3
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen

def f():
    
    fecha_actual = datetime.today().strftime('%Y-%m-%d')

    url = "https://casas.mitula.com.co/searchRE/nivel1-Cundinamarca/nivel2-Bogot%C3%A1/orden-0/op-1/m2_min-1/m2_max-200/hab_min-1/ban_min-1/q-bogot%C3%A1?req_sgmt=REVTS1RPUDtVU0VSX1NFQVJDSDtTRVJQOw=="

    with urlopen(url) as response:
        body = response.read()
    
    boto3.client('s3').put_object(Body=body,Bucket='landing-casas-20020503',Key= str(fecha_actual) + ".html")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }