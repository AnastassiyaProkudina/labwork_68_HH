# 🧑‍💻 Онлайн приложение `HeadHunter` для поиска работы и найма персонала.

### Содержание:
1. [Краткое описание приложения](#short_description)
2. [Задачи проекта](#project_tasks)
3. [Старт работы (как запустить приложение)](#start)
4. [Регистрация в приложении в качестве соискателя или работодателя)](#register)
5. [Пароли и логины для входа в приложение:](#login)
6. [Функционал пользователя-соискателя](#functional_applicant)
7. [Функционал пользователя-работодателя](#functional_employer)
8. [Функционал неавторизованного пользователя](#functional_guest)


---
<a id='short_description'></a>
## 1. Краткое описание приложения

Приложение HeadHunter - платформа `по поиску работы и сотрудников`, позволяющая работодателям быстро выбрать подходящих работников, а соискателям – искомую работу.


---
<a id='project_tasks'></a>
## 2. Задачи проекта

 ### **Две основные задачи:**

 *  помогать HR-специалистам и рекрутерам качественно и в срок закрывать вакансии
 *  содействовать соискателям в поиске достойной работы
 ---
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
<a id='register'></a>
## 4. 📫 Регистрация в приложении в качестве соискателя или работодателя

Для регистрации в приложении необходимо зайти на страницу формы регистрации путем нажатия на главной странице приложения кнопки `Зарегистрироваться`: 

<img src="https://github.com/AnastassiyaProkudina/labwork_68_HH/blob/main/static/img/for_readme_md/register_button.png" width="900" alt="register_button"/>

На странице регистрации пользователю будет предложено заполнить соответствующую форму, при этом стоит обратить внимание, что для регистрации в качестве работодателя необходимо отметить галочку в самом начале формы:

<img src="https://github.com/AnastassiyaProkudina/labwork_68_HH/blob/main/static/img/for_readme_md/register.png" width="600" alt="register"/>

После успешной регистрации в приложении необходимо на главной странице сайта нажать на внопку `Войти`:

<img src="https://github.com/AnastassiyaProkudina/labwork_68_HH/blob/main/static/img/for_readme_md/Login_button.png" width="900" alt="Login_button"/>

Далее на странице входа необходимо ввести соответствующий `логин` и `пароль`:

<img src="https://github.com/AnastassiyaProkudina/labwork_68_HH/blob/main/static/img/for_readme_md/login_form.png" width="900" alt="login_form"/>

В зависимости от роли пользователя, предоставляется соответствующий функционал, о котором мы раскажем ниже.


---
<a id='login'></a>
## 5. 🌍 Пароли и логины для входа в приложение


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
<a id='functional_applicant'></a>
## 6. 📝 Функционал `пользователя-соискателя`

**Соискатель может:**
* создавать и размещать в публичном доступе свое резюме (или несколько резюме)
* редактировать свое резюме и профиль
* поднимать наверх (обновлять)
* смотреть список вакансий, а также каждую вакансию в отдельности, осуществлять поиск и фильтрацию
* производить отклики на заинтересовавшие вакансии
* обмениваться сообщениями с работодателями посредстом чат платформы, а также просматривать профиль работодателя и информацию о компании.

 
> Профиль пользователя-соискателя
<img src="https://github.com/AnastassiyaProkudina/labwork_68_HH/blob/main/static/img/for_readme_md/Profile_applicant.png" width="500" alt="Profile_applicant"/>

> форма для заполнения резюме
<img src="https://github.com/AnastassiyaProkudina/labwork_68_HH/blob/main/static/img/for_readme_md/cv_form.png" width="500" alt="cv_form"/>
> Структура:
> - Контактные данные соискателя (имя, фамилия, ссылки на личные страницы в соц. сетях, мобильный номер)
> - Блок для указания желаемой позиции и сферы занятости (желаемая должность, категория сферы деятельности, желаемый уровень зарплаты)
> - Блок с указанием образования (возможность добавить неограниченное количество образовательных учреждений)
> - Блок с указанием опыта работы (каждый период работы заполняется добавлением нового блока)

> Пример заполненного резюме 
<img src="https://github.com/AnastassiyaProkudina/labwork_68_HH/blob/main/static/img/for_readme_md/cv_example.png" width="600" alt="cv_example"/>

> форма для редактирования профиля
<img src="https://github.com/AnastassiyaProkudina/labwork_68_HH/blob/main/static/img/for_readme_md/edit_profile.png" width="500" alt="edit_profile"/>


---
<a id='functional_employer'></a>
## 7. 📝 Функционал `пользователя-работодателя`

**Работодатель может:** 
* создавать и размещать в публичном доступе вакансии свой компании
* редактировать свои вакансии, а также свой профиль 
* поднимать наверх (обновлять) свои вакансии
* просмотр списка резюме, а также каждое резюме в отдельности, осуществлять поиск и фильтрацию резюме.
* обмениваться сообщениями с соискателями посредстом чат платформы.


> Профиль пользователя-работодателя
<img src="https://github.com/AnastassiyaProkudina/labwork_68_HH/blob/main/static/img/for_readme_md/Profile_employer.png" width="500" alt="Profile_employer"/>


> форма для заполнения вакансии
<img src="https://github.com/AnastassiyaProkudina/labwork_68_HH/blob/main/static/img/for_readme_md/vacancy_form.png" width="500" alt="vacancy_form"/>
> Структура:
> - Должность (указывается желаемая позиция)
> - Категория (сфера деятельности, в которой соискатель желает получить занятость)
> - Зарплата (желаемый уровень зарплаты)
> - Описание вакансии (данный блок может включать, но не ограничиваться, следующей информацией:  условия занятости, график работы, соц.пакет, требования к кандидату, такие как функциональные обязанности, ключевые навыки, "soft&hard skills" и т.д.)
> - Поля для указания минимального и максимального стажа/опыта работы


> Меню для просмотра своих вакансий с возможностью публикации/снятия с публикации, редактирования и удаления
<img src="https://github.com/AnastassiyaProkudina/labwork_68_HH/blob/main/static/img/for_readme_md/vacancy_list.png" width="900" alt="vacancy_list"/>


---
<a id='functional_guest'></a>
## 8. 📝 Функционал `неавторизованного пользователя`

**Неаторизованному пользователю доступен только следующий функционал приложения:**
* просмотр списка и поиск вакансий
* возможность зарегистрироваться в приложении в качестве соискателя/работодателя






