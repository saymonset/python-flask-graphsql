from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def calcular_edad_y_es_nino(birth_date):
    try:
        birthDate = datetime.strptime(birth_date.split("T")[0], "%Y-%m-%d")
        is_children = relativedelta(datetime.now().date(), birthDate).years < 18
        age = relativedelta(datetime.now(), birthDate).years
        days_birth = (datetime.now() - birthDate).days
        return is_children, age, days_birth
    except ValueError:
        return False, 0
          # Manejar el caso de fecha no válida
def calcular_date_must_apply(birth_date, expires_in_days):
    try:
        # Convertir la fecha de nacimiento a un objeto datetime
        birthDate = datetime.strptime(birth_date.split("T")[0], "%Y-%m-%d")
        
        # Sumar los días de expires_in_days a la fecha de nacimiento
        date_must_apply = birthDate + timedelta(days=expires_in_days)
        
        # Retornar la fecha resultante como una cadena en el formato deseado
        #return date_must_apply.strftime("%Y-%m-%d")
        # Retornar la fecha resultante como un objeto de tipo date
        # Convertir un objeto datetime.date a datetime.datetime
        # Retornar la fecha resultante como un objeto de tipo date
        #return date_must_apply.date()
        # Retornar la fecha resultante como una cadena en el formato deseado
        return date_must_apply.strftime("%d-%m-%Y")
    except ValueError:
        return "Fecha no válida"  # Manejar el caso de fecha no válida