# study_english
## Описание
Тестовое задание.

Технологии:
 - Django
 - PostgreSQL
 - Nginx
 - Docker

## Тестовый стенд
 - **Адрес**: http://185.41.163.131/
 - **Аккаунт**: admin:testing
 - **API_SECRET**: ciezee3aiP3aepu4baik
 
Для упрощения проверки `DEBUG=True`.

## Развертывание
Склонировать репозиторий:
```bash
cd /opt/
git clone https://github.com/Vladius25/study_english.git
```

Произвести настройки PostgreSQL (логин/пароль/база) по образцу:
```bash
cp config/db/db_env config/db/db_prod_env
vim config/db/db_prod_env
```

Произвести настройки Django по образцу:
```bash
cp app/study_english/local_settings.default.py app/study_english/local_settings.py
vim app/study_english/local_settings.py
```

Запустить проект:
```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d
```

Для систем с **systemd** (большинство современных дистрибутивов) для запуска можно использовать подготовленный юнит:
```bash
cp study_english.service /etc/systemd/system/
systemctl enable --now study_english
```

После запуска собрать статические файлы, применить миграции и создать админа:
```bash
docker-compose run --rm djangoapp python src/manage.py collectstatic --noinput
docker-compose run --rm djangoapp python src/manage.py migrate
docker-compose run --rm djangoapp python src/manage.py createsuperuser
```
