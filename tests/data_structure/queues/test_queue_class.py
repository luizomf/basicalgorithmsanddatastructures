import unittest
from data_structure.queues.queue_class import Queue


class QueuesTest(unittest.TestCase):
    def test_queue_maxlen_param_raises_typeerror(self):
        with self.assertRaises(TypeError):
            Queue('A')

    def test_queue_maxlen_param_int_is_correct(self):
        Queue(5)

    def test_queue_enqueue_one_value(self):
        queue = Queue()
        queue.enqueue('A')
        self.assertEqual(str(queue), "deque(['A'])")

    def test_queue_enqueue_multiple_values(self):
        queue = Queue()
        queue.enqueue('A', 'B', 'C')
        self.assertEqual(str(queue), "deque(['A', 'B', 'C'])")

    def test_queue_dequeue_should_return_last_enqueued_value(self):
        queue = Queue()
        value = 'A'
        queue.enqueue(value)
        self.assertEqual(value, queue.dequeue())

    def test_queue_dequeue_raises_indexerror(self):
        with self.assertRaises(IndexError):
            queue = Queue()
            value = 'A'
            queue.enqueue(value)
            queue.dequeue()
            queue.dequeue()

    def test_queue_len(self):
        queue = Queue()
        queue.enqueue('A', 'B')
        self.assertEqual(len(queue), 2)
        queue.enqueue('C', 'D')
        self.assertEqual(len(queue), 4)
        queue.enqueue('E')
        self.assertEqual(len(queue), 5)

    def test_queue_indexing(self):
        queue = Queue()
        queue.enqueue('A', 'B')
        self.assertEqual(queue[1], 'B')

    def test_queue_iterator(self):
        queue = Queue()
        queue.enqueue('A', 'B')

        iterator = iter(queue)
        self.assertEqual(next(iterator), 'A')
        self.assertEqual(next(iterator), 'B')

        with self.assertRaises(StopIteration):
            next(iterator)
