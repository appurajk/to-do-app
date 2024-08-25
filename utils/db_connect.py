from pymongo import MongoClient
import threading

class Dbconnect:
    '''Class to connect to MongoDB using Singleton pattern.'''

    _instance = None
    _lock = threading.Lock()  # Lock to ensure thread safety during instance creation
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Dbconnect, cls).__new__(cls)
                cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        '''Initialize the MongoDB connection.'''
        MONGO_DB_URL = '172.25.232.220'
        MONGO_DB_PORT = '27017'
        self.client = MongoClient(MONGO_DB_URL, int(MONGO_DB_PORT), uuidRepresentation="standard")
        self.db = self.client["todos"]

    @staticmethod
    def mongodb_conn_get():
        '''Get the database instance.'''
        return Dbconnect().db