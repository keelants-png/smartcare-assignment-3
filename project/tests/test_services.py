import pytest
from datetime import datetime

from smartcare.data_store import SmartCareDataStore
from smartcare.services import PatientService, PractitionerService, AppointmentService

def test_find_patient_success():
    store = SmartCareDataStore()
    service = PatientService(store)
    patient = service.register_patient("P1", "Alice")
    found = service.find_patient("P1")
    assert found is patient

def test_find_patient_missing():
    store = SmartCareDataStore()
    service = PatientService(store)
    with pytest.raises(LookupError):
        service.find_patient("UNKNOWN")

def test_find_patient_blank():
    store = SmartCareDataStore()
    service = PatientService(store)
    with pytest.raises(ValueError):
        service.find_patient("")

def test_find_practitioner_success():
    store = SmartCareDataStore()
    service = PractitionerService(store)
    practitioner = service.register_practitioner("D1", "Dr. Chen", "GP")
    found = service.find_practitioner("D1")
    assert found is practitioner

def test_cancel_appointment_success():
    store = SmartCareDataStore()
    pat_service = PatientService(store)
    prac_service = PractitionerService(store)
    appt_service = AppointmentService(store)
    
    pat_service.register_patient("P1", "Alice")
    prac_service.register_practitioner("D1", "Dr. Chen", "GP")
    appt = appt_service.book_appointment("A1", "P1", "D1", datetime(2026, 10, 1, 9, 0))
    assert appt.status.value == "scheduled"
    
    cancelled = appt_service.cancel_appointment("A1")
    assert cancelled is appt
    assert cancelled.status.value == "cancelled"

def test_cancel_appointment_twice():
    store = SmartCareDataStore()
    pat_service = PatientService(store)
    prac_service = PractitionerService(store)
    appt_service = AppointmentService(store)
    
    pat_service.register_patient("P1", "Alice")
    prac_service.register_practitioner("D1", "Dr. Chen", "GP")
    appt_service.book_appointment("A1", "P1", "D1", datetime(2026, 10, 1, 9, 0))
    appt_service.cancel_appointment("A1")
    
    with pytest.raises(ValueError):
        appt_service.cancel_appointment("A1")
