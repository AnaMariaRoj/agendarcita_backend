import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Función para conectar a la base de datos MongoDB
def connect_to_mongodb(uri, db_name, collection_name):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    return collection

# Función para leer todas las citas médicas de la colección
def read_appointments_from_mongodb(collection):
    try:
        # Consultar todos los documentos en la colección
        appointments = collection.find()
        
        # Convertir los documentos a una lista de diccionarios
        appointment_list = list(appointments)
        
        # Retornar la lista de citas médicas
        return appointment_list
    except Exception as e:
        print(f"Error al leer desde MongoDB: {e}")
        return None

# Función para mostrar los datos de las citas médicas
def display_appointments(appointment_list):
    if appointment_list:
        for appointment in appointment_list:
            print("Cita Médica:")
            print(f"  ID: {appointment.get('_id')}")
            print(f"  Paciente: {appointment.get('patient', {}).get('name', 'Desconocido')}")
            print(f"  Especialidad: {appointment.get('specialty', 'No especificada')}")
            print(f"  Fecha: {appointment.get('date', 'No especificada')}")
            print(f"  Hora: {appointment.get('time', 'No especificada')}")
            print("-" * 30)
    else:
        print("No se encontraron citas médicas en la base de datos.")

# Ejemplo de uso
if __name__ == "__main__":
    # Cadena de conexión a MongoDB (reemplaza con tu propia cadena de conexión)
    uri = "mongodb+srv://mardugo:clave@sampleinformationservic.t2yog.mongodb.net/?retryWrites=true&w=majority&appName=SampleInformationService"

    # Nombre de la base de datos y la colección
    db_name = "HIS"
    collection_name = "appointments"

    # Conectar a MongoDB
    collection = connect_to_mongodb(uri, db_name, collection_name)
    
    # Leer las citas médicas de la colección
    appointments = read_appointments_from_mongodb(collection)
    
    # Mostrar los datos de las citas médicas
    display_appointments(appointments)
