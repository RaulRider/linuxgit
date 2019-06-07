

# OTRO MODO ES VOLCAR A FICHERO Y LEER
# import urllib2
# import json
# subprocess.call(curl_venus + ' > venus.json' ,  shell=True)
# response = urllib2.urlopen(url)
# data = response.read()
# values = json.loads(data)

# OTRO MODO ES REQUEST
# import requests
# res = requests.get('URL')
# res.json() es el JSON

# OJO type(subprocess.run('ls' , stdout=subprocess.PIPE).stdout) = <class 'bytes'>
# OJO type(subprocess.run('ls' , stdout=subprocess.PIPE , universal_newlines=True).stdout) = <class 'str'>


import os
import subprocess
import json
import requests

# DATOS DEL NODO PRINCIPAL
venusid = '02dfec60f3cafbe1b34951073e1956e1bfd72f7302ed3e68d1f69a24a479fa9329'
venusurl = 'https://1ml.com/node/02dfec60f3cafbe1b34951073e1956e1bfd72f7302ed3e68d1f69a24a479fa9329/json/'
res = requests.get(venusurl) # res NO es un json()
venusjson = res.json()
print(venusjson['alias'])

# VOLCADO DE CHANNELS A channels.txt OJO es una lista de nodos no un JSON
subprocess.call('~/eclair/eclair-cli -p Buster1968 channels > channels.txt' ,  shell=True) # LISTA de nodos

"""

LEER ESTO: https://stackabuse.com/reading-and-writing-lists-to-a-file-in-python/



with open('data.json') as f:
    data = json.load(f)

pprint(data)

With data, you can now also find values like so:

data["maps"][0]["id"]
data["masks"]["id"]
data["om_points"]
"""

