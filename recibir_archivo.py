import json
import boto3
from datetime import datetime
from bs4 import BeautifulSoup

def f():
    
    nombre = str(datetime.today().strftime('%Y-%m-%d'))
    
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('landing-casas-20020503')
    obj = bucket.Object(str(nombre + ".html"))
    body = obj.get()['Body'].read()
    
    html = BeautifulSoup(body, 'html.parser')

    data_casas = html.find_all('div',class_='listing listing-card')
    data_titulo = html.find_all('div',class_='listing-card__title')
    data_precio = html.find_all('div',class_='price')
    
    fecha_actual = datetime.today().strftime('%Y-%m-%d')
    
    linea_0 = "FechaDescarga, Info, Valor, NumHabitaciones, NumBanos, mts2\n"
    
    for i in range(len(data_casas)):
        linea_0 = linea_0 + fecha_actual + "," + str(data_titulo[i].text) + "," + str(data_precio[i].text) + "," + str(data_casas[i]['data-rooms']) + "," + str(data_casas[i].find_all('div', class_='listing-card__properties')[0].find_all('span')[1].text[:1]) + "," + str(data_casas[i].find_all('div', class_='listing-card__properties')[0].find_all('span')[2].text) + "\n"
   
            
    boto3.client('s3').put_object(Body=linea_0,Bucket='casas-fina-20020503',Key=str(nombre+".csv"))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }