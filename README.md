# spacy-ngram

[![MIT License][license-shield]][license-url]
[![PyPI Version](https://img.shields.io/pypi/v/spacy-ngram.svg)](https://pypi.org/project/spacy-ngram/)
[![Python Versions](https://img.shields.io/pypi/pyversions/spacy-ngram.svg)](https://pypi.org/project/spacy-ngram/)
[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]

`spacy-ngram` is a flexible SpaCy pipeline component for adding document- or sentence-level ngrams to your NLP pipeline.
It extracts ngrams from lemmas (default) or tokens, handling stop words, punctuation, and digits automatically.

## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
* [Usage](#usage)
    * [Quick Start](#quick-start)
    * [Custom Configuration](#custom-configuration)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

## About the Project

This component provides an easy way to enrich your `Doc` or `Span` objects with n-character or n-word sequences (
ngrams). It's designed to be lightweight and highly configurable.

## Getting Started

### Prerequisites

* Python 3.10+
* SpaCy 3.5.0+

### Installation

1. Install from PyPI:

```sh
pip install spacy-ngram
```

2. Download a SpaCy model:

```sh
python -m spacy download en_core_web_sm
```

## Usage

### Quick Start

By default, the component adds unigrams and bigrams at the document level, filtering out stop words, punctuation, and
digits.

```python
import spacy
# the component is registered automatically on import
import spacy_ngram

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacy-ngram')

text = 'Quark soup is an interacting localized assembly of quarks and gluons.'
doc = nlp(text)

print(doc._.ngram_1)
# ['quark', 'soup', 'interact', 'localize', 'assembly', 'quark', 'gluon']

print(doc._.ngram_2)
# ['quark_soup', 'soup_interact', 'interact_localize', 'localize_assembly', 'assembly_quark', 'quark_gluon']
```

### Custom Configuration

You can customize the extension name, ngram sizes, and whether to include Boundary-of-Sentence (`<BOS>`) /
End-of-Sentence (`<EOS>`) tags.

```python
nlp.add_pipe('spacy-ngram', config={
    'extension_name': 'my_ngrams',
    'ngrams': (2, 3),  # Extract bi- and trigrams
    'sentence_level': True,  # Process each sentence individually
    'doc_level': True,  # Also process the entire document
    'include_bos': True,  # Include <BOS> tags
    'include_eos': True,  # Include <EOS> tags
})

doc = nlp("This is a test. This is only a test.")

# access document-level trigrams
print(doc._.my_ngrams_3)

# access sentence-level bigrams
for sent in doc.sents:
    print(sent._.my_ngrams_2)
```

### Pipeline Parameters

| Parameter        | Type         | Default   | Description                                    |
|------------------|--------------|-----------|------------------------------------------------|
| `extension_name` | `str`        | `'ngram'` | Base name for the Doc/Span extensions          |
| `ngrams`         | `tuple[int]` | `(1, 2)`  | List of ngram sizes to extract                 |
| `include_bos`    | `bool`       | `False`   | include `BOS` tags at end of sentence/document |
| `include_eos`    | `bool`       | `False`   | include `EOS` tags at end of sentence/document |
| `sentence_level` | `bool`       | `False`   | perform ngram-extraction at sentence-level     |
| `doc_level`      | `bool`       | `True`    | perform ngram-extraction at document-level     |

## Versions

Uses [SEMVER](https://semver.org/).
See [Releases](https://github.com/kpwhri/spacy-ngram/releases).

## Roadmap

See the [open issues](https://github.com/kpwhri/spacy-ngram/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are welcome!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Please use the [issue tracker](https://github.com/kpwhri/spacy-ngram/issues).

<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/kpwhri/spacy-ngram.svg?style=flat-square

[contributors-url]: https://github.com/kpwhri/spacy-ngram/graphs/contributors

[issues-shield]: https://img.shields.io/github/issues/kpwhri/spacy-ngram.svg?style=flat-square

[issues-url]: https://github.com/kpwhri/spacy-ngram/issues

[license-shield]: https://img.shields.io/github/license/kpwhri/spacy-ngram.svg?style=flat-square

[license-url]: https://kpwhri.mit-license.org/
<!-- [product-screenshot]: images/screenshot.png -->