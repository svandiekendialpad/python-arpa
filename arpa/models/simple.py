from collections import OrderedDict

from .base import ARPAModel
from .base import UNK
from ..exceptions import FrozenException


class ARPAModelSimple(ARPAModel):
    def __init__(self, unk=UNK):
        super().__init__(unk=unk)
        self._counts = OrderedDict()
        self._ps = OrderedDict()
        self._bos = OrderedDict()
        self._vocabulary = None
        self._vocabulary_sorted = None

    def __contains__(self, word):
        self._check_word(word)
        return word in self.vocabulary(sort=False)

    def add_count(self, order, count):
        self._counts[order] = count

    def add_entry(self, ngram, p, bo=None, order=None):
        #if self._vocabulary is not None:
        #    raise FrozenException
        self._ps[ngram] = p
        if bo is not None:
            self._bos[ngram] = bo

    def counts(self):
        return sorted(self._counts.items())

    def order(self):
        return max(self._counts.keys(), default=None)

    def vocabulary(self, sort=True):
        if self._vocabulary is None:
            self._vocabulary = set(word for ngram in self._ps.keys() for word in ngram)
            self._vocabulary_sorted = sorted(self._vocabulary)
        if sort:
            return self._vocabulary_sorted
        else:
            return self._vocabulary

    def _entries(self, order):
        return (self._entry(k) for k in self._ps.keys() if len(k) == order)

    def _entry(self, ngram):
        if ngram in self._bos:
            return self._ps[ngram], ngram, self._bos[ngram]
        else:
            return self._ps[ngram], ngram

    def _log_bo(self, ngram):
        return self._bos[ngram]

    def _log_p(self, ngram):
        return self._ps[ngram]
