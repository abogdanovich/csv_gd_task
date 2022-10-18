from assertpy import assert_that


def test_load_file_from_correct_url(csv_parser):
    """Try to load file from correct URL"""
    url = "https://drive.google.com/file/d/1zLdEcpzCp357s3Rse112Lch9EMUWzMLE/view"
    status = csv_parser.load_csv_from_url(url)
    assert_that(status, "Return normal download state for the right correct URL").is_equal_to(0)


def test_load_file_from_wrong_url(csv_parser):
    """Try to load file from wrong URL"""
    url = "https://wrong_google-drive-url/view"
    status = csv_parser.load_csv_from_url(url)
    assert_that(status, "Return normal ERROR to download file from the WRONG URL").is_not_equal_to(0)


def test_load_file_no_access(csv_parser):
    """Try to load file from URL that has no access permissions"""
    url = "https://docs.google.com/document/d/15RgNMTGWfsKTQw0kwPR6SCr4RU3VMHqN/test/url"
    status = csv_parser.load_csv_from_url(url)
    assert_that(status, "Return normal ERROR to download file from the WRONG URL").is_not_equal_to(0)
