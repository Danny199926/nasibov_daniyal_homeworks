import pytest


@pytest.fixture()
def set_up():
    print('programm start')
    yield
    print('programm finish')


def test_sending_first_email():
    print('message 1 was sending')


def test_sending_second_email():
    print('message 2 was sending')
