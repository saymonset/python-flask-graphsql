# Create virtual enviroment
python3 -m venv venv

#Activa virtual enviroment
source venv/bin/activate

#Instalamos los requerimientos
 pip3 install -r requirements.txt 



#dev
Copiar el ```env.template``` y renombrar a ```.env```

#Arrancamos la aplicacion
flask --app flaskr run --debug --port 8000

```
localhost:8000/graphql
```


#--------------otros----------

#Caso de bug
1-)  pip3 freeze > requirements.txt
2-)   pip3 uninstall -r requirements.txt 
3-) source venv/bin/activate
4-) pip3 install -r requirements.txt 
5-) flask --app flaskr run --debug --port 8000



export FLASK_APP=flaskr

 pip3 freeze > requirements.txt


# Forma para comenzar sencillo
flask --app app run --port 8000

#Para una arquitectura mejor
flask --app flaskr run --debug --port 8000