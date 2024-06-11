FROM python:3.12-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо poetry.lock та pyproject.toml
COPY poetry.lock pyproject.toml /app/

# Копіюємо весь проект
COPY . .

# Запускаємо ваш проект
CMD ["poetry", "run", "python", "my_project.py"]