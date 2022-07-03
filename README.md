# Inventor AI User Interface
This project is a web interface to a large language model based on the T5 architecture that has been trained to solve inventive problems. Link to language model https://disk.yandex.ru/d/Y9W-zdavchobGw
### Run (developer config)
Put files of model into folder models/t5base. Next run docker-compose and python. Open localhost:80 in your browser
```sh
docker-compose -f docker-compose-dev.yml up
python main.py
```
### Run (simple prod config)
Put files of model into folder models/t5base. Build docker images for frontend and backend. Run docker-compose. Open localhost:8080 in your browser
```sh
docker build -t fronted-inventor ./frontend/ 
docker build -t backend-inventor ./backend/ 
docker-compose up
```
