"""Pure query helpers for SmartCare."""
from smartcare.domain import Appointment, AppointmentStatus

def appointment_sort_key(appointment: Appointment) -> tuple:
    return (appointment.date_time, appointment.appointment_id)

def select_appointments(
    appointments: list[Appointment],
    practitioner_id: str,
    status: AppointmentStatus | None = None,
) -> list[Appointment]:
    filtered = []
    for appt in appointments:
        if appt.practitioner.practitioner_id == practitioner_id:
            if status is None or appt.status == status:
                filtered.append(appt)
    filtered.sort(key=appointment_sort_key)
    return filtered
