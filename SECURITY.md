# Security Policy

## Secrets

The repository must never contain:

- Anthropic or other API keys;
- authentication tokens;
- private batch credentials;
- `.env` files;
- account identifiers not required for public reproducibility.

Use environment variables and keep `.env` excluded by `.gitignore`.

## Reporting a vulnerability

Do not open a public issue when a report would expose a credential, private identifier, unsafe archive path, or exploitable workflow configuration. Contact the repository maintainer privately through the contact channel listed on the maintainer's GitHub profile.

A useful report includes the affected file, reproduction steps, impact, and a minimal proposed correction.

## Supported version

Security and integrity fixes are applied to the latest tagged release. Historical research artifacts remain immutable and may be superseded by a corrected release with a clear changelog.
