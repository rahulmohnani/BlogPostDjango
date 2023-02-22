# Blog Post Application
## How to install this project in your local system guide
1. Take the pull of this repo or download the zip file of the project and extract it in your local system. Use this command to clone the project if you have git isntalled in your local machine.
```
git clone https://github.com/rahulmohnani/BlogPostDjango
```
2. Make sure you have Python already installed in your system. You can download Python from here: [Download Python](https://www.python.org/downloads/)
3. Install Virtual Environment using pip commands. You can refer to this link for installing virtual environment [Virtual Environment Docs](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).
Install virtual environment for windows command
```
py -m pip install --user virtualenv
```
Install virtual environment for macOS/Unix
```
python3 -m pip install --user virtualenv
```
4. After installing virtual environment create a virtual environment for downloading dependencies of particular version for this project. 
Creating virtual environment command for windows
```
py -m venv env
```
Creating virtual environment command for macOs/Unix
```
python3 -m venv env
```
5. Activate the virtual environment that you have created.
Activating virtual environment command for windows
```
.\env\Scripts\activate
```
Activating virtual environment command for macOs/Unix
```
source env/bin/activate
```
6. Install all the dependencies after you have activated environment using this command.
```
pip install -r requirements.txt
```
7. Make the migrations to create migration files in your system. Use these commands for migrations.
```
python manage.py makemigrations blog
```
```
python manage.py makemigrations members
```
8. Migrate these migrations to dataase using this command.
```
python manage.py migrate
```
9. Project and database will be setup after following these steps. If you want to create a super user who can access admin panel to add blog categories and access control, you can use this command andd fill all the credentials required.
```
python manage.py createsuperuser
```
10. To run the project use this command.
```
python manage.py runserver
```
11. The project will run on localhost port 8000. [Link](http://127.0.0.1:8000/)
