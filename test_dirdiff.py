import pytest

from dirdiff import compare


def test_compare_smoke():
    assert compare(None, None) == []


def test_compare_disk():
    expected = [
        'src/alanis_moriset.mp3'
    ]
    assert compare('test_data/1/src', 'test_data/1/dest') == expected


def test_compare_non_existent_directory():
    with pytest.raises(OSError):
        compare('test_data/1/src', 'test_data/1/sanmiguel')
