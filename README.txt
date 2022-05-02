Чтобы запустить проект, нужно при установленном докер открыть консоль, зайти в папку с проектом bewise_test и выполнить:
    - docker build app
    - docker-compose up -d 
    - docker-compose exec web python init_db.py

После этого можно попробовать послать POST запрос по адресу http://127.0.0.1:8000/add-questions 
с application/x-www-form-urlencoded параметром questions_num, по умолчанию равному 1
