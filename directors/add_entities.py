import names
import random
import requests
import json

def add_entities():
    args = dict()
    for i in range(1, 150):
        args['name'] = names.get_first_name()
        args['surname'] = names.get_last_name()
        args['birthdate'] = str(random.randrange(1950,1980)) + '-' + str(random.randrange(1,12)) + '-' + str(random.randrange(1,31))
        args['year'] = random.randint(1950, 2010)
        args['score'] = str(random.randrange(100, 200)/5)
        r = requests.post('http://localhost:9090/api/directors/?format=json', json=args)
        print(json.dumps(args))
        print(r.status_code)


if __name__ == '__main__':
    add_entities()