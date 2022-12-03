# POEVENT
An example of a rest API made with Flask and MySQL, registering college students for a poetry event.

# Installation Guide
## Pre-requirements
In this project I will use `MySQL` as a database administrator and it is recommended to use `virtualenv` to avoid conflicts with other projects.

## How to start?
Clone the repository.
```
$ git clone https://github.com/Angel-Gabriel-Chavez/poevent.git
```
Create the virtual environment, and activate it.
```
> cd poevent
> python -m venv venv
> venv\Scripts\activate.bat
```
Enter the following commands in the MySQL console.
```
mysql> CREATE DATABASE IF NOT EXISTS poevent;
mysql> USE poevent;
```

## Install dependencies
```
(venv) C:\poevent> python -m pip install -r requirements.txt
```

## Run 
```
(venv) C:\poevent> python main.py
```
Visit `https://127.0.0.1:5000` to see the project in operation
# License
- MIT