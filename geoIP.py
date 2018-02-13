#-----------------------------------------------------------------------
#Nombre: geoIP.py
#Descripción: Script de geolocalización basado en la IP del usuario
#Uso: Simplemente ejecutar y te geolocaliza según tu IP pública
#			considerIp: true/false para determinar si usa la IP o no
#Autor:@edusatoe
#------------------------------------------------------------------------
import requests

datos = {
"considerIp": "true"
}

url = "https://www.googleapis.com/geolocation/v1/geolocate?key=YOUR_API_KEY"
response = requests.post(url, json=datos)

print "Latitud:"+str(response.json()['location']['lat'])
print "Longitud:"+str(response.json()['location']['lng'])
print "Precision:"+str(response.json()['accuracy'])

