# Задание по SQL.

## Все возможные запросы.

1. Выбор имен и фамилий водителей (выборка):

```sql
select
    forename, 
    surname
from
    drivers
```

2. Выбор стартовых позиций на гонках (проекция):

```sql
select distinct
    raceId,
    driverId,
    position
from qualifying
```

3. Объединение всех raceID и driverID из таблиц results и qualifying (объединение):

```sql
select
    raceId,
    driverId
from
    results
union select
    raceId,
    driverId
from
    qualifying
```

4. Выбор тех и только тех raceID и driverID, которые есть и в results, и в qualifying (пересечение):

```sql
select
    raceId,
    driverId
from
    results
intersect select
    raceId,
    driverId
from
    qualifying
```

5. Выбор raceID и driverID, которые есть в results, но нет в qualifying (разность):

```sql
select
    raceId,
    driverId
from
    results
except select
    raceId,
    driverId
from
    qualifying
```

6. Назначение каждого гонищка каждому констрактору (ничего лучше не придумали) (декартово произведение):

```sql
select
    forename,
    surname,
    name
from
    drivers,
    constructors
```

7. "Проверка целостности данных" (деление):

```sql
select distinct
    raceId,
    driverId
from
    results
where not exists(select raceId, driverId from qualifying)
```

8. Сажаем всех водителей в McLaren (тета-соединение):

```sql
select
    forename,
    surname,
    name
from
    drivers,
    constructors
where
    name = 'McLaren'
```

## Всех возможные варианты выполнения тех или иных запросов

1. Выбор призёров гонок:

```sql
select distinct
    position,
    forename,
    surname,
    name as race_name
from
    qualifying
left join
    drivers on qualifying.driverId = drivers.driverId
inner join
    races on qualifying.raceId = races.raceId
```

Выбираем из таблицы qualifying `driverId` и `raceId`, по ним соединяемся с таблицами `drivers` и `races` с помощью LEFT JOIN и INNER JOIN соответственно, после фильтруем призёров (занимаемое место <= 3).

2. Получение времени первого круга для водителя с id=20 и ссылки на сезон для этого времени:

```sql
select distinct
    laptimes.time as time,
    seasons.url as url
from
    laptimes
left outer join
    races on laptimes.raceId = races.raceId
join
    seasons on races.year = seasons.year
where
    lap = 1 and driverId = 20
order by
    url
```

Выделяем из таблицы laptimes `raceId`, по которому соединяем с таблицей races, где выделяем `year`, соединяем с `seasons` и фильтруем по id водителя и количеству кругов и сортируем по ссылке по возростанию.


## Комментарии

К сожалению, в диалекте SQLite нет FULL OUTER JOIN, RIGHT JOIN и т.д., поэтому их нет в примерах.
