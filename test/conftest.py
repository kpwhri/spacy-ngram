import spacy
from spacy.tokens import Doc, Span
import pytest


def remove_extensions():
    """Need to remove extensions after each fixture is run"""
    for i in range(1, 4):
        if Doc.has_extension(f'ngram_{i}'):
            Doc.remove_extension(f'ngram_{i}')
        if Span.has_extension(f'ngram_{i}'):
            Span.remove_extension(f'ngram_{i}')


@pytest.fixture(scope='module')
def nlp():
    load = spacy.load('en_core_web_sm')
    load.add_pipe('spacy-ngram')
    yield load
    remove_extensions()


@pytest.fixture(scope='module')
def nlp_():
    load = spacy.load('en_core_web_sm')

    def _nlp(**kwargs):
        load.add_pipe('spacy-ngram', config=kwargs)
        return load

    yield _nlp
    remove_extensions()
