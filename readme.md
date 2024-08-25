# To-do App

This Application helps user to add to-do items,view items, update items and delete items.


The procedure to setup this Application: \
clone the repository using link
https://github.com/appurajk/Todo-App-FastAPI.git

Create python environment
    $ python -m venv venv \
    $ source venv/bin/activate \
    $ pip install -r requirements.txt 


MongoDB Driver
download https://www.mongodb.com/
install mongodb server

Start the mongodb server<br />
$ mongo

Project directory has the following structure:

Todo-App-FastAPI/
│
├── main.py
├── models/
│   ├── __init__.py
│   └── todo_models.py
├── repositories/
│   └── todo_repository.py
└── services/
|    └── todo_service.py
|___utils/
     |__ db_connect.py

$ cd Todo-App-FastAPI \
$ python main.py

goto-http://localhost:8000/docs
make use of UISwagger to drive the Application. 