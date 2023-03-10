import os
from decouple import config
from pymongo import MongoClient
from pymongo.collection import Collection


class MongoDBInfrastructure:
    __mongo_client = None

    def __init__(self):
        mongo_connection_string = config("MONGODB_CONNECTION_STRING")
        self.__mongo_client = MongoClient(mongo_connection_string)

    def get_list_database_names(self):
        dbs = self.__mongo_client.list_database_names()

        return dbs

    def get_db_connection(self) -> Collection:
        db_name = config("DB_NAME")

        db_connection = self.__mongo_client[db_name]

        return db_connection[config("DB_COLLECTION_NAME")]
