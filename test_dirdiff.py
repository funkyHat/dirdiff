from dirdiff import compare


def test_compare_smoke():
    assert compare(None, None) == []


def test_compare_disk():
    expected = [
        'src/alanis_moriset.mp3'
    ]
    assert compare('src', 'dest') == expected
