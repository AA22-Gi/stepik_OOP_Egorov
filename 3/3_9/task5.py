"""
Очень часто настройки приложения выносят в отдельный файл и при старте приложения подгружают из него значения.

Вам необходимо разработать простой конфигурационный менеджер для вашего приложения.
Для этого необходимо реализовать класс AppConfig, который предоставляет методы
для загрузки конфигурации из JSON-файла и получения значений конкретных параметров.

В классе AppConfig должно быть реализовано следующее:

    1)  метод load_config, который загружает конфигурацию из указанного JSON-файла

    2)  метод get_config, который принимает ключ и возвращает соответствующее значение
        из загруженной конфигурации. Если ключ не найден, метод должен возвращать None.
        Также необходимо предоставить возможность обращаться к вложенным параметрам через точку.

Вам будет предоставлен файл 'app_config.json', который имеет следующее содержимое
{
    "database": {
        "host": "127.0.0.1",
        "port": 5432,
        "database_name": "postgres_db",
        "user": "owner",
        "password": "ya_vorona_ya_vorona"
    },
    "api_key": "hUFHu834837248jhoiHF89",
    "log_level": "debug",
    "max_connections": 10
}

Необходимо реализовать возможность вызова перечисленных методов как через класс, так и через экземпляр.
Также необходимо обеспечить распространение значений параметров на все экземпляры класса AppConfig.
Это значит, что все экземпляры AppConfig должны иметь одинаковые значения конфигурации приложения.

Выбор реализации данной задачи остается за вами.
"""


class AppConfig:
    _data = None  # Исправлено на _data

    @classmethod
    def load_config(cls, file_json):
        with open(file_json, 'r') as file:
            cls._data = json.load(file)

    @classmethod
    def get_config(cls, key):
        if cls._data is None:  # Исправлено здесь
            return None

        keys = key.split('.')
        data_value = cls._data

        for k in keys:
            if isinstance(data_value, dict) and k in data_value:
                data_value = data_value[k]
            else:
                return None

        return data_value


if __name__ == '__main__':
    import json

    # Загрузка конфигурации при запуске приложения
    AppConfig.load_config('app_config.json')

    # Получение значения конфигурации
    assert AppConfig.get_config('database') == {
        'host': '127.0.0.1', 'port': 5432,
        'database_name': 'postgres_db',
        'user': 'owner',
        'password': 'ya_vorona_ya_vorona'}
    assert AppConfig.get_config('database.user') == 'owner'
    assert AppConfig.get_config('database.password') == 'ya_vorona_ya_vorona'
    assert AppConfig.get_config('database.pass') is None
    assert AppConfig.get_config('password.database') is None

    config = AppConfig()
    assert config.get_config('max_connections') == 10
    assert config.get_config('min_connections') is None

    conf = AppConfig()
    assert conf.get_config('max_connections') == 10
    assert conf.get_config('database.user') == 'owner'
    assert conf.get_config('database.host') == '127.0.0.1'
    assert conf.get_config('host') is None

    print('Good')
