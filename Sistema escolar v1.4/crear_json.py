import json

nuevo = {

    'contraseñas': {

        'rector': 202600,
        'coordinador': 202601,
        'docente':202614
    }
    
}

with open('logins.json', 'w') as d:
    json.dump(nuevo,d, indent=4)