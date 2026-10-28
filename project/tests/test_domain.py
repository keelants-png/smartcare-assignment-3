import pytest
from datetime import datetime
from smartcare.domain import Patient, Practitioner, Appointment, AppointmentStatus

def test_patient_valid_creation():
    patient = Patient("P1", "Alice")
    assert patient.patient_id == "P1"
    assert patient.name == "Alice"

def test_patient_blank_id_rejected():
    with pytest.raises(ValueError):
        Patient("", "Alice")

def test_patient_blank_name_rejected():
    with pytest.raises(ValueError):
        Patient("P1", "   ")

def test_practitioner_valid_creation():
    prac = Practitioner("D1", "Dr. Chen", "GP")
    assert prac.practitioner_id == "D1"
    assert prac.specialty == "GP"

def test_practitioner_blank_specialty_rejected():
    with pytest.raises(ValueError):
        Practitioner("D1", "Dr. Chen", "")

def test_appointment_initial_status_is_scheduled():
    p = Patient("P1", "Alice")
    d = Practitioner("D1", "Dr. Chen", "GP")
    appt = Appointment("A1", p, d, datetime(2026, 10, 1, 9, 0))
    assert appt.status == AppointmentStatus.SCHEDULED

def test_appointment_cancellation_changes_status():
    p = Patient("P1", "Alice")
    d = Practitioner("D1", "Dr. Chen", "GP")
    appt = Appointment("A1", p, d, datetime(2026, 10, 1, 9, 0))
    appt.cancel()
    assert appt.status == AppointmentStatus.CANCELLED

def test_appointment_repeated_cancellation_rejected():
    p = Patient("P1", "Alice")
    d = Practitioner("D1", "Dr. Chen", "GP")
    appt = Appointment("A1", p, d, datetime(2026, 10, 1, 9, 0))
    appt.cancel()
    with pytest.raises(ValueError):
        appt.cancel()
