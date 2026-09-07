# Backlog

Ordered, small tasks for building the app described in [`_docs/plan.md`](_docs/plan.md).

1. **Project setup** — Create the Django project and a `chores` app, wire it
   into `INSTALLED_APPS`, set up the default SQLite database, and confirm the
   dev server runs.

2. **Household & Roommate models** — Add a `Household` model and a `Roommate`
   model (name, belongs to a household). Register both in the Django admin.

3. **Chore model** — Add a `Chore` model (name, household, repeat frequency
   e.g. weekly/fortnightly, points value defaulting to 1). Register in admin.

4. **Rotation order** — Add a way to order roommates per chore (e.g. an
   ordered list or an `order` field) and a `current_assignee` (or equivalent)
   on `Chore` so each chore knows whose turn it is.

5. **Rotation advance logic** — Write the function/method that, given a
   chore, picks the next roommate in the rotation (wrapping around), without
   wiring it to any view yet. Cover it with unit tests.

6. **ChoreCompletion model & check-off** — Add a `ChoreCompletion` model
   (chore, roommate, completed_at, points_awarded). Add a view/action to mark
   a chore done: records the completion, awards points, and advances the
   rotation (using the logic from step 5).

7. **Due dates & overdue tracking** — Add a `next_due` date on `Chore`,
   computed from its frequency and last completion. Add a helper/property to
   flag a chore as overdue.

8. **Points leaderboard** — Add a query/view that totals each roommate's
   points from `ChoreCompletion` and ranks them.

9. **Shared dashboard view** — Build the single dashboard page: current rota
   (chore → whose turn), overdue chores, and the leaderboard, using the
   pieces from steps 6-8.

10. **Setup UI for roommates & chores** — Add simple forms/pages to add
    roommates and define chores, so the household doesn't depend on the
    Django admin for day-to-day setup.

11. **Polish pass** — Basic styling for the dashboard, empty states (no
    roommates/chores yet), and a smoke-test walkthrough of the full flow
    (add roommates → add chore → check off → see dashboard update).
