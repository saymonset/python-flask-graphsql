export FLASK_APP=flaskr

 pip3 freeze > requirements.txt
 pip3 install -r requirements.txt 

# Forma para comenzar sencillo
flask --app app run --port 8000

#Para una arquitectura mejor
flask --app flaskr run --debug --port 8000