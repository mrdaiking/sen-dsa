#!/usr/bin/env python3
"""
DSA Review Scheduler CLI Tool

A spaced repetition tool for DSA algorithms stored in a GitHub repo.
Scans for .meta.yaml files, manages reviews, and logs progress.

Usage:
    python review_scheduler.py --due
    python review_scheduler.py --add Day1/two_sum.py
    python review_scheduler.py --log Day1/two_sum.py
"""

import argparse
import datetime
import os
import pathlib
import yaml

# Constants
META_EXT = '.meta.yaml'
LOG_FILE = 'review_log.csv'

def load_meta(meta_path):
    """Load metadata from YAML file."""
    with open(meta_path, 'r') as f:
        return yaml.safe_load(f)

def is_due(meta, today):
    """Check if algorithm is due for review today."""
    learned_at = datetime.datetime.strptime(meta['learned_at'], '%Y-%m-%d').date()
    intervals = meta.get('review_intervals', [1, 3, 7, 14, 30])
    for days in intervals:
        review_date = learned_at + datetime.timedelta(days=days)
        if review_date <= today:
            return True
    return False

def find_meta_files(root_dir='.'):
    """Find all .meta.yaml files in subdirectories."""
    meta_files = []
    for path in pathlib.Path(root_dir).rglob(f'*{META_EXT}'):
        meta_files.append(path)
    return meta_files

def load_review_log():
    """Load review log from CSV."""
    log = {}
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            for line in f:
                date_str, file_path = line.strip().split(',')
                date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                if file_path not in log:
                    log[file_path] = []
                log[file_path].append(date)
        # Sort dates
        for path in log:
            log[path].sort()
    return log

def get_last_review_and_missed(file_path, log, today):
    """Get last review date and days missed."""
    if file_path in log and log[file_path]:
        last_review = log[file_path][-1]
        days_missed = (today - last_review).days
        return last_review, days_missed
    return None, None

def list_due_with_stats():
    """List due with last review and missed days."""
    today = datetime.date.today()
    meta_files = find_meta_files()
    log = load_review_log()
    due_list = []
    for meta_file in meta_files:
        try:
            meta = load_meta(meta_file)
            if is_due(meta, today):
                algo_path = str(meta_file).replace(META_EXT, '')
                last_review, days_missed = get_last_review_and_missed(algo_path, log, today)
                due_list.append({
                    'name': meta['name'],
                    'path': algo_path,
                    'day': (today - datetime.datetime.strptime(meta['learned_at'], '%Y-%m-%d').date()).days,
                    'last_review': last_review,
                    'days_missed': days_missed
                })
        except Exception as e:
            print(f"Error loading {meta_file}: {e}")
    return due_list

def add_meta(file_path):
    """Interactively create .meta.yaml for a new algorithm."""
    meta_file = pathlib.Path(file_path).with_suffix(META_EXT)
    if meta_file.exists():
        print(f"Meta file already exists: {meta_file}")
        return

    name = input("Algorithm name: ")
    tags = input("Tags (comma-separated): ").split(',')
    tags = [tag.strip() for tag in tags]
    difficulty = int(input("Difficulty (1-10): "))
    learned_at = datetime.date.today().isoformat()

    meta = {
        'name': name,
        'tags': tags,
        'difficulty': difficulty,
        'learned_at': learned_at,
        'confidence': 5,  # Default
        'review_intervals': [1, 3, 7, 14, 30]
    }

    with open(meta_file, 'w') as f:
        yaml.dump(meta, f)
    print(f"Created {meta_file}")

def log_review(py_file):
    """Log a review for an algorithm."""
    today = datetime.date.today().isoformat()
    with open(LOG_FILE, 'a') as f:
        f.write(f"{today},{py_file}\n")
    print(f"Logged review for {py_file}")

def generate_ics(due_list, output_file='reviews.ics'):
    """Generate a simple .ics file for due reviews."""
    ics_content = "BEGIN:VCALENDAR\nVERSION:2.0\n"
    for item in due_list:
        today_str = datetime.date.today().isoformat().replace('-', '')
        ics_content += f"BEGIN:VEVENT\nSUMMARY:Review {item['name']}\nDTSTART:{today_str}T090000\nEND:VEVENT\n"
    ics_content += "END:VCALENDAR\n"
    with open(output_file, 'w') as f:
        f.write(ics_content)
    print(f"Generated {output_file}")

def add_all_meta(root_dir='.', base_learned_at='2025-09-19'):
    """Create .meta.yaml for all .py files without meta."""
    base_date = datetime.datetime.strptime(base_learned_at, '%Y-%m-%d').date()
    for path in pathlib.Path(root_dir).rglob('*.py'):
        meta_file = path.with_suffix('.meta.yaml')
        if not meta_file.exists():
            # Extract day number from path
            day_match = None
            for part in path.parts:
                if part.startswith('Day') and part[3:].replace('-', '').isdigit():
                    day_str = part[3:].split('-')[0]  # Handle Day24-5
                    day_match = int(day_str)
                    break
            learned_date = base_date + datetime.timedelta(days=day_match - 1) if day_match else base_date
            # Default meta
            meta = {
                'name': path.stem.replace('_', ' ').title(),
                'tags': ['dsa'],
                'difficulty': 5,
                'learned_at': learned_date.isoformat(),
                'confidence': 5,
                'review_intervals': [1, 3, 7, 14, 30]
            }
            with open(meta_file, 'w') as f:
                yaml.dump(meta, f)
            print(f"Created {meta_file}")

def main():
    parser = argparse.ArgumentParser(description="DSA Review Scheduler")
    parser.add_argument('--due', action='store_true', help="List due reviews")
    parser.add_argument('--add', metavar='FILE', help="Add new algorithm meta")
    parser.add_argument('--add-all', action='store_true', help="Add meta for all .py files without meta")
    parser.add_argument('--log', metavar='FILE', help="Log review for algorithm")
    parser.add_argument('--ics', action='store_true', help="Generate .ics for due reviews")

    args = parser.parse_args()

    if args.due:
        due_list = list_due_with_stats()
        if not due_list:
            print("No reviews due today!")
        else:
            print("Due for review today:")
            for item in due_list:
                last_str = f"Last reviewed: {item['last_review']} ({item['days_missed']} days ago)" if item['last_review'] else "Never reviewed"
                print(f"- {item['name']} ({item['path']}) - Day {item['day']} - {last_str}")
        if args.ics:
            generate_ics(due_list)

    elif args.add:
        add_meta(args.add)

    elif args.add_all:
        add_all_meta()

    elif args.log:
        log_review(args.log)

    else:
        parser.print_help()

if __name__ == '__main__':
    main()