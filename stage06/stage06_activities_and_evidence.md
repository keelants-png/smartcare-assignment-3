# Stage 6 activities and evidence

**Group/tutorial:** Solo Group
**Members, GitHub usernames and cohorts:** Keelan (UG)
**Repository URL:** https://github.com/keelants-png/smartcare-assignment-3

## A Requirement to issue activities
**FR-02 Patient Search:** Look up a registered patient by their unique ID. Valid ID returns the stored Patient. Missing ID raises LookupError. Blank ID raises ValueError.
**FR-06 Appointment Cancellation with FR-07 retained history:** Cancel a scheduled appointment and retain it in the system for history. Status changes to 'cancelled'. The object is not deleted. Cancelling a cancelled appointment raises ValueError.

## B Commit quality
- **Weak:** "fix stuff". 
- **Strong:** "Stage 6: Implement lookups and cancellation with tests". The strong message clearly explains what was done.

## E Team workflow agreement
Solo assignment. Standard practices followed.

## J Contributions
**Member:** Keelan
- **Implementation:** Implemented `find_patient`, `find_practitioner`, and `cancel_appointment` in `services.py`.
- **Testing:** Created `tests/test_services.py` with 6 new tests to verify the implementations.

## K Exit question
**Why is a high commit count not necessarily evidence of strong contribution?**
Because someone could make 100 tiny, meaningless commits. Contribution is judged by the quality and correctness of the code and tests, not just the number of times you clicked commit.

## L Stage 6 formative questions
1. **What is version control?** A system that records changes to files over time.
2. **Why is a feature branch useful?** It allows you to work on a new feature without messing up the main codebase.
3. **What makes a commit a good engineering commit?** A clear message explaining *what* and *why*.
4. **What is a pull request?** A request to merge a feature branch into the main branch for review.
5. **What is the purpose of code review?** To catch bugs and ensure code quality before merging.
6. **What does a Git diff show?** The exact lines of code added, removed, or changed.
7. **What is a Definition of Done?** A clear list of criteria that must be met before a task is complete.
8. **What is the appropriate role of GitHub Copilot in pull-request review?** To suggest potential issues, but humans make the final call.
9. **Why should individual contribution not be judged only by commit count?** It encourages gaming the system instead of writing good code.
10. **What is the Stage 6 engineering rule?** Work on focused branches, write meaningful commits, and ensure review before merging.

## M Completion and handover
- **Test command:** `python3 -m pytest`
- **Observed result:** `14 passed`
- **Stage 7 handover status:** Ready