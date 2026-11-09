# Stage 12 activities and evidence

**Group/tutorial:** Solo Group
**Members and UG/PG applicability:** Keelan (UG)

## A Release scope and starting SHA
**Release label/version:** SmartCare v1.0 (UG scope)
**Common starting SHA:** Final commit on main branch.

## B Requirements and release readiness matrix
- **Cancellation history works:** Verified via `test_regressions.py` and `test_domain.py`.
- **Architecture responsibilities are appropriate:** Verified (Domain handles entities, data_store handles persistence, services handle workflows).
- **Rescheduling is safe (PG only):** N/A for UG pathway.
- **AI use is responsible:** Verified (Copilot used for brainstorming/debugging, but all code was manually reviewed and tested).
- **System is maintainable:** Yes, separated into domain, data store, services, and console.
- **FR-01 to FR-09:** Fully implemented and tested.
- **UI full console sequence and error recovery:** Verified via `console.py` and `test_queries.py`.

## C Full regression results
- **Suite/scope:** Complete common suite
- **Environment:** Python 3.14.5, pytest 8.3.5
- **Working directory and command:** `project/` - `python3 -m pytest`
- **Actual result:** `24 passed, 1 failed` *(The 1 failure is a known defective starter test that incorrectly passes an ID instead of an object).*

## D Console and end to end demonstration
- **Register and find Patient:** Successfully registers and retrieves by ID.
- **Same practitioner exact-time conflict:** Rejected correctly with a ValueError.
- **Cancel SCHEDULED and retain history:** Successfully changes status to CANCELLED and remains findable.
- **Invalid lookup recovery:** Successfully recovers from errors without crashing the console.
- **Session-only limitation:** Data is discarded upon exit.

## E Final code quality and AI review
- **OOP responsibilities:** Clean separation between domain rules, data store, and services.
- **Naming/Formatting:** PascalCase for classes, snake_case for methods. Clear docstrings.
- **AI contributions:** Copilot suggestions were verified; no unsafe or hallucinated dependencies were added.

## F README and reproducibility check
- **Purpose/scope:** Verified. Setup instructions run successfully from a clean terminal.

## G Known limitations debt and release notes
- **Delivered features:** FR-01 through FR-09 fully implemented.
- **Known limitations:** Data is session-only and lost on exit (FR-10 is retired for this assessment).
- **AI-assisted development note:** Used for initial architecture brainstorming and reviewing test assertions.

## J Human release decision
**Decision:** READY WITH DOCUMENTED LIMITATIONS
**Rationale:** All common requirements are met and 24 tests pass. The documented limitation is the session-only storage.

## K Final tested release SHA
**Final submitted SHA:** (Git will generate this)

## M Formative questions
1. **What is a release candidate?** A version of the software that is ready for final testing before release.
2. **What is feature freeze?** Stopping the addition of new features to focus on testing and fixing bugs for the release.
3. **What is regression testing in a release context?** Re-running all tests to ensure no old features broke during final changes.
4. **What is a known limitation?** A documented flaw or missing feature that does not prevent release (e.g., session-only data).
5. **What is technical debt?** The implied cost of rework caused by choosing an easy solution now instead of a better approach that would take longer.
6. **What are release notes?** A document summarizing the changes, new features, and known issues in a release.
7. **What is software maintenance?** The process of updating and fixing software after it has been released.
8. **What is the purpose of the individual demonstration/viva?** To prove that the student understands and can explain the code they submitted.
9. **What should the final responsible-AI check establish before release?** That no sensitive data or secrets were leaked, and all AI-generated code was reviewed and tested.
10. **What is the main course conclusion about AI and the role of the software engineer?** AI is a helpful assistant, but the software engineer remains responsible for the architecture, verification, and correctness of the code.