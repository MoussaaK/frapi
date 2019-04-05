from django.http import Http404
from pymongo import MongoClient
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Maire, Region
from .serializers import MaireSerializer, RegionSerializer
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='France Cities API')


class MaireList(APIView):
    def get(self, request):
        client = MongoClient('localhost', 27017)
        db = client['regions_db']
        maires_collection = db['maires']
        collections = maires_collection.find({})
        for collection in collections:
            Maire.objects.create(nom=collection.nompsn, prenom=collection.prepsn, situation=collection.libcsp,
                                 date_de_naissance=collection.naissance, age=collection.csp)
        maires = Maire.objects.all()
        serializer = MaireSerializer(maires, many=True)

        return Response(serializer.data,
                        HTTP_200_OK)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = MaireSerializer(data=data)
        if serializer.is_valid(data):
            serializer.save()
            return Response(serializer.data, HTTP_201_CREATED)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)


class MaireDetails(APIView):
    def get_object(self, pk):
        try:
            return Maire.objects.get(pk=pk)
        except Maire.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        serializer = MaireSerializer(self.get_object(pk=pk))
        return Response(serializer.data)

    def put(self, request, pk):
        data = JSONParser.parse(request)
        serializer = MaireSerializer(self.get_object(pk=pk), data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, HTTP_201_CREATED)
        return Response(serializer.errors,
                        HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.get_object(pk=pk).delete()
        return Response(HTTP_204_NO_CONTENT)


class RegionList(APIView):
    def get(self, request):
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        return Response(serializer.data, HTTP_200_OK)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = RegionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            HTTP_201_CREATED)
        return Response(serializer.errors,
                        HTTP_400_BAD_REQUEST)


class RegionDetails(APIView):
    def get_object(self, pk):
        try:
            return Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        serializer = RegionSerializer(self.get_object(pk=pk))
        return Response(serializer.data)

    def put(self, request, pk):
        data = JSONParser.parse(request)
        serializer = RegionSerializer(self.get_object(pk=pk), data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            HTTP_201_CREATED)
        return Response(serializer.errors,
                        HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.get_object(pk=pk).delete()
        return Response(HTTP_204_NO_CONTENT)
