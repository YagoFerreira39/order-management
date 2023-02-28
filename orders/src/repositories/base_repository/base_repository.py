from src.infrastructure.mongodb.mongodb_infrastructure import MongoDBInfrastructure


class BaseRepository:
    __mongodb_infrastructure = MongoDBInfrastructure()
    _mongodb_connection = __mongodb_infrastructure.get_db_connection()
