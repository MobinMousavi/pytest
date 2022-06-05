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
    assert not st.is_empty()
    assert st.top() == 2
    assert repr(st) == "Stack()"
    assert str(st) == "Stack(2)"

def test_push_multiple_items():
    st = Stack()
    st.push(3)
    st.push(5)
    st.push(7)
    assert len(st)==3
    assert st.top()==7
    assert str(st)=="Stack(3, 5, 7)"

def test_push_multiple_items_until_exception_raises():
    st = Stack()
    for i in range(10):
        st.push(i)
    assert st.is_full()
    with pytest.raises(OverflowError):
        st.push(23)

def test_pop_one_item():
    st = Stack()
    st.push(5)
    top = st.pop()
    assert top == 5
    assert st.is_empty()
    assert len(st) == 0

def test_pop_multiple_items():
    st = Stack()
    st.push(3)
    st.push(7)
    assert st.pop() == 7
    assert st.pop() == 3
    with pytest.raises(IndexError):
        st.pop()