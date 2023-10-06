from decouple import config as config

class APPENV:
    _SQLHOST = config('SQLHOST')
    _SQLUSER = config('SQLUSER')
    _SQLUSERPW = config('SQLUSERPW')
    _SQLDB = config('SQLDB')
    _SQLPORT = config('SQLPORT')

    def __init__(self) -> None:
        self._SQLHOST = config('SQLHOST')
        self._SQLUSER = config('SQLUSER')
        self._SQLUSERPW = config('SQLUSERPW')
        self._SQLDB = config('SQLDB')
        self._SQLPORT = config('SQLPORT')

    @classmethod
    def get_sql(cls) -> dict:
        sql_config = {
            "host":cls._SQLHOST,
            "port":cls._SQLPORT,
            "user":cls._SQLUSER,
            "password":cls._SQLUSERPW,
            "db":cls._SQLDB,
        }
        return sql_config


