import json
import time
import random
import json
from locust import HttpUser, task, tag, between
from GenerationData import GenerationData


# Статичные данные для тестирования
names_avto = ['3EXK13', '5PTB95', 'r777os', 'r777os']

recommendations = ["Зарядить аккумулятор", "Необходимо заправиться", "Уже ничем не помочь"]


class RESTServerUser(HttpUser):
    """ Класс, эмулирующий пользователя / клиента сервера """
    wait_time = between(1.0, 5.0)       # время ожидания пользователя перед выполнением новой task

    # Адрес, к которому клиенты (предположительно) обращаются в первую очередь (это может быть индексная страница, страница авторизации и т.п.)
    def on_start(self):
        self.client.get("/docs")    # базовый класс HttpUser имеет встроенный HTTP-клиент для выполнения запросов (self.client)

    @tag("get_all_task")
    @task(3)
    def get_all_task(self):
        """ Тест GET-запроса (получение нескольких записей оо автомобиле по статусу ошибки) """
        errors_id = random.randint(1, 3)      # генерируем случайный id ошибки в диапазоне от 1 до 3
        with self.client.get(f'/api/car/{errors_id}',
                             catch_response=True,
                             name='/api/car/{errors_id}') as response:
            # Если получаем код HTTP-код 200, то оцениваем запрос как "успешный"
            if response.status_code == 200:
                response.success()
            # Иначе обозначаем как "отказ"
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("get_one_task")
    @task(10)
    def get_one_task(self):
        """ Тест GET-запроса (получение одной об автомобиле по его госномеру) """
        name_id = random.randint(0, 3)
        name = names_avto[name_id]
        with self.client.get(f'/api/car?name={name}',
                             catch_response=True,
                             name='/api/car?name={name}') as response:
            # Если получаем код HTTP-код 200 или 204, то оцениваем запрос как "успешный"
            if response.status_code == 200 or response.status_code == 204:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("post_task")
    @task(1)
    def post_task(self):
        """ Тест POST-запроса (создание записи об автомобиле) """
        car = GenerationData()
        test_data = {'name': car.getName(),
                     'coord_x': car.getX(),
                     'coord_y': car.getY(),
                     'acc': car.getAccCharge(),
                     'oil': car.getVolumeOil(),
                     'fuel': car.getVolumeFuel(),
                     'temp': car.getEngineTemp(),
                     'fuel_consumption': car.getFuelConsumption(),
                     'milease': car.getMilease(),
                     'status': random.randint(1, 3)}
        post_data = json.dumps(test_data)       # сериализуем тестовые данные в json-строку
        # отправляем POST-запрос с данными (POST_DATA) на адрес <SERVER>/api/car
        with self.client.post('/api/car',
                              catch_response=True,
                              name='/api/car', data=post_data,
                              headers={'content-type': 'application/json'}) as response:
            # проверяем, корректность возвращаемого HTTP-кода
            if response.status_code == 201:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')

    @tag("put_task")
    @task(3)
    def put_task(self):
        """ Тест PUT-запроса (обновление записи оо автомобиле) """
        name_id = random.randint(0, 3)
        name = names_avto[name_id]
        status = random.randint(1, 3)

        test_data = {'name': name,
                     'status': status}
        
        put_data = json.dumps(test_data)
        # отправляем PUT-запрос на адрес <SERVER>/api/car
        with self.client.put(f'/api/car?name={name}&status={status}',
                             catch_response=True,
                             name='/api/car?name={name}&status={status}',
                             data=put_data,
                             headers={'content-type': 'application/json'}) as response:
            if response.status_code == 202:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')
          
          
    @tag("put_task_mil")
    @task(3)
    def put_task_mil(self):
        """ Тест PUT-запроса (обновление пробега у автомобиля) """
        name = "1YHY33"
        milease = random.randint(10000, 200000)

        test_data = {'name': name,
                     'milease': milease}
        
        put_data = json.dumps(test_data)
        # отправляем PUT-запрос на адрес <SERVER>/api/car
        with self.client.put(f'/api/carmil?name={name}&milease={milease}',
                             catch_response=True,
                             name=f'/api/carmil?name={name}&milease={milease}',
                             data=put_data,
                             headers={'content-type': 'application/json'}) as response:
            if response.status_code == 202:
                response.success()
            else:
                response.failure(f'Status code is {response.status_code}')

