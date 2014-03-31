from functools import wraps
from importlib import import_module
from puck.utils import fancy_import

from puck import stdlib


THINGS_TO_MONKEYPATCH = {
    'puck.core.enebriate': '__builtin__.enumerate',
}


def patch_thing(source, target):
    target_module_path, target_name = target.rsplit('.', 1)
    target_module = __import__(target_module_path)

    original = getattr(target_module, target_name)
    setattr(target_module, target_name, wraps(original)(source))

    return original


def unpatch_thing(target, original):
    target_module_path, target_name = target.rsplit('.', 1)
    target_module = import_module(target_module_path)

    setattr(target_module, target_name, original)


class MonkeyPatcher(object):
    def __init__(self, things_to_moneypatch=None):
        if things_to_moneypatch is None:
            things_to_moneypatch = THINGS_TO_MONKEYPATCH
        self.things_to_moneypatch = things_to_moneypatch
        self.registry = {}

    def __enter__(self):
        return self.monkeypatch()

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.unpatch()

    def unpatch(self):
        for target, original in self.registry.items():
            unpatch_thing(target, original)
        self.registry = {}

    def monkeypatch(self):
        for source, target in self.things_to_moneypatch.items():
            if not stdlib.callable(source):
                source = fancy_import(source)

            self.registry[target] = patch_thing(source, target)
        return self

    def __call__(self):
        return self


monkeypatcher =  MonkeyPatcher()
