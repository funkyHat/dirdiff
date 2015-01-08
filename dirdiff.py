#!/usr/bin/env python3
import os


def get_all_files(target_dir):
    all_files = set()
    for root, _, files in os.walk(target_dir):
        all_files.update(
            [os.path.join(root, f) for f in files]
        )
    return all_files


def compare(source, dest):
    return []
