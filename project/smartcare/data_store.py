"""In-memory data store for SmartCare."""

from datetime import datetime
from smartcare.domain import Appointment, AppointmentStatus, Patient, Practitioner

class SmartCareDataStore:
    def __init__(self) -> None:
        self._patients: dict[str, Patient] = {}
        self._practitioners: dict[str, Practitioner] = {}
        self._appointments: dict[str, Appointment] = {}

    def add_patient(self, patient: Patient) -> None:
        if patient.patient_id in self._patients:
            raise ValueError(f"Patient {patient.patient_id} already exists")
        self._patients[patient.patient_id] = patient

    def find_patient(self, patient_id: str) -> Patient | None:
        return self._patients.get(patient_id)

    def add_practitioner(self, practitioner: Practitioner) -> None:
        if practitioner.practitioner_id in self._practitioners:
            raise ValueError(f"Practitioner {practitioner.practitioner_id} already exists")
        self._practitioners[practitioner.practitioner_id] = practitioner

    def find_practitioner(self, practitioner_id: str) -> Practitioner | None:
        return self._practitioners.get(practitioner_id)

    def add_appointment(self, appointment: Appointment) -> None:
        if appointment.appointment_id in self._appointments:
            raise ValueError(f"Appointment {appointment.appointment_id} already exists")
        self._appointments[appointment.appointment_id] = appointment

    def find_appointment(self, appointment_id: str) -> Appointment | None:
        return self._appointments.get(appointment_id)

    def list_appointments(self) -> list[Appointment]:
        return list(self._appointments.values())

    def has_practitioner_conflict(self, practitioner_id: str, date_time: datetime) -> bool:
        for appt in self._appointments.values():
            if (appt.practitioner.practitioner_id == practitioner_id and 
                appt.date_time == date_time and 
                appt.status == AppointmentStatus.SCHEDULED):
                return True
        return False
