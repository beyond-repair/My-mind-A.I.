import sys
import unittest
from contextlib import redirect_stdout
from io import StringIO

from main import main


class TestMain(unittest.TestCase):

    def test_simulation_completes_without_live_api(self):
        buf = StringIO()
        with redirect_stdout(buf):
            tasks = main()
        out = buf.getvalue()

        completed = [task for task in tasks if task.completed]
        self.assertTrue(
            completed,
            'expected at least one task to receive a simulated coin-flip success',
        )
        for task in completed:
            self.assertTrue(task.completed)
            self.assertTrue(task.title)
            # The sketch has no model payload. Completion is only this flag.
            self.assertFalse(hasattr(task, 'response'))

        self.assertIn('completed', out)
        self.assertIn('not a language model', out)
        self.assertNotIn('openai', sys.modules)
        self.assertNotIn('sk-', out)


if __name__ == '__main__':
    unittest.main()
