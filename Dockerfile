FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

# Устанавливаем время
ENV TZ=Europe/Moscow

# Установка необходимых зависимостей
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    tzdata \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY .env .

EXPOSE 8000

# Запуск миграций и бота
CMD ["sh", "-c", "alembic upgrade head && python bot.py"]
