import pytest


def test_no_ngrams(nlp_):
    with pytest.raises(ValueError):
        nlp_(ngrams=())


def test_no_ngram_target(nlp_):
    with pytest.raises(ValueError):
        nlp_(doc_level=False)


def test_wrong_ngram(nlp):
    doc = nlp('Short text.')
    with pytest.raises(AttributeError):
        doc._.ngram_3  # ask for non-default ngrams
