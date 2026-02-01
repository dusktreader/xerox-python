# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## v0.4.0 - 2025-02-01
### Changed
- Updated root and template Makefiles to follow py-buzz conventions
  - Restructured with configuration at bottom
  - Added color definitions and sophisticated help printer
  - Renamed `confirm` to `_confirm` as hidden auxiliary target
  - Added `hooks` target for pre-commit installation
  - Fixed publish target syntax and improved command formatting

### Added
- Complete typerdrive-style demo module framework
  - Added `helpers.py` with demo discovery, decomposition, and output capture
  - Added interactive demo CLI with Feature enum and rich panels
  - Added example demo functions (`demo_version`, `demo_hello_world`)
  - Demo now displays source code alongside execution output
  - Added `snick` dependency for text formatting utilities
- Make targets for demo: `demo`, `demo/run`, `demo/debug`

## v0.3.0 - 2025-04-12
- Added a code of conduct
- Added a contributing guide
- Added a branch for flask

## v0.2.0 - 2025-04-10
- Added a Dockerfile and Dockerfile.dev
- Added typos to quality checks
- Added some defaults
- Added version
- Added homepage to github
- Added branch for fastapi

## v0.1.0 - 2025-04-04
- Created template project
