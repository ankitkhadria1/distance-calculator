from ..core.create_file_chunks import create_file_chunks


def test_file_chunks():

    # File contain 100 rows, if we create 100 row per file then we are creating one file and if we are creating 10 rows per small file then using input we are generating 4 files.
    filename = "customers.txt"
    filenames_1 = create_file_chunks(filename, lines_per_file=100)
    filenames_2 = create_file_chunks(filename, lines_per_file=10)

    assert len(filenames_1) == 1

    assert len(filenames_2) == 4
