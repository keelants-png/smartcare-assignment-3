import pytest
from datetime import datetime
from smartcare.data_store import SmartCareDataStore
from smartcare.services import PatientService, PractitionerService, AppointmentService

def test_find_patient_success():
    store = SmartCareDataStore(); service = PatientService(store)
    patient = service.register_patient("P1", "Alice")
    assert service.find_patient("P1") is patient

def test_find_patient_missing():
    store = SmartCareDataStore(); service = PatientService(store)
    with pytest.raises(LookupError): service.find_patient("UNKNOWN")

def test_find_patient_blank():
    store = SmartCareDataStore(); service = PatientService(store)
    with pytest.raises(ValueError): service.find_patient("")

def test_find_practitioner_success():
    store = SmartCareDataStore(); service = PractitionerService(store)
    practitioner = service.register_practitioner("D1", "Dr. Chen", "GP")
    assert service.find_practitioner("D1") is practitioner

def test_cancel_appointment_success():
    store = SmartCareDataStore(); pat_s = PatientService(store)
    prac_s = PractitionerService(store); appt_s = AppointmentService(store)
    pat_s.register_patient("P1", "Alice"); prac_s.register_practitioner("D1", "Dr. Chen", "GP")
    appt = appt_s.book_appointment("A1", "P1", "D1", datetime(2026, 10, 1, 9, 0))
    cancelled = appt_s.cancel_appointment("A1")
    assert cancelled is appt and cancelled.status.value == "cancelled"

def test_cancel_appointment_twice():
    store = SmartCareDataStore(); pat_s = PatientService(store)
    prac_s = PractitionerService(store); appt_s = AppointmentService(store)
    pat_s.register_patient("P1", "Alice"); prac_s.register_practitioner("D1", "Dr. Chen", "GP")
    appt_s.book_appointment("A1", "P1", "D1", datetime(2026, 10, 1, 9, 0))
    appt_s.cancel_appointment("A1")
    with pytest.raises(ValueError): appt_s.cancel_appointment("A1")
