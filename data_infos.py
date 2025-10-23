#!/usr/bin/env python3
"""Compute per-year observation counts and unique species counts from CSV.

Usage:
  python data_infos.py --csv observations_swiss.csv --out results.csv

Outputs CSV with header: year,observations,species
"""
import argparse
import csv
import re
import sys

def detect_columns(headers):
    headers = [h.strip() for h in (headers or [])]
    obs_col = None
    taxon_col = None
    observer_col = None
    obs_candidates = ['observed_on', 'observed_on_string', 'observed_at', 'date', 'date_observed', 'observed_on']
    taxon_candidates = ['taxon_id', 'taxon', 'taxon_name', 'scientific_name']
    observer_candidates = ['observer_id', 'user_id', 'observer', 'user_login']

    for c in obs_candidates:
        if c in headers:
            obs_col = c
            break
    if obs_col is None:
        for h in headers:
            if 'observ' in h.lower() or 'date' in h.lower():
                obs_col = h
                break

    for c in taxon_candidates:
        if c in headers:
            taxon_col = c
            break
    if taxon_col is None:
        for h in headers:
            if 'taxon' in h.lower() or 'scientific' in h.lower() or 'species' in h.lower():
                taxon_col = h
                break

    for c in observer_candidates:
        if c in headers:
            observer_col = c
            break
    if observer_col is None:
        for h in headers:
            if 'observer' in h.lower() or 'user' in h.lower() or 'observer_id' in h.lower():
                observer_col = h
                break

    return obs_col, taxon_col, observer_col


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--csv', required=True)
    ap.add_argument('--out', default='')
    args = ap.parse_args()

    try:
        f = open(args.csv, newline='', encoding='utf-8')
    except Exception as e:
        sys.stderr.write(f"Error opening CSV: {e}\n")
        sys.exit(1)

    reader = csv.DictReader(f)
    obs_col, taxon_col, observer_col = detect_columns(reader.fieldnames)

    if obs_col is None:
        sys.stderr.write('Error: could not find an observed/date column in CSV headers\n')
        sys.exit(2)
    if taxon_col is None:
        sys.stderr.write('Error: could not find a taxon column in CSV headers\n')
        sys.exit(2)
    if observer_col is None:
        sys.stderr.write('Error: could not find an observer id column in CSV headers\n')
        sys.exit(2)

    years = {}
    year_re = re.compile(r"(\d{4})")

    for row in reader:
        val = row.get(obs_col, '')
        if val is None:
            continue
        m = year_re.search(val)
        if not m:
            continue
        y = m.group(1)
        taxon = row.get(taxon_col, '') or ''
        taxon = taxon.strip()
        if y not in years:
            years[y] = {'obs': 0, 'taxa': set(), 'observers': set()}
        years[y]['obs'] += 1
        if taxon:
            years[y]['taxa'].add(taxon)
        obs_id = row.get(observer_col, '') or ''
        obs_id = obs_id.strip()
        if obs_id:
            years[y]['observers'].add(obs_id)

    lines = ["year,observations,species,observers"]
    for y in sorted(years.keys()):
        obs = years[y]['obs']
        species = len(years[y]['taxa'])
        observers = len(years[y]['observers'])
        lines.append(f"{y},{obs},{species},{observers}")

    out_text = "\n".join(lines) + "\n"
    if args.out:
        try:
            with open(args.out, 'w', encoding='utf-8') as outf:
                outf.write(out_text)
            print(f"Wrote results to {args.out}")
        except Exception as e:
            sys.stderr.write(f"Error writing output: {e}\n")
            sys.exit(3)
    else:
        sys.stdout.write(out_text)

    f.close()

if __name__ == '__main__':
    main()
