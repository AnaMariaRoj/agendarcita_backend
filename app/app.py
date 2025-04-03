from fastapi import FastAPI, HTTPException, Request
import uvicorn
from app.controlador.AppointmentCrud import GetAppointmentById, GetAppointmentByIdentifier, WriteAppointment
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes (ajustar según necesidad)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

@app.get("/appointments/{appointments_id}", response_model=dict)
async def get_appointment_by_id(appointment_id: str):
    status, appointment = GetAppointmentById(appointment_id)
    if status == 'success':
        return appointment  # Devolver la cita médica
    elif status == 'notFound':
        raise HTTPException(status_code=404, detail="Appointment not found")
    else:
        raise HTTPException(status_code=500, detail=f"Internal error. {status}")

@app.get("/appointment/", response_model=dict)
async def get_appointment_by_identifier(system: str, value: str):
    status, appointment = GetAppointmentByIdentifier(system, value)
    if status == 'success':
        return appointment  # Devolver la cita médica
    elif status == 'notFound':
        raise HTTPException(status_code=404, detail="Appointment not found")
    else:
        raise HTTPException(status_code=500, detail=f"Internal error. {status}")

@app.post("/appointment", response_model=dict)
async def add_appointment(request: Request):
    new_appointment_dict = dict(await request.json())
    status, appointment_id = WriteAppointment(new_appointment_dict)

    if status == 'success':
        return {"_id": appointment_id}  # Devolver el ID de la cita médica
    elif "errorValidating" in status:
        raise HTTPException(status_code=422, detail=f"Validation Error: {status}")
    else:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {status}")

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
