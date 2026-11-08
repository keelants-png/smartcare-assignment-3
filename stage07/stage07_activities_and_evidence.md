# Stage 7 activities and evidence
**Group/tutorial:** Solo Group
**Members:** Keelan (UG)

## A Tutorial and test design
- `assert True` -> Weak (proves nothing).
- `assert appointment.status == AppointmentStatus.CANCELLED` -> Strong (checks exact required state).

## B Traceability
Tested FR-01, FR-05, FR-06, and FR-07 using positive, negative, and boundary cases.

## J Contributions
**Member:** Keelan
- Wrote 8 domain tests (`test_domain.py`) and 3 new service tests to check constructor validation, default status, and guarded cancellation logic.
- **Result:** 22 passed.