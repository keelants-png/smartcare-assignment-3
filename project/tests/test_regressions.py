import pytest
from datetime import datetime
from smartcare.data_store import SmartCareDataStore
from smartcare.services import PatientService, PractitionerService, AppointmentService

def test_regression_practitioner_conflict():
    store = SmartCareDataStore(); pat_s = PatientService(store)
    prac_s = PractitionerService(store); appt_s = AppointmentService(store)
    pat_s.register_patient("P1", "Alice"); prac_s.register_practitioner("D1", "Dr. Chen", "GP")
    appt_s.book_appointment("A1", "P1", "D1", datetime(2026, 10, 1, 9, 0))
    with pytest.raises(ValueError): appt_s.book_appointment("A2", "P1", "D1", datetime(2026, 10, 1, 9, 0))

def test_regression_find_cancelled_appointment():
    store = SmartCareDataStore(); pat_s = PatientService(store)
    prac_s = PractitionerService(store); appt_s = AppointmentService(store)
    pat_s.register_patient("P1", "Alice"); prac_s.register_practitioner("D1", "Dr. Chen", "GP")
    appt = appt_s.book_appointment("A1", "P1", "D1", datetime(2026, 10, 1, 9, 0))
    appt_s.cancel_appointment("A1")
    found = appt_s.find_appointment("A1")
    assert found is appt and found.status.value == "cancelled"
