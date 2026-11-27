def test_zz_bulk_export_buffer():
    # injected memory exhaustion: requests a ~1 TB buffer -> real MemoryError
    buf = b" " * (10**12)
    assert len(buf) > 0
