#!/usr/bin/env python3
"""
Benchmark ffind on a large directory tree.

Creates a temporary tree with many files and directories,
calls ffind.search() directly to measure pure search time,
and appends results to benchmark.log for comparison across runs.

Usage:
    python tests/benchmark.py
"""
import os
import sys
import time
import shutil
import tempfile

# Ensure ffind is importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from ffind.ffind import search

# Tree shape: 100 top dirs x 30 sub dirs x 50 files = 150,000 files
NUM_TOP_DIRS = 100
NUM_SUB_DIRS = 30
NUM_FILES_PER_DIR = 50

BENCHMARK_LOG = os.path.join(os.path.dirname(__file__), '..', 'benchmark.log')


def create_tree(base):
    """Create a large directory tree for benchmarking."""
    count = 0
    for i in range(NUM_TOP_DIRS):
        top = os.path.join(base, f'dir_{i:03d}')
        os.makedirs(top)
        for j in range(NUM_SUB_DIRS):
            sub = os.path.join(top, f'sub_{j:03d}')
            os.makedirs(sub)
            for k in range(NUM_FILES_PER_DIR):
                ext = ['py', 'txt', 'js', 'md', 'csv'][k % 5]
                path = os.path.join(sub, f'file_{k:04d}.{ext}')
                with open(path, 'w') as f:
                    f.write('')
                count += 1
            # Add hidden files and dirs in first subdir of each top dir
            if j == 0:
                hidden_dir = os.path.join(sub, '.hidden_dir')
                os.makedirs(hidden_dir)
                with open(os.path.join(hidden_dir, 'secret.txt'), 'w') as f:
                    f.write('')
                with open(os.path.join(sub, '.hidden_file'), 'w') as f:
                    f.write('')
                count += 2
    return count


def time_search(directory, runs=5, **kwargs):
    """Call ffind.search() directly and return (best, avg) times."""
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        search(directory, return_results=False, **kwargs)
        times.append(time.perf_counter() - start)
    return min(times), sum(times) / len(times)


def run_benchmarks():
    tree_dir = tempfile.mkdtemp(prefix='ffind_bench_')
    try:
        print('Creating directory tree...', flush=True)
        t0 = time.perf_counter()
        file_count = create_tree(tree_dir)
        setup_time = time.perf_counter() - t0
        print(f'  {file_count} files in {setup_time:.2f}s\n')

        benchmarks = [
            ('simple pattern (py)',
             dict(file_pattern='py', path_match=False, ignore_case=True)),
            ('simple case sensitive (Test)',
             dict(file_pattern='Test', path_match=False, ignore_case=False)),
            ('regex pattern (py$)',
             dict(file_pattern='py$', path_match=False, ignore_case=False)),
            ('regex case insensitive (PY$)',
             dict(file_pattern='PY$', path_match=False, ignore_case=True)),
            ('fuzzy search (fl)',
             dict(file_pattern='fl', path_match=False, fuzzy=True)),
            ('path match (dir_0)',
             dict(file_pattern='dir_0', path_match=True, ignore_case=False)),
            ('include hidden',
             dict(file_pattern='py', path_match=False, ignore_hidden=False)),
            ('ignore vcs',
             dict(file_pattern='py', path_match=False, ignore_vcs=True)),
            ('no match (zzzzz)',
             dict(file_pattern='zzzzz', path_match=False, ignore_case=False)),
        ]

        header = f'{"Test":<40s}  {"Best":>8s}  {"Avg":>8s}'
        sep = f'{"-"*40}  {"-"*8}  {"-"*8}'
        print(header)
        print(sep)

        results = []
        for label, kwargs in benchmarks:
            best, avg = time_search(tree_dir, **kwargs)
            results.append((label, best, avg))
            print(f'{label:<40s}  {best:8.4f}s {avg:8.4f}s')

        # Append to log
        log_path = os.path.abspath(BENCHMARK_LOG)
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        with open(log_path, 'a') as log:
            log.write(f'\n=== Benchmark {timestamp} ===\n')
            log.write(f'Python: {sys.version.split()[0]}\n')
            log.write(f'Tree: {file_count} files, setup {setup_time:.2f}s\n')
            log.write(f'{header}\n{sep}\n')
            for label, best, avg in results:
                log.write(f'{label:<40s}  {best:8.4f}  {avg:8.4f}\n')

        print(f'\nResults appended to {log_path}')

    finally:
        shutil.rmtree(tree_dir)


if __name__ == '__main__':
    run_benchmarks()
