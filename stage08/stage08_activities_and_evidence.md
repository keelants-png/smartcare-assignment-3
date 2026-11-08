# Stage 8 activities and evidence
**Group/tutorial:** Solo Group
**Members:** Keelan (UG)

## C & D Debugging F8-01 (Practitioner Conflict)
- **Root cause:** `has_practitioner_conflict` only checked ID, not time or status.
- **Repair:** Updated to check date/time and SCHEDULED status.

## C & D Debugging F8-02 (Cancelled History)
- **Root cause:** `find_appointment` was missing retrieval logic for cancelled states.
- **Repair:** Updated to return the appointment regardless of status.

## J Contributions
**Member:** Keelan
- Fixed bugs in `data_store.py`.
- Created `test_regressions.py` to verify cancelled appointments are retrievable and conflicts are blocked.