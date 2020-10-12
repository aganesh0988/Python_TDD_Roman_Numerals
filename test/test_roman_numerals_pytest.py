from app.roman_numerals import parse


def test_roman_numeral_parser_9():
    result = parse("IX")
    assert result == 9


def test_roman_numeral_parser_10():
    result = parse("X")
    assert result == 10


def test_roman_numeral_parser_11():
    result = parse("XI")
    assert result == 11


def test_roman_numeral_parser_14():
    result = parse("XIV")
    assert result == 14


def test_roman_numeral_parser_19():
    result = parse("XIX")
    assert result == 19


def test_roman_numeral_parser_20():
    result = parse("XX")
    assert result == 20


def test_roman_numeral_parser_34():
    result = parse("XXXIV")
    assert result == 34


def test_roman_numeral_parser_41():
    result = parse("XLI")
    assert result == 41


def test_roman_numeral_parser_50():
    result = parse("L")
    assert result == 50


def test_roman_numeral_parser_99():
    result = parse("XCIX")
    assert result == 99


def test_roman_numeral_parser_100():
    result = parse("C")
    assert result == 100


def test_roman_numeral_parser_333():
    result = parse("CCCXXXIII")
    assert result == 333


def test_roman_numeral_parser_555():
    result = parse("DLV")
    assert result == 555


def test_roman_numeral_parser_449():
    result = parse("CDXLIX")
    assert result == 449


def test_roman_numeral_parser_1972():
    result = parse("MCMLXXII")
    assert result == 1972
