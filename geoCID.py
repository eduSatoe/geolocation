#-----------------------------------------------------------------------
#Nombre: geoCID.py
#Descripción: Script de geolocalización basado en torres de telefonía
#Uso: Rellena los datos del cellTowers más cercano: 
#			cellID: Identificador de celda donde estás conectado CID
#			locationAreaCode: Código de área LAC (Local Area Code) o TAC (Tracking Area Code)
#			mobileCountryCode: Código del pais MCC, 214 para España
#			mobileNetworkCode: Código de red móvil MNC, 01 para vodafone
#
#Documentación de la API: https://developers.google.com/maps/documentation/geolocation/overview
#
#Autor:@edusatoe
#------------------------------------------------------------------------
import requests

datos = {
  "considerIp": "false",
	"cellTowers": [
		{
		  "cellId": 73628675,
		  "locationAreaCode": 268,
		  "mobileCountryCode": 214,
		  "mobileNetworkCode": 1
		}
	  ]
  
}

url = "https://www.googleapis.com/geolocation/v1/geolocate?key=YOUR_API_KEY"
response = requests.post(url, json=datos)

print ("Latitud:"+str(response.json()['location']['lat']))
print ("Longitud:"+str(response.json()['location']['lng']))
print ("Precision:"+str(response.json()['accuracy']))
print ("---------------------")
print ("https://www.google.com/maps/@"+str(response.json()['location']['lat'])+","+str(response.json()['location']['lng'])+",15z")
