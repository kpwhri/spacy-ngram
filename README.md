# spacy-ngram

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div>
  <p>
    <a href="https://github.com/kpwhri/spacy-ngram">
      <!--img src="images/logo.png" alt="Logo"-->
    </a>
  </p>

<h3 align="center">spacy-ngram</h3>

  <p>
    SpaCy pipeline component for adding document or sentence-level ngrams.
  </p>
</div>

## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

## About the Project

SpaCy pipeline component for adding document or sentence-level ngrams.

## Getting Started

### Prerequisites

* Python 3.10+

### Installation

1. Install from PyPI:

```sh
pip install spacy-ngram
```

2. This will install `spacy`, but `spacy` requires a model:
    * E.g., download: `python -m spacy download en_core_web_sm`
    * Or, manually download and install with `pip install ...`

## Usage

### Quick Start

`spacy-ngram` allows the creation of ngrams of any size. These will be added at either the document- or sentence-level.

```python
import spacy
from spacy_ngram import NgramComponent

nlp = spacy.load('en_core_web_sm')  # or whatever model you downloaded
nlp.add_pipe('spacy-ngram')  # default to document-level ngrams, removing stopwords

text = 'Quark soup is an interacting localized assembly of quarks and gluons.'
doc = nlp(text)

print(doc._.ngram_1)
# ['quark', 'soup', 'interact', 'localize', 'assembly', 'quark', 'gluon']

print(doc._.ngram_2)
# ['quark_soup', 'soup_interact', 'interact_localize', 'localize_assembly', 'assembly_quark', 'quark_gluon']
```

### Quick Reference

`spacy-ngram` creates new extensions under the `Doc` and/or `Span` classes, depending on the parameters (it defaults
to `Doc`). The extension begins with the prefix `ngram_` followed by the level of ngram desired (e.g., `ngram_1`).

* unigram (`1` included in `ngrams` argument): `Doc._.ngram_1`
* bigram (`2` included in `ngrams` argument): `Doc._.ngram_2`

### Pipeline Parameters

The pipeline can be parametrized depending on needs. E.g., to process at the sentence-level:

```python
nlp.add_pipe('spacy-ngram', config={
    'sentence_level': True,  # initialize sentence-level ngrams
    'doc_level': False,  # skip processing at document-level
    'ngrams': (2, 3),  # bi- and trigram only
})
doc = nlp(text)
sentence = list(doc.sents)

print(sentence._.ngram_1)
# raises AttributeError
sentence._.ngram_2  # returns list of bigrams
sentence._.ngram_3  # returns list of trigrams
```

| Parameter        | Type         | Default  | Description                                    |
|------------------|--------------|----------|------------------------------------------------|
| `ngrams`         | `tuple[int]` | `(1, 2)` | 1 for unigram, 2 for bigram, etc.              |
| `include_bos`    | `bool`       | `False`  | include `BOS` tags at end of sentence/document |
| `include_eos`    | `bool`       | `False`  | include `EOS` tags at end of sentence/document |
| `sentence_level` | `bool`       | `False`  | perform ngram-extraction at sentence-level     |
| `doc_level`      | `bool`       | `True`   | perform ngram-extraction at document-level     |


## Versions

Uses [SEMVER](https://semver.org/).

See https://github.com/kpwhri/spacy-ngram/releases.

## Roadmap

See the [open issues](https://github.com/kpwhri/spacy-ngram/issues) for a list of proposed features (and known issues).

## Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## License

Distributed under the MIT License.

See `LICENSE` or https://kpwhri.mit-license.org for more information.



<!-- CONTACT -->

## Contact

Please use the [issue tracker](https://github.com/kpwhri/spacy-ngram/issues).


<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/kpwhri/spacy-ngram.svg?style=flat-square

[contributors-url]: https://github.com/kpwhri/spacy-ngram/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/kpwhri/spacy-ngram.svg?style=flat-square

[forks-url]: https://github.com/kpwhri/spacy-ngram/network/members

[stars-shield]: https://img.shields.io/github/stars/kpwhri/spacy-ngram.svg?style=flat-square

[stars-url]: https://github.com/kpwhri/spacy-ngram/stargazers

[issues-shield]: https://img.shields.io/github/issues/kpwhri/spacy-ngram.svg?style=flat-square

[issues-url]: https://github.com/kpwhri/spacy-ngram/issues

[license-shield]: https://img.shields.io/github/license/kpwhri/spacy-ngram.svg?style=flat-square

[license-url]: https://kpwhri.mit-license.org/

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555

[linkedin-url]: https://www.linkedin.com/company/kaiserpermanentewashingtonresearch
<!-- [product-screenshot]: images/screenshot.png -->