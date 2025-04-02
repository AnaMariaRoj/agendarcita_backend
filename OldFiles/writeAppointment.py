import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Función para conectar a la base de datos MongoDB
def connect_to_mongodb(uri, db_name, collection_name):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    return collection

# Función para guardar la cita médica en MongoDB
def save_appointment_to_mongodb(appointment_json, collection):
    try:
        # Convertir el JSON string a un diccionario de Python
        appointment_data = json.loads(appointment_json)

        # Insertar el documento en la colección de MongoDB
        result = collection.insert_one(appointment_data)

        # Retornar el ID del documento insertado
        return result.inserted_id
    except Exception as e:
        print(f"Error al guardar en MongoDB: {e}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    # Cadena de conexión a MongoDB (reemplaza con tu propia cadena de conexión)
    uri = "mongodb+srv://mardugo:clave@sampleinformationservic.t2yog.mongodb.net/?retryWrites=true&w=majority&appName=SampleInformationService"

    # Nombre de la base de datos y la colección
    db_name = "HIS"
    collection_name = "appointments"

    # Conectar a MongoDB
    collection = connect_to_mongodb(uri, db_name, collection_name)

    # JSON string correspondiente al artefacto Appointment de HL7 FHIR
    appointment_json = '''
    {
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
    '''

    # Guardar la cita en MongoDB
    inserted_id = save_appointment_to_mongodb(appointment_json, collection)

    if inserted_id:
        print(f"Cita médica guardada con ID: {inserted_id}")
    else:
        print("No se pudo guardar la cita médica.")