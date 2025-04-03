from pymongo import MongoClient
from pymongo.server_api import ServerApi

def connect_to_mongodb(uri, db_name, collection_name):
    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client[db_name]
        collection = db[collection_name]
        print("✅ Conectado a MongoDB correctamente")
        return collection
    except Exception as e:
        print(f"❌ Error conectando a MongoDB: {e}")
        return None

def save_appointment_to_mongodb(appointment_data, collection):
    try:
        if not isinstance(appointment_data, dict):
            raise ValueError("Los datos de la cita deben ser un diccionario")
        
        result = collection.insert_one(appointment_data)
        return str(result.inserted_id)  # Convertir ObjectId a string
    except Exception as e:
        print(f"❌ Error al guardar en MongoDB: {e}")
        return None

# Prueba de conexión y almacenamiento
if __name__ == "__main__":
    uri = "mongodb+srv://mardugo:clave@sampleinformationservic.t2yog.mongodb.net/?retryWrites=true&w=majority&appName=SampleInformationService"
    db_name = "HIS"
    collection_name = "appointments"
    
    collection = connect_to_mongodb(uri, db_name, collection_name)
    
    if collection:
        appointment_data = {
            "resourceType": "Appointment",
            "status": "booked",
            "description": "Consulta médica general",
            "start": "2025-04-10T10:00:00Z",
            "end": "2025-04-10T10:30:00Z",
            "participant": [
                {
                    "actor": {
                        "reference": "Patient/1020713756",
                        "display": "Mario Enrique Duarte"
                    },
                    "status": "accepted"
                },
                {
                    "actor": {
                        "reference": "Practitioner/12345",
                        "display": "Dr. Juan Pérez"
                    },
                    "status": "accepted"
                }
            ]
        }
        
        inserted_id = save_appointment_to_mongodb(appointment_data, collection)
        
        if inserted_id:
            print(f"✅ Cita médica guardada con ID: {inserted_id}")
        else:
            print("❌ No se pudo guardar la cita médica.")
