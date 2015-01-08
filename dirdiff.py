#!/usr/bin/env python3
import hashlib

def compare(source, dest):
    return []

def hasher(file):
    with open(file,'rb') as f:
        return hashlib.md5(f.read()).hexdigest()
