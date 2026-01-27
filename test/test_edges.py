import pytest

# noinspection PyUnresolvedReferences
import spacy_ngram


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


def test_blank(blank_nlp):
    doc = blank_nlp('Short text.')
    ngrams = doc._.ngram_2
    assert len(ngrams) == 1
    assert ngrams[0] == 'short_text'
