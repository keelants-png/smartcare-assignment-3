import pytest
from datetime import datetime
from smartcare.data_store import SmartCareDataStore
from smartcare.services import PatientService, PractitionerService, AppointmentService

def test_list_practitioner_appointments():
    store = SmartCareDataStore(); pat_s = PatientService(store)
    prac_s = PractitionerService(store); appt_s = AppointmentService(store)
    pat_s.register_patient("P1", "Alice")
    prac_s.register_practitioner("D1", "Dr. Chen", "GP"); prac_s.register_practitioner("D2", "Dr. Bob", "GP")
    appt_s.book_appointment("A1", "P1", "D1", datetime(2026, 10, 1, 9, 0))
    appt_s.book_appointment("A2", "P1", "D1", datetime(2026, 10, 1, 10, 0))
    appt_s.book_appointment("A3", "P1", "D2", datetime(2026, 10, 1, 11, 0))
    res = appt_s.list_practitioner_appointments("D1")
    assert len(res) == 2 and res[0].appointment_id == "A1" and res[1].appointment_id == "A2"
