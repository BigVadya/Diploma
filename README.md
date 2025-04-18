
# DocuCloud Reference Guide

**DocuCloud Reference Guide** — это веб-приложение, разработанное на Django, которое предоставляет пользователям справочную информацию по созданию и внедрению систем автоматизации документооборота с использованием облачных технологий.

## 📦 Установка и запуск проекта

1. Клонируйте репозиторий:

```bash
git clone https://github.com/BigVadya/Diploma.git
cd Diploma
```

2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. Примените миграции:

```bash
python manage.py migrate
```

4. Запустите сервер разработки:

```bash
python manage.py runserver
```

После запуска проект будет доступен в браузере по адресу:  
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ⚙️ Основная функциональность

- Регистрация и аутентификация пользователей  
- Редактирование личного профиля (имя, email, пароль)  
- Просмотр справочных материалов:
  - схемы документооборота  
  - терминология  
  - классификации  
  - рекомендации  
- Удобная навигация по разделам сайта

---

## 👤 Разработчик

[BigV](https://github.com/BigVadya)

---

## 📄 Лицензия

Проект распространяется под лицензией **MIT**. Подробнее в файле [LICENSE](LICENSE).
