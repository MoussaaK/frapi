import json
import sys

from pymongo import MongoClient


def main():
    client = MongoClient('localhost', 27017)
    db = client['regions_db']
    collection_regions = db['regions']

    with open('../resources/regions.json') as f:
        file_data = json.load(f)

    collection_regions.insert_many(file_data)

    collection_maires = db['maires']

    with open('../resources/maires.json') as f:
        file_data = json.load(f)

    collection_maires.insert_many(file_data)

    collection_departements = db['departements']

    with open('../resources/departments.json') as f:
        file_data = json.load(f)

    collection_departements.insert_many(file_data)

    collections = collection_maires.find({})
    # for collection in collections:
    #   maire = dict(nom=collection['nompsn'], prenom=collection['prepsn'], situation=collection['libcsp'],
    #               date_de_naissance=collection['naissance'], age=collection['csp'])
    #  print(maire)

    client.close()


if __name__ == "__main__":
    sys.exit(main())
