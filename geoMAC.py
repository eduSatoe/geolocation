#-----------------------------------------------------------------------
#Nombre: geoMAC.py
#Descripción: Script de geolocalización basado en MACs de puntos de acceso
#Uso: Rellena los datos de los wifiAccessPoints más próximos del usuario
#			macAddress: Identificador de celda donde estás conectado CID
#			signalStrength: Intensidad de señal del AP en db
#			signalToNoiseRatio: SNR o proporción señal/ruido
#Autor:@edusatoe
#------------------------------------------------------------------------

import requests

datos = {
  "considerIp": "false",
  "wifiAccessPoints": [
    {
        "macAddress": "68:bc:0c:64:e6:3f",
        "signalStrength": -48,
        "signalToNoiseRatio": 0
    },
    {
        "macAddress": "c8:f9:f9:d4:80:df",
        "signalStrength": -49,
        "signalToNoiseRatio": 0
    }
  ]
}

url = "https://www.googleapis.com/geolocation/v1/geolocate?key=YOUR_API_KEY"
response = requests.post(url, json=datos)

print "Latitud:"+str(response.json()['location']['lat'])
print "Longitud:"+str(response.json()['location']['lng'])
print "Precision:"+str(response.json()['accuracy'])

