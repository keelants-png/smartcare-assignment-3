# Stage 7 activities and evidence

**Group/tutorial:** Solo Group
**Members, GitHub usernames and cohorts:** Keelan (UG)
**Repository URL:** https://github.com/keelants-png/smartcare-assignment-3

## A Tutorial and test design
**Activity 1: Requirement to test**
- **FR-01 Register patient:** Positive: Register valid patient. Negative: Blank name raises ValueError.
- **FR-05 Prevent practitioner conflict:** Positive: Book different practitioners at same time. Negative: Book same practitioner at same time raises ValueError.
- **FR-06 Cancel appointment:** Positive: Cancel scheduled appointment. Negative: Cancel cancelled appointment raises ValueError.
- **FR-07 Retain cancelled history:** Positive: Find cancelled appointment by ID.

**Activity 2: Strong or weak assertion**
- `assert True` -> Weak.
- `assert appointment is not None` -> Weak.
- `assert appointment.status == AppointmentStatus.CANCELLED` -> Strong (checks exact required state).
- `assert data_store.find_appointment('A1') is appointment` -> Strong (proves object identity).

**Activity 3: Boundary thinking**
- Blank IDs -> ValueError.
- Same-time practitioner bookings -> ValueError.
- Cancelling a CANCELLED appointment -> ValueError.

**Activity 4: Critique GitHub Copilot tests**
- Diagnosis: Copilot generated tests that pass but prove nothing (`assert True`).
- Revised intention: Rewrite tests to assert actual domain state changes and specific exceptions.

## B Establish requirement to test traceability
| Requirement | Acceptance Criterion | Test ID | Test Type | Test Name | Expected Behaviour |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FR-01 | AC-01.2 | TEST-01 | Negative | `test_patient_blank_id_rejected` | Blank ID raises ValueError. |
| FR-04 | AC-03.1 | TEST-02 | Positive | `test_book_appointment_success` | Valid booking stores SCHEDULED appointment. |
| FR-05 | AC-04.1 | TEST-03 | Boundary | `test_book_appointment_practitioner_conflict` | Same practitioner/time raises ValueError. |
| FR-06 | AC-05.1 | TEST-04 | Positive | `test_appointment_cancellation_changes_status` | Cancel changes status to CANCELLED. |

## C Write domain tests
I wrote 8 domain tests to check constructor validation, default status (SCHEDULED), and guarded cancellation logic.

## D Write service tests
Extended service tests to check that booking requires registered participants, prevents practitioner time conflicts, and correctly stores the appointment.

## E Add negative and boundary cases
Included tests for blank IDs, repeated cancellation, and practitioner conflicts to ensure invalid operations preserve state and raise correct exceptions.

## H Run the full regression suite
- **Command:** `python3 -m pytest`
- **Working directory:** `project/`
- **Result:** `25 passed`

## L Stage 7 formative questions
1. **What question does verification answer?** Are we building the product right?
2. **What question does validation answer?** Are we building the right product?
3. **What is a unit test?** A test that checks a single isolated piece of code.
4. **What is a pytest fixture?** A way to provide fresh setup data for tests.
5. **What is parametrisation?** Running the same test with different inputs.
6. **What is regression testing?** Re-running tests to ensure new code didn't break old features.
7. **What does code coverage tell us?** Which lines were executed, but not if the assertions are strong.
8. **What makes an assertion weak?** If it can pass even when the code is broken.
9. **What is the role of Copilot as a test assistant?** To suggest edge cases, but humans must write the assertions.
10. **What is the Stage 7 engineering rule?** A test is only as good as the assertion it makes.

## M Completion and handover
- **Observed result:** `22 passed`
- **Stage 8 handover status:** Ready