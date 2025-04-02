from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Función para conectar a la base de datos MongoDB
def connect_to_mongodb(uri, db_name, collection_name):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    return collection

# Función para buscar citas por un identifier específico
def find_appointment_by_identifier(collection, identifier_value):
    try:
        # Consultar el documento que coincida con el identifier
        query = {"patient.identifier.value": identifier_value}
        appointment = collection.find_one(query)
        
        # Retornar la cita encontrada
        return appointment
    except Exception as e:
        print(f"Error al buscar en MongoDB: {e}")
        return None

# Función para mostrar los datos de una cita
def display_appointment(appointment):
    if appointment:
        print("Cita encontrada:")
        print(f"  ID: {appointment.get('_id')}")
        print(f"  Paciente: {appointment.get('patient', {}).get('name', 'Desconocido')}")
        print(f"  Especialidad: {appointment.get('specialty', 'Desconocida')}")
        print(f"  Fecha: {appointment.get('date', 'Desconocida')}")
        print(f"  Hora de inicio: {appointment.get('start_time', 'Desconocida')}")
        print(f"  Hora de fin: {appointment.get('end_time', 'Desconocida')}")
    else:
        print("No se encontró ninguna cita con el identifier especificado.")

# Ejemplo de uso
if __name__ == "__main__":
    # Cadena de conexión a MongoDB (reemplaza con tu propia cadena de conexión)
    uri = "mongodb+srv://mardugo:clave@sampleinformationservic.t2yog.mongodb.net/?retryWrites=true&w=majority&appName=SampleInformationService"

    # Nombre de la base de datos y la colección
    db_name = "HIS"
    collection_name = "appointments"

    # Conectar a MongoDB
    collection = connect_to_mongodb(uri, db_name, collection_name)
    
    # Identifier específico a buscar (reemplaza con los valores que desees)
    identifier_value = "1020713756"
    
    # Buscar la cita por identifier
    appointment = find_appointment_by_identifier(collection, identifier_value)
    
    # Mostrar los datos de la cita encontrada
    display_appointment(appointment)