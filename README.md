# Пульт охраны
Это внутренний репозиторий для сотрудников банка "Сияние". Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.
Для запуска используем bash команду: 


```
python3 manage.py runserver
```


### Как установить
Для работы в файле .env нужно указать актуальные данные настроек БД. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:



```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).