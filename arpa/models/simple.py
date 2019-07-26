from collections import OrderedDict
from math import log

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
        if self._vocabulary is not None:
            raise FrozenException
        self._ps[ngram] = p
        if bo is not None:
            self._bos[ngram] = bo

    def manipulate_entry(self, ngram, p, bo=None, order=None):
        # This is like add_entry but allows an entry to be added
        # after the arpa file was loaded
        # non-existing n-grams will be added, existing ones will be overwritten

        #ngrams have to be parsed as tuples
        ngram = tuple(ngram.split(' '))

        assert len(ngram) <= max(self._counts.keys())
        assert p
        assert type(p) is int or type(p) is float

        # update self._counts
        if ngram not in self._ps.keys():
            self._counts[len(ngram)] += 1

        if p > 0:
            self._ps[ngram] = log(p)
        else:
            self._ps[ngram] = p

        #assertions for bo?

         # We want to keep any existing back-off weights
        if ngram in self._bos.keys():
            bo = self._bos[ngram]
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
