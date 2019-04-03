import json
import sys

from pymongo import MongoClient


def main():
    client = MongoClient('localhost', 27017)
    db = client['regions_db']
    collection_regions = db['regions']

    with open('regions.json') as f:
        file_data = json.load(f)

    collection_regions.insert_many(file_data)

    collection_maires = db['maires']

    with open('maires.json') as f:
        file_data = json.load(f)

    collection_maires.insert_many(file_data)

    collection_departements = db['departements']

    with open('maires.json') as f:
        file_data = json.load(f)

    collection_departements.insert_many(file_data)

    client.close()


if __name__ == "__main__":
    sys.exit(main())
