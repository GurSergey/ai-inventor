# Inventor AI User Interface
This project is a web interface to a large language model based on the T5 architecture that has been trained to solve inventive problems. Link to language model https://disk.yandex.ru/d/Y9W-zdavchobGw
### Run (developer config)
Put files of model into folder models/t5base. Next run docker-compose and python. Loading the tokenizer into the computer memory takes a long time, please be patient (on my computer 7 minutes). When the application is started, you will see in the console that the Flask application is running. Open localhost:80 in your browser (basic auth - user1 test)
```sh
docker-compose -f docker-compose-dev.yml up
python main.py
```
### Run (simple prod config)
Put files of model into folder models/t5base. Build docker images for frontend and backend. Run docker-compose. Loading the tokenizer into the computer memory takes a long time, please be patient (on my computer 7 minutes). When the application is started, you will see in the console that the Flask application is running. Open localhost:8080 in your browser (basic auth - user1 test)
```sh
docker build -t frontend-inventor ./frontend/ 
docker build -t backend-inventor ./backend/ 
docker-compose up
```
