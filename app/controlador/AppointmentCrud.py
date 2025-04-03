from connection import connect_to_mongodb
from bson import ObjectId
from fhir.resources.appointment import Appointment
import json

collection = connect_to_mongodb("HIS", "appointments")

def GetAppointmentById(appointment_id: str):
    try:
        appointment = collection.find_one({"_id": ObjectId(appointment_id)})
        if appointment:
            appointment["_id"] = str(appointment["_id"])
            return "success", appointment
        return "notFound", None
    except Exception as e:
        return "notFound", None

def GetAppointmentByIdentifier(patientSystem, patientValue):
    try:
        appointment = collection.find_one({
            "participant.actor.identifier.system": patientSystem, 
            "participant.actor.identifier.value": patientValue
        })
        if appointment:
            appointment["_id"] = str(appointment["_id"])
            return "success", appointment
        return "notFound", None
    except Exception as e:
        return "notFound", None        

def WriteAppointment(appointment_dict: dict):
    try:
        appt = Appointment.model_validate(appointment_dict)
    except Exception as e:
        print("Error de validación en Appointment:", e)  # <-- Agregado para depuración
        return f"errorValidating: {str(e)}", None

    validated_appointment_json = appt.model_dump()
    result = collection.insert_one(validated_appointment_json)  # <-- Guarda el objeto validado
    if result:
        inserted_id = str(result.inserted_id)
        return "success", inserted_id
    else:
        return "errorInserting", None
