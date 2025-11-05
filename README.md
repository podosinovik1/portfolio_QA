# API Testing Project


## Overview
This project contains automated tests for the public REST API available at [https://api.restful-api.dev/objects](https://api.restful-api.dev/objects). The tests validate various endpoints and functionality of the API service.


## Features
- CRUD operations testing (Create, Read, Update, Delete)
- Data validation and schema verification
- Error handling scenarios
- API response time checks


## Setup

1. **Create virtual environment**
```bash
python -m venv venv
```

2. **Activate virtual environment**
```bash
# Linux/MacOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Running Tests**
```bash
pytest              # Run all tests
pytest -v           # Verbose output
```


## Test Structure
- **tests/**
    - **settings/**
        - **endpoints.py**              # API endpoint URLs and paths
        - **http_codes.py**             # HTTP status codes constants
    - **objects_endpoint/**
        - **cases/**                    # Test data generators and scenario descriptions
        - **fixtures/**                 # Custom fixtures and client setup for /objects endpoint
        - **objects_test.py**           # Test functions for /objects endpoint
    - **conftest.py**                   # Global pytest configuration and shared fixtures
- **pytest.ini**                        # Test markers and pytest configuration
- **requirements.txt**                  # Project dependencies and packages

**Key Advantages of the Test Structure:**

### **🏗️ Modularity**
- Clear separation of configuration, data, and test logic
- Isolated components prevent cross-contamination

### **⚙️ Centralization**
- Single source of truth for endpoints and status codes
- Easy maintenance and updates in one location

### **🧪 Data Management**
- Dedicated test data generators
- Reusable test scenarios

### **🔧 Fixture Flexibility**
- Global and endpoint-specific fixtures
- Support for different testing levels

### **📁 Scalability**
- Easy addition of new endpoints
- Maintainable structure as project grows

### **🎯 Focus**
- Single responsibility for each component
- Simplified navigation and debugging



# Проект тестирования API

## Обзор
Этот проект содержит автоматизированные тесты для публичного REST API, доступного по адресу [https://api.restful-api.dev/objects](https://api.restful-api.dev/objects). Тесты проверяют различные эндпоинты и функциональность API-сервиса.

## Функциональность
- Тестирование CRUD операций (Создание, Чтение, Обновление, Удаление)
- Валидация данных и проверка схем
- Сценарии обработки ошибок
- Проверка времени ответа API

## Установка

1. **Создание виртуального окружения**
```bash
python -m venv venv
```

2. **Активация виртуального окружения**
```bash
# Linux/MacOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3. **Установка зависимостей**
```bash
pip install -r requirements.txt
```

4. **Запуск тестов**
```bash
pytest              # Запуск всех тестов
pytest -v           # Подробный вывод
```

## Структура тестов
- **tests/**
    - **settings/**
        - **endpoints.py**              # URL-адреса и пути API эндпоинтов
        - **http_codes.py**             # Константы HTTP статус-кодов
    - **objects_endpoint/**
        - **cases/**                    # Генераторы тестовых данных и описания сценариев
        - **fixtures/**                 # Кастомные фикстуры и настройка клиента для эндпоинта /objects
        - **objects_test.py**           # Тестовые функции для эндпоинта /objects
    - **conftest.py**                   # Глобальная конфигурация pytest и общие фикстуры
- **pytest.ini**                        # Маркеры тестов и конфигурация pytest
- **requirements.txt**                  # Зависимости проекта и пакеты

**Ключевые преимущества структуры тестов:**

### **🏗️ Модульность**
- Четкое разделение конфигурации, данных и логики тестов
- Изолированные компоненты предотвращают взаимовлияние

### **⚙️ Централизация**
- Единый источник истины для эндпоинтов и статус-кодов
- Простое обслуживание и обновление в одном месте

### **🧪 Управление данными**
- Отдельные генераторы тестовых данных
- Многоразовые тестовые сценарии

### **🔧 Гибкость фикстур**
- Глобальные и специфичные фикстуры
- Поддержка разных уровней тестирования

### **📁 Масштабируемость**
- Легкое добавление новых эндпоинтов
- Поддерживаемая структура при росте проекта

### **🎯 Фокусировка**
- Каждый компонент имеет одну ответственность
- Упрощенная навигация и отладка