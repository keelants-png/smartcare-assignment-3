# Stage 6 activities and evidence
**Group/tutorial:** Solo Group
**Members:** Keelan (UG)
**Repository URL:** https://github.com/keelants-png/smartcare-assignment-3

## A Requirement to issue activities
Implemented FR-02 (Patient Search) and FR-06/07 (Cancellation and Retained History). Valid IDs return the stored object, missing IDs raise LookupError, and blank IDs raise ValueError.

## J Contributions
**Member:** Keelan
- **Implementation:** Implemented `find_patient`, `find_practitioner`, and `cancel_appointment` in `services.py`.
- **Testing:** Created `tests/test_services.py` with 6 new tests to verify the implementations.
- **Result:** 14 passed.