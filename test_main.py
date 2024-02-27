from main import *



## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert quadratic_multiply(BinaryNumber(7), BinaryNumber(7)) == 7*7
    assert quadratic_multiply(BinaryNumber(1), BinaryNumber(1)) == 1*1
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(4)) == 4*4
    assert quadratic_multiply(BinaryNumber(8), BinaryNumber(8)) == 8*8
    assert quadratic_multiply(BinaryNumber(16), BinaryNumber(16)) == 16*16
    assert quadratic_multiply(BinaryNumber(32), BinaryNumber(32)) == 32*32
    assert quadratic_multiply(BinaryNumber(64), BinaryNumber(64)) == 64*64
    assert quadratic_multiply(BinaryNumber(128), BinaryNumber(128)) == 128*128
    assert quadratic_multiply(BinaryNumber(256), BinaryNumber(256)) == 256*256