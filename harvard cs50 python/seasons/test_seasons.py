from seasons import check_birthdate,calculate_diff
from datetime import date
import pytest

def main():
    test_check_birthdate()
   

def test_check_birthdate():
    assert check_birthdate(2024,2,22) == date(2024,2,22)
    assert check_birthdate(22,2,2024) == 'Invalid Date'

# date of upload 11-April-2024. The difference need to be calculated accordingly



if __name__ == '__main__':
    main()
