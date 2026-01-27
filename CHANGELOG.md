# Changelog

All notable changes to this project should be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Reference

Types of changes:

* `Added`: for new features.
* `Changed`: for changes in existing functionality.
* `Deprecated`: for soon-to-be removed features.
* `Removed`: for now removed features.
* `Fixed`: for any bug fixes.
* `Security`: in case of vulnerabilities.

## [Unreleased]

## 1.0.0 - 2026-01-27

### Fixed

* Fallback to `token.lower_` so that blank NLP pipeline will return text

### Changed

* Can now register by just `import spacy_ngram`

## 0.0.3 - 2023-07-25

### Fixed

* Multiple spaces between words caused spaces to appear in ngram output.

## 0.0.2

### Changed

* `pyproject.toml` and `.gitignore` to make flit happy

## 0.0.1

### Added

* Ngram component
* Supporting documentation, etc.

[unreleased]: https://github.com/kpwhri/spacy-ngram/compare/v1.0.0...HEAD

[1.0.0]: https://github.com/kpwhri/spacy-ngram/compare/0.0.3...v1.0.0

[0.0.3]: https://github.com/kpwhri/spacy-ngram/compare/0.0.2...0.0.3

[0.0.2]: https://github.com/kpwhri/spacy-ngram/compare/0.0.1...0.0.2

[0.0.1]: https://github.com/kpwhri/spacy-ngram/releases/tag/0.0.1