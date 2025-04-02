from fhir.resources.appointment import Appointment
import json

# Ejemplo de uso
if __name__ == "__main__":
    # JSON string correspondiente al artefacto Appointment de HL7 FHIR
    appointment_json = '''
    {
      "resourceType": "Appointment",
      "status": "booked",
      "serviceCategory": [
        {
          "coding": [
            {
              "system": "http://terminology.hl7.org/CodeSystem/service-category",
              "code": "57",
              "display": "Consulta médica"
            }
          ]
        }
      ],
      "serviceType": [
        {
          "coding": [
            {
              "system": "http://terminology.hl7.org/CodeSystem/service-type",
              "code": "11429006",
              "display": "Consulta de medicina general"
            }
          ]
        }
      ],
      "appointmentType": {
        "coding": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/v2-0276",
            "code": "WALKIN",
            "display": "Consulta sin cita previa"
          }
        ]
      },
      "reasonCode": [
        {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "308335008",
              "display": "Dolor de cabeza"
            }
          ]
        }
      ],
      "start": "2025-04-05T10:00:00Z",
      "end": "2025-04-05T10:30:00Z",
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

    # Validar el recurso Appointment
    appointment = Appointment.model_validate(json.loads(appointment_json))
    print("JSON validado:", appointment.model_dump())
