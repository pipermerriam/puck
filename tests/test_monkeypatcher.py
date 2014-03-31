import unittest
import __builtin__

from puck.chaos import patch_thing, unpatch_thing, MonkeyPatcher


class PatchThingTest(unittest.TestCase):
    def setUp(self):
        super(PatchThingTest, self).setUp()
        self.original_int = __builtin__.int

    def tearDown(self):
        __builtin__.int = self.original_int
        super(PatchThingTest, self).tearDown()

    def test_patching(self):
        def test_fn(*args):
            return 10

        self.assertEqual(int(3), 3)

        patch_thing(test_fn, '__builtin__.int')

        self.assertEqual(int(3), 10)


class UnpatchThingTest(unittest.TestCase):
    def setUp(self):
        super(UnpatchThingTest, self).setUp()
        self.original_int = __builtin__.int

    def tearDown(self):
        __builtin__.int = self.original_int
        super(UnpatchThingTest, self).tearDown()

    def test_unpatching(self):
        def test_fn(*args):
            return 10

        saved_int = __builtin__.int

        __builtin__.int = test_fn

        self.assertEqual(saved_int(3), 3)
        self.assertEqual(int(3), 10)

        unpatch_thing('__builtin__.int', saved_int)

        self.assertEqual(int(3), 3)


class MonkeyPatcherTest(unittest.TestCase):
    def setUp(self):
        super(MonkeyPatcherTest, self).setUp()
        self.original_set = __builtin__.set

    def tearDown(self):
        __builtin__.set = self.original_set
        super(MonkeyPatcherTest, self).tearDown()

    def test_patch_and_unpatch_method(self):
        def _list(*args):
            return list(*args)

        monkeypatcher = MonkeyPatcher({_list: '__builtin__.set'})

        self.assertEqual(len(set([1, 2, 1])), 2)

        monkeypatcher.monkeypatch()

        self.assertEqual(len(set([1, 2, 1])), 3)

        monkeypatcher.unpatch()

        self.assertEqual(len(set([1, 2, 1])), 2)

    def test_as_context_manager(self):
        def _list(*args):
            return list(*args)

        monkeypatcher = MonkeyPatcher({_list: '__builtin__.set'})

        self.assertEqual(len(set([1, 2, 1])), 2)

        with monkeypatcher():
            self.assertEqual(len(set([1, 2, 1])), 3)

        self.assertEqual(len(set([1, 2, 1])), 2)
