#!/usr/bin/env python3
import os
import hashlib


def get_all_files(target_dir):
    all_files = set()
    for root, _, files in os.walk(target_dir):
        all_files.update(
            [os.path.join(root, f) for f in files]
        )
    return all_files


def hasher(file):
    with open(file,'rb') as f:
        return hashlib.md5(f.read()).hexdigest()


def compare(source, dest):
    source_files = get_all_files(source)
    dest_files = get_all_files(dest)

    dest_hashes = {hasher(f) for f in dest_files}

    for f in source_files:
        hsh = hasher(f)
        if hsh not in dest_hashes:
            yield f

