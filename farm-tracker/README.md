# 🌱 My Farm Project Tracker

A simple, local, plain-text system for planning and tracking a small farm. Everything is Markdown (plus one Python helper), so it works in any text editor and can be versioned with git.

## Project Overview

| Item | Details (edit me) |
|---|---|
| Farm name | Green Acre Starter Farm |
| Location / climate zone | _e.g. Zone 7b, last frost ~Apr 15, first frost ~Oct 25_ |
| Size | _e.g. 0.25 acre (≈ 10,900 sq ft)_ |
| Start date | _YYYY-MM-DD_ |
| Main crops | Tomatoes, lettuce, beans, carrots |
| Livestock (optional) | 6 laying hens |
| Water source | _e.g. well / municipal / rain barrels_ |

## Goals

1. **Season 1 (learning):** Grow 4 beginner-friendly crops successfully on a small plot.
2. **Track everything:** Record costs, tasks, and yields so next season is better.
3. **Break even** on operating costs by the end of Season 2.
4. **Sell surplus** at a local farmers' market (Season 2+).

## Files in this tracker

| File | Purpose | Update how often |
|---|---|---|
| `README.md` | Overview, goals, how-to (this file) | Rarely |
| `schedule.md` | Tasks by phase with dates and status | Weekly (or after any task) |
| `inventory.md` | Tools, seeds, fertilizer, pesticides, equipment | When you buy, use, or run low |
| `finances.md` | Budget, expense ledger, expected vs. actual revenue | Every purchase / sale |
| `quick_reference.py` | Calculators for spacing, watering, fertilizer, harvest dates | Run whenever you need a number |

## How to use it

1. **Start with this README** – fill in the overview table and goals.
2. **Plan in `schedule.md`** – list tasks per phase. Set status to `Pending`, `In Progress`, or `Completed`.
3. **Log purchases in two places** – add the item to `inventory.md` *and* a line to the ledger in `finances.md`.
4. **Check numbers before you buy/plant** – e.g. `python3 quick_reference.py spacing tomato --bed-area 200` tells you how many plants fit.
5. **Weekly 10-minute review** – update statuses, note what happened (weather, pests, yields), adjust next week's tasks.
6. **End of season** – compare *Budget vs. Actual* in `finances.md` and write lessons learned at the bottom of `schedule.md`.

## Editing tips

- Tables: add a row by copying an existing line and changing the values; columns don't need to line up perfectly.
- Dates: use `YYYY-MM-DD` so they sort correctly.
- Delete the _example_ rows once you've entered your own.
- Back up with git: `git add farm-tracker && git commit -m "Update farm log"`.

## Running the quick-reference tool

```bash
python3 quick_reference.py            # shows help and list of crops
python3 quick_reference.py crops      # table of all built-in crop data
```
Requires Python 3.8+ and no extra packages.
