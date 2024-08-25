# To-do App

This Application helps user to add to-do items,view items, update items and delete items.


The procedure to setup this Application: \
clone the repository using link
https://github.com/appurajk/to-do-app.git

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

Todo-App-FastAPI/<br />
│<br />
├── main.py<br />
├── models/<br />
│   ├── __init__.py<br />
│   └── todo_models.py<br />
├── repositories/<br />
│   └── todo_repository.py<br />
└── services/<br />
|    └── todo_service.py<br />
|___utils/<br />
     |__ db_connect.py<br />
<br />
$ cd Todo-App-FastAPI \
$ python main.py

goto-http://localhost:8000/docs
make use of UISwagger to drive the Application. 
