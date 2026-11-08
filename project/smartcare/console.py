"""Interactive console for SmartCare."""
from datetime import datetime
from smartcare.domain import AppointmentStatus
from smartcare.data_store import SmartCareDataStore
from smartcare.services import PatientService, PractitionerService, AppointmentService

def parse_date_time(text: str) -> datetime:
    try:
        return datetime.strptime(text, "%Y-%m-%d %H:%M")
    except ValueError:
        raise ValueError("Use date/time format YYYY-MM-DD HH:MM")

def run_menu(data_store: SmartCareDataStore) -> None:
    pat_service = PatientService(data_store)
    prac_service = PractitionerService(data_store)
    appt_service = AppointmentService(data_store)

    while True:
        print("\nMAIN MENU")
        print("[1] Register patient\n[2] Find patient\n[3] Register practitioner\n[4] Find practitioner")
        print("[5] Book appointment\n[6] Cancel appointment\n[7] Find appointment\n[8] List appointments\n[0] Exit")
        choice = input("\nSelect an option: ")
        
        try:
            if choice == "1":
                pat_service.register_patient(input("Patient ID: "), input("Patient name: "))
                print("Patient registered successfully.")
            elif choice == "2":
                pat = pat_service.find_patient(input("Patient ID: "))
                print(f"Patient found. {pat.patient_id}: {pat.name}")
            elif choice == "3":
                prac_service.register_practitioner(input("Practitioner ID: "), input("Name: "), input("Specialty: "))
                print("Practitioner registered successfully.")
            elif choice == "4":
                prac = prac_service.find_practitioner(input("Practitioner ID: "))
                print(f"Practitioner found. {prac.practitioner_id}: {prac.name}, {prac.specialty}")
            elif choice == "5":
                appt_service.book_appointment(input("Appointment ID: "), input("Patient ID: "), input("Practitioner ID: "), parse_date_time(input("Date/time [YYYY-MM-DD HH:MM]: ")))
                print("Appointment booked successfully.")
            elif choice == "6":
                appt_service.cancel_appointment(input("Appointment ID: "))
                print("Appointment cancelled successfully.")
            elif choice == "7":
                appt = appt_service.find_appointment(input("Appointment ID: "))
                print(f"Appointment found. {appt.appointment_id} Status: {appt.status.value}")
            elif choice == "8":
                prid = input("Practitioner ID: ")
                s_in = input("Status [scheduled/cancelled/completed, blank = all]: ").strip()
                status = AppointmentStatus(s_in.lower()) if s_in else None
                results = appt_service.list_practitioner_appointments(prid, status)
                if not results: print("No appointments found.")
                for a in results: print(f"{a.appointment_id} | {a.date_time} | {a.status.value}")
            elif choice == "0":
                print("Goodbye. Session data discarded.")
                break
            else:
                print("Unknown choice. Choose a number from 0 to 8.")
        except Exception as e:
            print(f"Error: {e}")
