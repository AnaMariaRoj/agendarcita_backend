import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

# Función para conectar a la base de datos MongoDB
def connect_to_mongodb(uri, db_name, collection_name):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    return collection

# Función para guardar la cita médica en MongoDB
def save_appointment_to_mongodb(appointment_data, collection):
    try:
        # Verificar que appointment_data ya sea un diccionario
        if isinstance(appointment_data, str):
            appointment_data = json.loads(appointment_data)

        # Insertar el documento en la colección de MongoDB
        result = collection.insert_one(appointment_data)
        
        # Retornar el ID del documento insertado como string
        return str(result.inserted_id)
    except Exception as e:
        print(f"Error al guardar en MongoDB: {e}")
        return None

# Función principal de escritura de cita médica
def WriteAppointment(appointment_json):
    uri = "mongodb+srv://mardugo:clave@sampleinformationservic.t2yog.mongodb.net/?retryWrites=true&w=majority&appName=SampleInformationService"
    db_name = "HIS"
    collection_name = "appointments"
    
    # Conectar a la colección de MongoDB
    collection = connect_to_mongodb(uri, db_name, collection_name)
    
    # Guardar la cita en MongoDB
    inserted_id = save_appointment_to_mongodb(appointment_json, collection)
    
    if inserted_id:
        return "success", inserted_id
    else:
        return "error", None

