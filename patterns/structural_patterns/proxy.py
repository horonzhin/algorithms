# Заместитель (Proxy) — структурный паттерн
# Позволяет подставлять вместо реальных объектов специальные объекты-заменители. Эти объекты перехватывают вызовы
# к оригинальному объекту, сами создают экземпляр оригинального объекта, позволяя сделать что-то до или после передачи
# вызова оригиналу.
#
# Cхожий с фасадом или адаптером, только у прокси интерфейс полностью повторяет интерфейс замещающего объекта.
# Используется для отложенных действий над самим объектом, ограничения доступа к объекту, логирования и т.д.
########################################################################################################################
# Применяется:
# - Ленивая инициализация (виртуальный прокси). Когда у вас есть тяжёлый объект,
# грузящий данные из файловой системы или базы данных.
# - Защита доступа (защищающий прокси). Когда в программе есть разные типы пользователей,
# и вам хочется защищать объект от неавторизованного доступа.
# - Локальный запуск сервиса (удалённый прокси). Когда настоящий сервисный объект находится на удалённом сервере.
# - Логирование запросов (логирующий прокси). Когда требуется хранить историю обращений к сервисному объекту.
# - Кеширование объектов («умная» ссылка). Когда нужно кешировать результаты запросов клиентов и
# управлять их жизненным циклом.
########################################################################################################################
# Плюсы:
# - Позволяет контролировать сервисный объект незаметно для клиента.
# - Может работать, даже если сервисный объект ещё не создан.
# - Может контролировать жизненный цикл служебного объекта.
########################################################################################################################
# Минусы:
# - Усложняет код программы из-за введения дополнительных классов.
# - Увеличивает время отклика от сервиса.
########################################################################################################################

import random
import time
from abc import ABC, abstractmethod
from typing import Dict
from uuid import uuid4


class User:
    """Пользователь"""

    def __init__(self):
        self._user_id = random.randint(0, 100)

    @property
    def user_id(self):
        return self._user_id


class Token:
    """Токен"""

    def __init__(self, key, time_to_live):
        self.key = key
        self.time_to_live = time_to_live
        self.create_at = time.time()

    @property
    def is_expired(self):
        """Проверка валидности токена"""
        return time.time() - self.create_at > self.time_to_live


class AbstractTokenManager(ABC):
    """Интерфейс менеджера токенов"""

    @abstractmethod
    def create_token(self, user_id):
        """Создание нового токена"""
        pass


class TokenManager(AbstractTokenManager):
    """Реальный менеджер токенов №1"""
    time_to_live = 3

    def create_token(self, user_id):
        """Создание нового токена"""
        key = self._get_token_from_db(user_id)
        print(f'Токен для пользователя {user_id}: {key}')
        return Token(key, self.time_to_live)

    def _get_token_from_db(self, user_id):
        """Обращение к БД для получения токена"""
        print(f'Запрос токена из БД для пользователя: {user_id}')
        time.sleep(2)
        print(f'Токен для пользователя "{user_id}" получен!')
        return uuid4()


class CachedTokenManager(AbstractTokenManager):
    """Прокси в котором кэшируются токены пользователей"""

    def __init__(self, token_manager: TokenManager):
        self.token_manager = token_manager
        self.cache: Dict[int, Token] = {}

    def create_token(self, user_id):
        """Перед обращением к БД и созданием нового токена проверим есть ли указанный токен в кэше"""
        if user_id in self.cache:
            cache_token: Token = self.cache[user_id]
            if cache_token.is_expired:
                print('Токен устарел. Обновляю Токен!!!')
                self.refresh_token(user_id)
        else:
            self.refresh_token(user_id)

        return self.cache[user_id]

    def refresh_token(self, user_id):
        """Обновление токена"""
        self.cache[user_id] = self.token_manager.create_token(user_id=user_id)


if __name__ == '__main__':
    user = User()
    token_manager = TokenManager()
    time_start = time.time()
    token_manager.create_token(user.user_id)
    token_manager.create_token(user.user_id)
    print(f'Время 2-х запросов без использования Proxy: {time.time() - time_start:0.4f} секунд')  # ~ 4 сек.

    print('Ждем 3 секунды для протухания токена')
    time.sleep(3)

    token_manager = CachedTokenManager(TokenManager())
    time_start = time.time()
    token_manager.create_token(user.user_id)
    token_manager.create_token(user.user_id)
    token_manager.create_token(user.user_id)
    token_manager.create_token(user.user_id)
    print(f'Время 4-х запросов с Proxy: {time.time() - time_start:0.4f} секунд')  # ~ 2 сек.
