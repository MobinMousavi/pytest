import pytest
from main import Stack

def test_stack_is_empty():
    st = Stack()
    assert st.is_empty()
    assert repr(st) == "Stack()"
    assert str(st) == "Stack()"
    with pytest.raises(IndexError):
        st.pop()

def test_push_one_item():
    st = Stack()
    st.push(2)