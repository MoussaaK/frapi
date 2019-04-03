import sys

from pymongo import MongoClient
from .models import Maire, Region
from .serializers import RegionSerializer, MaireSerializer


class MongoConnection(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client['regions_db']

    def get_collection(self, name):
        self.collection = self.db[name]


class LoadMaires(MongoConnection):
    def __init__(self):
        super(LoadMaires, self).__init__()
        collections = self.get_collection('maires')

    def get_data(self):
        collections = self.collections.find({})
        for collection in collections:
            maire = Maire(nom=collection['nompsn'], prenom=collection['prepsn'], situation=collection['libcsp'],
                          date_de_naissance=collection['naissance'], age=collection['csp'])
            maire.save()
            serializer = MaireSerializer(maire)


class LoadRegions(MongoConnection):
    def __init__(self):
        super(LoadRegions, self).__init__()
        collections = self.get_collection('regions')

    def get_data(self):
        collections = self.collections.find({})
        for collection in collections:
            region = Region(nom=collection['name'], code=collection['code'])
            region.save()
            serializer = RegionSerializer(region)


load_maires = LoadMaires()
load_regions = LoadRegions()
