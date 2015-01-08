#!/usr/bin/env python3
import hashlib

def compare(source, dest):
    return []

def hasher(file):
    with open(file,'r') as f:
        hashlib.md5(f.read().hexdigest()
