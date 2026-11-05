#!/usr/bin/env python3
"""Quick-reference calculators for a beginner farm.

Usage examples:
    python3 quick_reference.py crops
    python3 quick_reference.py spacing tomato --bed-area 200
    python3 quick_reference.py water tomato --plants 12 --weekly-rain 0.5
    python3 quick_reference.py fertilizer --npk 10-10-10 --area 200 --n-lb-per-1000 1
    python3 quick_reference.py harvest carrot --sow-date 2027-04-05
    python3 quick_reference.py frost --last-frost 2027-04-15 --weeks-before 6

Values are general beginner guidelines. Always check seed packets and local
extension-office advice for your climate.
"""
import argparse
import sys
from datetime import date, timedelta

# spacing_in: in-row spacing; row_in: space between rows
# water_in_wk: inches of water per week in active growth
# days: days to maturity; n_lb_1000: lb actual nitrogen per 1,000 sq ft per season
CROPS = {
    "tomato":  {"spacing_in": 24, "row_in": 36, "water_in_wk": 1.5, "days": 80,  "n_lb_1000": 1.5, "season": "warm"},
    "lettuce": {"spacing_in": 8,  "row_in": 12, "water_in_wk": 1.0, "days": 50,  "n_lb_1000": 1.0, "season": "cool"},
    "bean":    {"spacing_in": 4,  "row_in": 24, "water_in_wk": 1.0, "days": 55,  "n_lb_1000": 0.5, "season": "warm"},
    "carrot":  {"spacing_in": 2,  "row_in": 12, "water_in_wk": 1.0, "days": 70,  "n_lb_1000": 1.0, "season": "cool"},
    "pepper":  {"spacing_in": 18, "row_in": 30, "water_in_wk": 1.25,"days": 75,  "n_lb_1000": 1.5, "season": "warm"},
    "squash":  {"spacing_in": 36, "row_in": 48, "water_in_wk": 1.5, "days": 55,  "n_lb_1000": 1.5, "season": "warm"},
    "potato":  {"spacing_in": 12, "row_in": 30, "water_in_wk": 1.25,"days": 100, "n_lb_1000": 2.0, "season": "cool"},
}

GAL_PER_SQFT_PER_INCH = 0.623  # 1 inch of water over 1 sq ft ≈ 0.623 gallons


def get_crop(name):
    key = name.lower().rstrip("s")
    if key not in CROPS:
        sys.exit(f"Unknown crop '{name}'. Known crops: {', '.join(sorted(CROPS))}")
    return key, CROPS[key]


def cmd_crops(_):
    print(f"{'Crop':<9}{'Spacing':>9}{'Row gap':>9}{'Water/wk':>10}{'Days':>6}{'N lb/1000sf':>13}  Season")
    for k, c in sorted(CROPS.items()):
        print(f"{k:<9}{str(c['spacing_in'])+' in':>9}{str(c['row_in'])+' in':>9}"
              f"{str(c['water_in_wk'])+' in':>10}{c['days']:>6}{c['n_lb_1000']:>13}  {c['season']}")


def cmd_spacing(a):
    k, c = get_crop(a.crop)
    sq_ft_per_plant = (c["spacing_in"] * c["row_in"]) / 144
    n = int(a.bed_area / sq_ft_per_plant)
    print(f"{k.title()}: plants {c['spacing_in']} in apart in rows {c['row_in']} in apart")
    print(f"Each plant uses ~{sq_ft_per_plant:.2f} sq ft")
    print(f"A {a.bed_area:g} sq ft bed fits about {n} plants")


def cmd_water(a):
    k, c = get_crop(a.crop)
    need_in = max(c["water_in_wk"] - a.weekly_rain, 0)
    area = a.plants * (c["spacing_in"] * c["row_in"]) / 144
    gallons = need_in * area * GAL_PER_SQFT_PER_INCH
    print(f"{k.title()} needs ~{c['water_in_wk']} in/week; rain covers {a.weekly_rain} in")
    print(f"Irrigate {need_in:.2f} in/week over ~{area:.0f} sq ft = ~{gallons:.1f} gallons/week")
    print(f"Tip: 2 deep waterings/week (~{gallons/2:.1f} gal each) beat daily sprinkles.")


def cmd_fertilizer(a):
    try:
        n, p, k = (float(x) for x in a.npk.split("-"))
    except ValueError:
        sys.exit("--npk must look like 10-10-10")
    if n <= 0:
        sys.exit("Fertilizer must contain nitrogen (first number > 0)")
    if a.crop:
        _, c = get_crop(a.crop)
        target = c["n_lb_1000"]
    else:
        target = a.n_lb_per_1000
    n_needed = target * a.area / 1000            # lb of actual N
    product_lb = n_needed / (n / 100)
    print(f"Target: {target} lb N per 1,000 sq ft over {a.area:g} sq ft = {n_needed:.2f} lb actual N")
    print(f"Using {a.npk}: apply ~{product_lb:.1f} lb ({product_lb*16:.0f} oz) of fertilizer")
    print("Split into 2-3 feedings (planting, flowering, fruit set) rather than all at once.")


def cmd_harvest(a):
    k, c = get_crop(a.crop)
    sow = date.fromisoformat(a.sow_date)
    print(f"{k.title()} sown {sow} -> ready around {sow + timedelta(days=c['days'])} ({c['days']} days)")


def cmd_frost(a):
    lf = date.fromisoformat(a.last_frost)
    print(f"Start indoors {a.weeks_before} weeks before last frost: {lf - timedelta(weeks=a.weeks_before)}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd")

    sub.add_parser("crops", help="show the built-in crop table").set_defaults(fn=cmd_crops)

    s = sub.add_parser("spacing", help="how many plants fit in a bed")
    s.add_argument("crop"); s.add_argument("--bed-area", type=float, required=True, help="sq ft")
    s.set_defaults(fn=cmd_spacing)

    w = sub.add_parser("water", help="weekly watering needs")
    w.add_argument("crop"); w.add_argument("--plants", type=int, required=True)
    w.add_argument("--weekly-rain", type=float, default=0.0, help="inches of rain this week")
    w.set_defaults(fn=cmd_water)

    f = sub.add_parser("fertilizer", help="how much fertilizer to apply")
    f.add_argument("--npk", required=True, help="e.g. 10-10-10")
    f.add_argument("--area", type=float, required=True, help="sq ft")
    f.add_argument("--crop", help="use that crop's typical nitrogen need")
    f.add_argument("--n-lb-per-1000", type=float, default=1.0, help="used if no --crop")
    f.set_defaults(fn=cmd_fertilizer)

    h = sub.add_parser("harvest", help="estimate harvest date")
    h.add_argument("crop"); h.add_argument("--sow-date", required=True, help="YYYY-MM-DD")
    h.set_defaults(fn=cmd_harvest)

    fr = sub.add_parser("frost", help="seed-starting date from last frost")
    fr.add_argument("--last-frost", required=True, help="YYYY-MM-DD")
    fr.add_argument("--weeks-before", type=int, default=6)
    fr.set_defaults(fn=cmd_frost)

    a = p.parse_args()
    if not a.cmd:
        p.print_help(); print(); cmd_crops(a); return
    a.fn(a)


if __name__ == "__main__":
    main()
