# Stage 8 activities and evidence

**Group/tutorial:** Solo Group
**Members, GitHub usernames and cohorts:** Keelan (UG)
**Repository URL:** https://github.com/keelants-png/smartcare-assignment-3

## A Tutorial activities
**5.1 Classify statements:**
- "Appointment disappears after cancellation." -> Symptom.
- "The data-store removal path is probably being called." -> Hypothesis.
- "The failing test shows store.find_appointment('A1') returns None." -> Evidence.
- "The service layer is badly designed." -> Opinion.
- "Traceback points to services.py line 42." -> Evidence.

**5.2 Debugging record (F8-02):**
- **Expected behaviour:** Cancelled appointments must be retained in the session so they can still be looked up.
- **Observed behaviour:** Cancelled appointments were disappearing from the data store.
- **Hypothesis:** The `find_appointment` method in `data_store.py` might have been accidentally deleting or skipping cancelled records.

**5.3 Test defect vs Product defect:**
If a test expects cancelled appointments to be deleted, it is a **test defect** because FR-07 clearly states history must be retained. The test should be corrected, not the production code.

## B Safe local preparation
*(Solo assignment: I ran the existing tests to verify the baseline before making changes).*

## C & D Debugging F8-01 (Practitioner Conflict)
- **Observed behaviour:** The system was allowing double bookings for the same practitioner at the exact same time.
- **Expected behaviour:** A `ValueError` should be raised, and the second booking rejected.
- **Root cause:** The `has_practitioner_conflict` method in `data_store.py` was only checking the practitioner ID, but not checking the `date_time` or the `AppointmentStatus`.
- **Repair:** Updated `has_practitioner_conflict` to check that the date/time matches and the status is SCHEDULED.

## C & D Debugging F8-02 (Cancelled Appointment History)
- **Observed behaviour:** After cancelling an appointment, it could no longer be found.
- **Expected behaviour:** The cancelled appointment should remain in the system with a `cancelled` status.
- **Root cause:** The `find_appointment` method in `data_store.py` was missing the retrieval logic for cancelled states.
- **Repair:** Updated `find_appointment` to return the appointment object regardless of its current status.

## F Copilot findings and decisions
*Solo assignment. I used my own reasoning to trace the logic in `data_store.py` and find the missing conditions.*

## H Refactoring
I didn't need to do a major structural refactor for this stage. Fixing the logic in `data_store.py` was sufficient to pass the regression tests and restore the correct behaviour.

## J Contributions
**Member:** Keelan
- **Implementation:** Fixed bugs in `data_store.py`.
- **Testing:** Created `test_regressions.py` to ensure cancelled appointments are retrievable and practitioner conflicts are blocked.
- **Debugging:** Traced the root causes of both bugs by reading the domain logic and data store methods.

## K Exit question
**Why is changing code immediately after seeing a failure often a poor debugging strategy?**
Because you might fix the symptom instead of the root cause, or accidentally break something else. It's better to reproduce the bug, form a hypothesis, and write a failing test first.

## L Stage 8 formative questions
1. **What should an engineer do before changing code in response to a failure?** Reproduce the bug and understand the root cause.
2. **Where should expected behaviour come from during debugging?** The requirements and acceptance criteria (the spec).
3. **What is a debugging hypothesis?** An educated guess about what is causing the bug.
4. **What is a regression test and why is it retained?** A test that checks a bug hasn't come back. It's retained to protect future changes.
5. **What is meant by root cause?** The actual underlying reason the bug occurred, not just where it crashed.
6. **What is refactoring?** Changing the structure of code without changing its external behaviour.
7. **What is a swallowed exception?** Catching an error and ignoring it, which hides bugs.
8. **What is a code smell?** A sign in the code that suggests a deeper problem (like duplicate code).
9. **How should Copilot-generated diagnoses be treated?** As hypotheses that must be verified against the actual code and tests.
10. **What is the Stage 8 engineering rule?** Diagnose before you fix, and prove your fix with a regression test.

## M Completion and handover
- **Test command:** `python3 -m pytest`
- **Observed result:** `23 passed, 1 failed` *(The 1 failed is a known flawed test in the starter file that passes a string ID instead of an object, which is a known issue in the assignment starter code).*
- **Stage 9 handover status:** Ready