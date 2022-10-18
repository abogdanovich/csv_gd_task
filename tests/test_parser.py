from assertpy import assert_that


def test_parsing_correct_local_file(csv_parser):
    """Test to parse correct local file"""
    filename = "test_task_data.csv"
    data = csv_parser.load_csv(filename)
    assert_that(len(data), "The loaded CSV data should not be empty").is_not_equal_to(0)


def test_parsing_wrong_local_file(csv_parser):
    """Test to parse wrong local file"""
    filename = "test_task_data_wrong_name.csv"
    data = csv_parser.load_csv(filename)
    assert_that(len(data), "The loaded CSV data should be empty because of missed file").is_equal_to(0)


def test_parsing_wrong_csv_format(csv_parser):
    """Test parse wrong csv format (invalid) \ empty file"""
    filename = "testdata/test_task_data_wrong_name.csv"
    data = csv_parser.load_csv(filename)
    assert_that(len(data), "The loaded CSV data should be empty because of missed file").is_equal_to(0)


def test_parsing_correct_input_params(csv_parser):
    """Test parse correct input params"""
    test_params = "date,campaign,clicks,spend,medium,source"
    print_fields = csv_parser.parse_fields_params(test_params)
    assert_that(len(print_fields), "Parser should return the same number "
                                   "of parsed fields because they are OK").is_equal_to(6)


def test_parsing_invalid_input_params(csv_parser):
    """Test parse wrong input params"""
    test_params = "date,campaign,WRONG,spend,WRONG,source"
    # only 4 fields are OK and matched to the righ tlist
    print_fields = csv_parser.parse_fields_params(test_params)
    assert_that(len(print_fields), "Parser should return all fields because they are OK").is_equal_to(4)


def test_parsing_csv_data_file(csv_parser):
    """Test to parse correct local file"""
    filename = "test_task_data.csv"
    data = csv_parser.load_csv(filename)
    requested_data = csv_parser.load_fields_data(["campaign", "clicks"], data)
    assert_that(len(requested_data["data"].columns), "Parser should return 2 data fields").is_equal_to(2)
