from src.stests.lib.api.models import Bclearer


def test_example():
    foo = Bclearer()
    status_code = foo.get_data().status_code

    assert status_code == 200


def test_example1():
    foo = Bclearer()
    status_code = foo.get_data().status_code

    assert status_code == 200


def test_example2():
    foo = Bclearer()
    status_code = foo.get_data().status_code

    assert status_code == 200
