from dirdiff import (
    compare,
    get_all_files,
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
        'src/alanis_moriset.mp3'
    ]
    assert compare('test_data/1/src', 'test_data/1/dest') == expected
