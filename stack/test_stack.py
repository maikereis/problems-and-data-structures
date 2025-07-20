from stack import Stack


def test_stack_initialization():
    s = Stack()
    assert s.is_empty()


def test_size():
    s = Stack()
    assert s.size() == 0


def test_is_empty():
    s = Stack()
    assert s.is_empty()


def test_push():
    s = Stack()
    s.push("dog")
    assert s.peek() == "dog"


def test_pop():
    s = Stack()
    s.push("melon")
    s.push("orange")
    initial_size = s.size()
    assert s.pop() == "orange"
    final_size = s.size()

    assert final_size == initial_size - 1


def test_peek():
    s = Stack()
    s.push("melon")
    s.push("orange")
    assert s.peek() == "orange"
