# FOODGRAM
## Описание проекта
Проект foodgram позволяет создавать "рецепты". Рецепт состоит из ингредиентов, наименования, картинки, описания, все поля редактируемы.
### Содержанеие

- [Технологии](#tech)
- [Начало](#begining)
- [Запуск через docker](#docker)
- [Основные команды](#commands)
- [FAQ](#faq)
- [Комнада проекта](#team)

## <a name="tech">Технологии</a>

- [Green API](https://green-api.com/docs/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Docker](https://www.docker.com/)

## <a name="begining">Начало работы</a>

### Начало работы

Зарегестрируйтесь на Green API:

https://green-api.com/docs/before-start/

В файле .env
```
API_TOKEN_INSTANCE = <ваш токен>
API_ID_INSTANCE = <ваш ID инстанса>
```

## <a name="docker">Запуск через docker</a>

Зайти в корневую директорию. 
Запустить docker файл:

```
docker build -t whatsapp-bot .
docker-compose up --build
```
или
```
docker compose -f docker-compose.yml up -d
```

Если захотите отключить бота
Введите следующие команды

```
docker compose -f docker-compose.yml down -v
```
## <a name="commands">Основные команды</a>
- **"help"** 
Выведет пример запроса на добавление Напоминания
- **"remember message:'<your_commnad>' time:'%H:%M'"** 
Пример запроса на запоминание (время в 24 часовом формате)
- **"remind"** 
Выведет все Ваши напоминания
## <a name="faq">FAQ</a>

### Работает?

Да, работает

## <a name="team">Команда проектка</a>

- Паршин Денис - backend developer