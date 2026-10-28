"""Simple workflows using a shared SmartCareDataStore object."""

from datetime import datetime

from smartcare.data_store import SmartCareDataStore
from smartcare.domain import (
    Appointment,
    AppointmentStatus,
    Patient,
    Practitioner,
)


class PatientService:
    def __init__(self, data_store: SmartCareDataStore) -> None:
        self.data_store = data_store

    def register_patient(self, patient_id: str, name: str) -> Patient:
        patient = Patient(patient_id, name)
        self.data_store.add_patient(patient)
        return patient

    def find_patient(self, patient_id: str) -> Patient:
        if not patient_id or not patient_id.strip():
            raise ValueError("Patient ID cannot be blank")
        patient = self.data_store.find_patient(patient_id)
        if patient is None:
            raise LookupError(f"Patient {patient_id} not found")
        return patient


class PractitionerService:
    def __init__(self, data_store: SmartCareDataStore) -> None:
        self.data_store = data_store

    def register_practitioner(self, practitioner_id: str, name: str, specialty: str) -> Practitioner:
        practitioner = Practitioner(practitioner_id, name, specialty)
        self.data_store.add_practitioner(practitioner)
        return practitioner

    def find_practitioner(self, practitioner_id: str) -> Practitioner:
        if not practitioner_id or not practitioner_id.strip():
            raise ValueError("Practitioner ID cannot be blank")
        practitioner = self.data_store.find_practitioner(practitioner_id)
        if practitioner is None:
            raise LookupError(f"Practitioner {practitioner_id} not found")
        return practitioner


class AppointmentService:
    def __init__(self, data_store: SmartCareDataStore) -> None:
        self.data_store = data_store

    def book_appointment(self, appointment_id: str, patient_id: str, practitioner_id: str, date_time: datetime) -> Appointment:
        patient = self.data_store.find_patient(patient_id)
        practitioner = self.data_store.find_practitioner(practitioner_id)
        if patient is None:
            raise LookupError('Patient not found')
        if practitioner is None:
            raise LookupError('Practitioner not found')
        appointment = Appointment(appointment_id, patient, practitioner, date_time)
        if self.data_store.find_appointment(appointment.appointment_id) is not None:
            raise ValueError('Appointment ID already exists')
        if self.data_store.has_practitioner_conflict(practitioner.practitioner_id, date_time):
            raise ValueError('Practitioner already has a SCHEDULED appointment at this time')
        self.data_store.add_appointment(appointment)
        return appointment

    def find_appointment(self, appointment_id: str) -> Appointment:
        appointment = self.data_store.find_appointment(appointment_id)
        if appointment is None:
            raise LookupError('Appointment not found')
        return appointment

    def cancel_appointment(self, appointment_id: str) -> Appointment:
        if not appointment_id or not appointment_id.strip():
            raise ValueError("Appointment ID cannot be blank")
        appointment = self.data_store.find_appointment(appointment_id)
        if appointment is None:
            raise LookupError(f"Appointment {appointment_id} not found")
        appointment.cancel()
        return appointment

    def list_practitioner_appointments(self, practitioner_id: str, status: AppointmentStatus | None = None) -> list[Appointment]:
        raise NotImplementedError('Stage 9: practitioner appointments')
