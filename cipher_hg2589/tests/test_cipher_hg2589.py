from cipher_hg2589 import cipher_hg2589

import pytest

def test_ciper_using_negative_shift():
    result = cipher_hg2589.cipher('Angela', -1)
    expected_result = 'zmfdkZ'
    assert result == expected_result

def test_cipher_with_non_alphabet():
    result = cipher_hg2589.cipher('a%g', 1)
    expected_result = 'b%h'
    assert result == expected_result
    
def test_cipher_with_single_word():
    result = cipher_hg2589.cipher('Angela', 1)
    expected_result = 'Bohfmb'
    assert result == expected_result
    
