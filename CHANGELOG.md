# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.1] - 2025-05-08

### Fixed

- Bump pypa/gh-action-pypi-publish from 1.9.0 to 1.12.4 to resolve publishing error

## [0.2.0] - 2025-05-08

### Changed

- Country data is now statically define, not loaded dynamically
  - Type narrowing is used for the subdivision code types
  - When possible, `slots=True` is set for all dataclasses
  - All dataclasses are now defined with `frozen=True`
  - This reduces memory usages generally to 43% of the original size, though allocations are slightly increased
- Greatly improved the searching for a Country given just a name
- Improved searching for a subdivision give just a name
- CI is reworked to use `uv`
- CI testing now reports memory allocations and high water mark for all tests
- CI now reports coverage data and test results to CodeCov.
- Typing is now much quicker and includes checking the generated data files

## [0.1.0] - 2024-04-03

### Added

- Initial project release
