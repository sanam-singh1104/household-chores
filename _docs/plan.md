# Household Chores Manager — Plan

## Idea
A tool for managing shared household chores, aimed at roommates
(equal peers sharing a flat). The core goal is splitting chores
**fairly**, so the app owns the rota instead of roommates having
to negotiate it.

## Target users
Roommates / housemates sharing a home — treated as equal peers,
not a parent-child or manager-report relationship.

## Core concept
Chores are assigned by **automatic rotation**: the app cycles each
recurring chore between roommates on its own schedule, so nobody
has to divvy things up manually. Completing a chore earns points,
and the whole house looks at one shared dashboard.

## Features
1. **Roommates & chores setup**
   - Add roommates to the household.
   - Define recurring chores, each with a repeat frequency
     (e.g. weekly, fortnightly).

2. **Automatic rotation**
   - The app assigns each chore to the next roommate in turn,
     on that chore's schedule.
   - Fairness is handled by the rotation, not by manual choice.

3. **Check off + points**
   - When it's your turn, mark the chore as done.
   - Completing a chore earns points (default: every chore = 1 point;
     could later be weighted so harder chores are worth more).

4. **Shared dashboard**
   - One screen the whole household sees, showing:
     - the current rota and whose turn each chore is,
     - anything overdue,
     - a leaderboard ranking roommates by points.

## Out of scope (for now)
- Personal / per-user private views (dashboard is shared).
- Notifications, reminders, mobile app.
- Payments, expenses, or anything beyond chores.

## Tech
- Django (Python web framework).
