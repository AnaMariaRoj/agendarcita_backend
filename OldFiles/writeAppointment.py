import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId
from fhir.resources.appointment import Appointment

def connect_to_mongodb():
    """ Conecta a la base de datos MongoDB """
    uri = "mongodb+srv://mardugo:clave@sampleinformationservic.t2yog.mongodb.net/?retryWrites=true&w=majority&appName=SampleInformationService"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["HIS"]
    return db["appointments"]

def save_appointment_to_mongodb(appointment_data, collection):
    try:
        # Verificar que appointment_data sea un diccionario
        if isinstance(appointment_data, str):
            appointment_data = json.loads(appointment_data)

        # Validar el formato FHIR del Appointment
        appointment = Appointment.model_validate(appointment_data)
        validated_data = appointment.model_dump()

        # Insertar el documento validado en MongoDB
        result = collection.insert_one(validated_data)
        return str(result.inserted_id)
    except Exception as e:
        print(f"Error al guardar en MongoDB: {e}")
        return None

def WriteAppointment(appointment_json):
    """ Función para registrar una cita médica en MongoDB """
    collection = connect_to_mongodb()
    inserted_id = save_appointment_to_mongodb(appointment_json, collection)
    
    if inserted_id:
        return "success", inserted_id
    else:
        return "error", None


