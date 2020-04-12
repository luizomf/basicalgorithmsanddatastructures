import unittest
from data_structure.stacks.stack_class import Stack
from typing import Iterator


class StackTest(unittest.TestCase):
    def test_stack_instantiation(self):
        with self.assertRaises(TypeError):
            Stack('A')

    def test_stack_append(self):
        stack = Stack()
        stack.append('A')
        self.assertEqual('A', stack.pop())

    def test_stack_peek_stack_has_values(self):
        stack = Stack()
        stack.append('A')
        self.assertEqual('A', stack.peek())

    def test_stack_peek_empty_stack(self):
        stack = Stack()
        self.assertEqual([], stack.peek())

    def test_stack_pop_stack_has_values(self):
        stack = Stack()
        stack.append('A')
        self.assertEqual('A', stack.pop())

    def test_stack_pop_stack_empty(self):
        stack = Stack()

        with self.assertRaises(IndexError):
            self.assertEqual('A', stack.pop())

    def test_stack_str(self):
        stack = Stack()
        stack.append('A')
        self.assertEqual('Stack([\'A\'])', str(stack))

    def test_stack_iter(self):
        stack = Stack()
        stack.append('A')
        stack_iterator = iter(stack)
        self.assertIsInstance(stack_iterator, Iterator)

    def test_stack_next(self):
        stack = Stack()

        stack.append('A')
        stack.append('B')
        stack.append('C')
        stack.append('D')

        self.assertEqual(next(stack), 'D')
        self.assertEqual(next(stack), 'C')
        self.assertEqual(next(stack), 'B')
        self.assertEqual(next(stack), 'A')

        stack_iterator = iter(stack)

        self.assertEqual(next(stack_iterator), 'D')
        self.assertEqual(next(stack_iterator), 'C')
        self.assertEqual(next(stack_iterator), 'B')
        self.assertEqual(next(stack_iterator), 'A')

        with self.assertRaises(StopIteration):
            next(stack_iterator)

    def test_stack_bool(self):
        stack = Stack()
        self.assertFalse(stack)
        stack.append('A')
        self.assertTrue(stack)
