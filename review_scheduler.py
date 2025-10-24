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
                # Normalize path without suffix
                normalized_path = str(pathlib.Path(file_path).with_suffix(''))
                if normalized_path not in log:
                    log[normalized_path] = []
                log[normalized_path].append(date)
        # Sort dates
        for path in log:
            log[path].sort()
    return log

def get_last_review_and_missed(file_path, log, today):
    """Get last review date and days missed."""
    # Check both with and without suffix
    paths_to_check = [file_path, pathlib.Path(file_path).with_suffix('')]
    for path in paths_to_check:
        path_str = str(path)
        if path_str in log and log[path_str]:
            last_review = log[path_str][-1]
            days_missed = (today - last_review).days
            return last_review, days_missed
    return None, None

def list_all_with_stats():
    """List all algorithms with stats."""
    today = datetime.date.today()
    meta_files = find_meta_files()
    log = load_review_log()
    all_list = []
    for meta_file in meta_files:
        try:
            meta = load_meta(meta_file)
            algo_path = str(meta_file).replace(META_EXT, '')
            last_review, days_missed = get_last_review_and_missed(algo_path, log, today)
            all_list.append({
                'name': meta['name'],
                'path': algo_path,
                'day': (today - datetime.datetime.strptime(meta['learned_at'], '%Y-%m-%d').date()).days,
                'last_review': last_review,
                'days_missed': days_missed
            })
        except Exception as e:
            print(f"Error loading {meta_file}: {e}")
    return all_list

def list_due_with_stats():
    """List due algorithms with stats."""
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
    
    # Auto-update confidence based on review count
    auto_update_confidence(py_file)

def auto_update_confidence(file_path):
    """Auto-update confidence based on review history and consistency."""
    log = load_review_log()
    normalized_path = str(pathlib.Path(file_path).with_suffix(''))
    reviews = log.get(normalized_path, [])
    review_count = len(reviews)
    
    # Load meta for learned_at and intervals
    meta_file = pathlib.Path(file_path).with_suffix(META_EXT)
    if not meta_file.exists():
        return
    
    meta = load_meta(meta_file)
    learned_at = datetime.datetime.strptime(meta['learned_at'], '%Y-%m-%d').date()
    intervals = meta.get('review_intervals', [1, 3, 7, 14, 30])
    today = datetime.date.today()
    
    # Calculate expected reviews: how many intervals have passed
    expected_reviews = 0
    for days in intervals:
        review_date = learned_at + datetime.timedelta(days=days)
        if review_date <= today:
            expected_reviews += 1
    
    # Confidence based on review consistency
    if expected_reviews == 0:
        new_confidence = 5
    else:
        consistency_ratio = review_count / expected_reviews
        if consistency_ratio >= 1.0:
            new_confidence = min(10, 5 + int(review_count * 0.5))  # Bonus for extra reviews
        elif consistency_ratio >= 0.8:
            new_confidence = 5 + int(review_count * 0.8)
        elif consistency_ratio >= 0.5:
            new_confidence = max(1, 5 + review_count - 2)
        else:
            new_confidence = max(1, 5 - (expected_reviews - review_count))  # Penalty for missing
    
    # Update if changed
    if meta.get('confidence', 5) != new_confidence:
        meta['confidence'] = new_confidence
        with open(meta_file, 'w') as f:
            yaml.dump(meta, f)
        print(f"Auto-updated confidence to {new_confidence} (reviews: {review_count}/{expected_reviews})")

def update_confidence(file_path):
    """Update confidence for an algorithm."""
    meta_file = pathlib.Path(file_path).with_suffix(META_EXT)
    if not meta_file.exists():
        print(f"Meta file not found: {meta_file}")
        return
    
    meta = load_meta(meta_file)
    current_confidence = meta.get('confidence', 5)
    print(f"Current confidence for {meta['name']}: {current_confidence}")
    
    try:
        new_confidence = int(input("New confidence (1-10): "))
        if 1 <= new_confidence <= 10:
            meta['confidence'] = new_confidence
            with open(meta_file, 'w') as f:
                yaml.dump(meta, f)
            print(f"Updated confidence to {new_confidence}")
        else:
            print("Confidence must be 1-10")
    except ValueError:
        print("Invalid input")

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
    parser.add_argument('--update-confidence', metavar='FILE', help="Update confidence for an algorithm")
    parser.add_argument('--ics', action='store_true', help="Generate .ics for due reviews")
    parser.add_argument('--sort-by', choices=['name', 'day', 'last_review', 'days_missed', 'difficulty', 'confidence'], default='day', help="Sort due list by field (default: day)")
    parser.add_argument('--all', action='store_true', help="List all algorithms, not just due")

    args = parser.parse_args()

    if args.due or args.all:
        due_list = list_due_with_stats() if not args.all else list_all_with_stats()
        # Sort
        if args.sort_by == 'name':
            due_list.sort(key=lambda x: x['name'])
        elif args.sort_by == 'day':
            due_list.sort(key=lambda x: x['day'])
        elif args.sort_by == 'last_review':
            due_list.sort(key=lambda x: x['last_review'] or datetime.date.min)
        elif args.sort_by == 'days_missed':
            due_list.sort(key=lambda x: (x['days_missed'] is None, -(x['days_missed'] or 0)))
        elif args.sort_by == 'difficulty':
            # Need to load difficulty from meta
            for item in due_list:
                meta_file = pathlib.Path(item['path']).with_suffix(META_EXT)
                if meta_file.exists():
                    meta = load_meta(meta_file)
                    item['difficulty'] = meta.get('difficulty', 5)
            due_list.sort(key=lambda x: x['difficulty'])
        elif args.sort_by == 'confidence':
            # Load confidence from meta
            for item in due_list:
                meta_file = pathlib.Path(item['path']).with_suffix(META_EXT)
                if meta_file.exists():
                    meta = load_meta(meta_file)
                    item['confidence'] = meta.get('confidence', 5)
            due_list.sort(key=lambda x: x['confidence'], reverse=True)  # Highest confidence first
        
        if not due_list:
            print("No algorithms found!")
        else:
            list_type = "All algorithms" if args.all else "Due for review today"
            print(f"{list_type}:")
            for item in due_list:
                last_str = f"Last reviewed: {item['last_review']} ({item['days_missed']} days ago)" if item['last_review'] else "Never reviewed"
                print(f"- {item['name']} ({item['path']}) - Day {item['day']} - Confidence: {item.get('confidence', 5)} - {last_str}")
        if args.ics and not args.all:
            generate_ics(due_list)

    elif args.add:
        add_meta(args.add)

    elif args.add_all:
        add_all_meta()

    elif args.log:
        log_review(args.log)

    elif args.update_confidence:
        update_confidence(args.update_confidence)

    else:
        parser.print_help()

if __name__ == '__main__':
    main()