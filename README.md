# networkschoolapi
api для Электронной школы


# Использование
```python
from networkschool import NetworkSchool
import asyncio

async def main():
    async with NetworkSchool("адрес школы(вместе с https:// http://",
        "логин",
        "пароль",
        ) as api:
            # ваш код живет тут
asyncio.run(main())
```

# Методы
## Получение дневника
```python
diary = await api.get_diary()
```
**Параметры**
| Параметр | Значение| По умолчанию |
|----------------|:---------:|----------------:|
| from_date(необязательно) | Дата с которой нужно получить дневник(datetime) | День начала недели |
| to_date(необзательно) | Дата до которой нужно получить дневник(datetime) | День конца недели |


# Авторы
Нашел методы api: https://vk.com/mironovmeow

# Продукты
Бот в telegram(также есть поддержка других дневников): http://t.me/multidnevnikbot
