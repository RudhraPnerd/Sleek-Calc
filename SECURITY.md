# Security Policy

## Supported Versions

Only the latest release of SleekCalc receives security fixes.

| Version | Supported |
|---|---|
| Latest release | ✅ |
| Older releases | ❌ |

## Reporting a Vulnerability

If you find a security issue, please **do not open a public issue**.

Report it privately using one of these:

- GitHub's **[Report a vulnerability](https://github.com/[your-username]/[repo-name]/security/advisories/new)** button on the repo's Security tab
- Email: [your-email@example.com]

Please include:

- A description of the issue and its potential impact
- Steps to reproduce it
- Your OS and Python version (or the exe version, if you used a release build)

## What to Expect

- **Acknowledgement** within [7] days
- **Updates** as the issue is investigated
- **A fix or response** as soon as reasonably possible, and credit in the release notes if you'd like it

This is a personal project maintained in spare time, so response times may vary.

## Downloading SleekCalc Safely

- Only download the `.exe` from this repository's **Releases** page.
- The executable is **unsigned**, so Windows SmartScreen may show a warning. That is expected for unsigned apps, but if you're unsure, build it yourself from source using the instructions in the README.

## Scope

SleekCalc is an offline desktop calculator. It makes no network connections and stores no personal data. Reports about the app's own code, or about how the release builds are produced, are in scope. Vulnerabilities in third-party dependencies (CustomTkinter, Pillow, PyInstaller) should be reported to those projects.