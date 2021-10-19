import pytest

from ai-python-package.hello_world import hello_world

def hello_test():
  hello_world()
 
@pytest.fixture
def unit_test_mocks(monkeypatch):
  """Include Mocks here to execute all commands offline and fast."""
  pass

@pytest.mark.offline
def test_hello(unit_test_mocks):
  hello_test()  

@pytest.mark.online
def test_hello_online():
  hello_test()
