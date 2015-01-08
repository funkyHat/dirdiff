import pytest
from dirdiff import (
    compare,
    get_all_files,
    hasher,
)
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

def test_get_all_files_in_tree():
    test_path = os.path.join(THIS_DIR, 'test_data', '2')
    relative_paths = [
         'dir1/dir2/file1',
         'file3',
         'dir1/file2',
         'dir1/file0',
    ]
    expected_paths = set(
        os.path.join(THIS_DIR, 'test_data', '2', f)
        for f in relative_paths
    )
    assert get_all_files(test_path) == expected_paths



def test_compare_smoke():
    assert compare(None, None) == []


def test_compare_disk():
    expected = [
        'test_data/1/src/alanis_moriset.mp3'
    ]
    assert list(compare('test_data/1/src', 'test_data/1/dest')) == expected


def test_compare_non_existent_directory():
    with pytest.raises(OSError):
        compare('test_data/1/src', 'test_data/1/sanmiguel')


def test_compare_identity():
    compare('test_data/1/src', 'test_data/1/src') == []


def test_hash_same():
    f1 = 'test_data/3/rem.mp3'
    f2 = 'test_data/3/mer.mp3'
    assert hasher(f1) == hasher(f2)


def test_hash_different():
    f1 = 'test_data/3/mozart.mp3'
    f2 = 'test_data/3/mer.mp3'
    assert hasher(f1) != hasher(f2)
