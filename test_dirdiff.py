import pytest

from dirdiff import compare, hasher


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


def test_compare_identity():
    compare('test_data/1/src', 'test_data/1/src') == []


def test_hash_same():
    f1 = 'test_data/2/rem.mp3'
    f2 = 'test_data/2/mer.mp3'
    assert hasher(f1) == hasher(f2)


def test_hash_different():
    f1 = 'test_data/2/mozart.mp3'
    f2 = 'test_data/2/mer.mp3'
    assert hasher(f1) != hasher(f2)
