# 🧑‍💻 Онлайн приложение `HeadHunter` для поиска работы и найма персонала.

### Содержание:
1. [Краткое описание приложения](#short_description)
2. [Задачи проекта](#project_tasks)
3. [Старт работы (как запустить приложение)](#start)
4. [Пароли и логины для входа в приложение:](#login)
5. [Функционал неавторизованного пользователя](#functional_guest)
6. [Функционал пользователя-соискателя](#functional_applicant)
7. [Функционал пользователя-работодателя](#functional_employer)




---
<a id='short_description'></a>
## 1. Краткое описание приложения

Приложение HeadHunter - платформа `по поиску работы и сотрудников`, позволяющая работодателям быстро выбрать подходящих работников, а соискателям – искомую работу.


---
<a id='project_tasks'></a>
## 2. Задачи проекта

 ### **Две основные задачи**

 *  помогать HR-специалистам и рекрутерам качественно и в срок закрывать вакансии
 *  содействовать соискателям в поиске достойной работы
 
<a id='start'></a>
## 3. Старт работы (как запустить приложение)

    Чтобы запустить `проект` локально, необходимо произвести `клонирование` себе на устройство следующей командой

```python
   $ git clone [https://github.com/USERNAME/REPOSITORY]
```

После успешного клонирования проекта, создаем `виртуальное окружение` 
```python
   $ python3 -m virtualenv venv
```
```python
   $ source venv/bin/activate 
```
и активируем все зависимости проекта:
```python
   pip3 install -r requirements.txt
```

Затем необходимо создать `базу` и внести соответствующую настройки в `settings.py` в ядре проекта

и активируем все зависимости проекта:
```python
   DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "[название созданной базы]",
        "USER": "[имя юзера базы]",
        "PASSWORD": "[пароль юзера базы]",
        "HOST": "localhost",
        "PORT": "",
    }
}
```

Далее применяем `миграции` командой:

```python
   python manage.py migrate
```

`Запуск` проекта командой:

```python
   python manage.py runserver
```

Для закрузки `фикстур` проекта используем команду:

```python
   pythin manage.py loaddata ./fixtures/[название файла].json  
```


---
<a id='login'></a>
## 4. 🌍 Пароли и логины для входа в приложение


<table>
    <tr>
        <th>Вход для:</th>
        <th>Логин</th>
        <th>Пароль</th>
    </tr>
    <tr>
        <td>администратора(admin)</td>
        <td>admin@admin.com</td>
        <td>admin</td>
    </tr>
    <tr>
        <td>соискателя (applicant)</td>
        <td>john_doe@mail.com</td>
        <td>A123456a</td>
    </tr>
    <tr>
        <td>работодателя (employer)</td>
        <td>too@mail.ru</td>
        <td>1234</td>
    </tr>
</table>



---
<a id='functional_guest'></a>
## 5. 📝 Функционал неавторизованного пользователя



---
<a id='functional_applicant'></a>
## 6. 📝 Функционал пользователя-соискателя

### Структура для заполнения шаблона резюме:
- Контактные данные соискателя (имя, фамилия, ссылки на личные страницы в соц. сетях, мобильный номер)
- Блок для указания желаемой позиции и сферы занятости (желаемая должность, категория сферы деятельности, желаемый уровень зарплаты)
- Блок с указанием образования (возможность добавить неограниченное количество образовательных учреждений)
- Блок с указанием опыта работы (каждый период работы заполняется добавлением нового блока)
  

---
<a id='functional_employer'></a>
## 7. 📝 Функционал пользователя-работодателя

### Структура для заполнения шаблона вакансии:
- Должность (указывается желаемая позиция)
- Категория (сфера деятельности, в которой соискатель желает получить занятость)
- Зарплата (желаемый уровень зарплаты)
- Описание вакансии (данный блок может включать, но не ограничиваться, следующей информацией:  условия занятости, график работы, соц.пакет, требования к кандидату, такие как функциональные обязанности, ключевые навыки, "soft&hard skills" и т.д.)
- Поля для указания минимального и максимального стажа/опыта работы










