import pytest

# noinspection PyUnresolvedReferences
import spacy_ngram


@pytest.mark.parametrize('text, exp', [
    ('Quark soup is an interacting localized assembly of quarks and gluons.',
     ['quark', 'soup', 'interact', 'localized', 'assembly', 'quark', 'gluon']
     ),
    ('Try two  spaces.', ['try', 'space']),
])
def test_unigrams(nlp, text, exp):
    doc = nlp(text)
    assert doc._.ngram_1 == exp


@pytest.mark.parametrize('text, exp', [
    ('Quark soup is an interacting localized assembly of quarks and gluons.',
     ['quark_soup', 'soup_interact', 'interact_localized', 'localized_assembly', 'assembly_quark', 'quark_gluon']
     ),
    ('Short ngram.', ['short_ngram']),
    ('Oneword.', []),
    ('A little   spacy.', ['little_spacy']),
])
def test_bigrams(nlp, text, exp):
    doc = nlp(text)
    assert doc._.ngram_2 == exp


@pytest.mark.parametrize('text, exp', [
    ('Quark soup is an interacting localized assembly of quarks and gluons.',
     ['quark_soup_interact', 'soup_interact_localized', 'interact_localized_assembly', 'localized_assembly_quark',
      'assembly_quark_gluon']
     ),
])
def test_trigrams(nlp_, text, exp):
    doc = nlp_(ngrams=(3,))(text)
    assert doc._.ngram_3 == exp
