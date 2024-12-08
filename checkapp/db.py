from tinydb import TinyDB

class TinyDBSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if TinyDBSingleton._instance is None:
            TinyDBSingleton._instance = TinyDB('db.json')
        return TinyDBSingleton._instance

db = TinyDBSingleton.get_instance()