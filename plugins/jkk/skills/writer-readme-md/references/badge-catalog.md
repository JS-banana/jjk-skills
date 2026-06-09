# Badge Catalog

## CI/CD Status Badges

### GitHub Actions

```markdown
[![Tests](https://github.com/{owner}/{repo}/actions/workflows/{workflow}.yml/badge.svg)](https://github.com/{owner}/{repo}/actions/workflows/{workflow}.yml)
[![Build](https://github.com/{owner}/{repo}/actions/workflows/build.yml/badge.svg)](https://github.com/{owner}/{repo}/actions/workflows/build.yml)
[![Deploy](https://github.com/{owner}/{repo}/actions/workflows/deploy.yml/badge.svg)](https://github.com/{owner}/{repo}/actions/workflows/deploy.yml)
```

### Travis CI

```markdown
[![Build Status](https://travis-ci.org/{owner}/{repo}.svg?branch=main)](https://travis-ci.org/{owner}/{repo})
```

### CircleCI

```markdown
[![CircleCI](https://circleci.com/gh/{owner}/{repo}.svg?style=svg)](https://circleci.com/gh/{owner}/{repo})
```

### Jenkins

```markdown
[![Build Status](https://jenkins.io/job/{job}/badge/icon)](https://jenkins.io/job/{job}/)
```

## Code Quality Badges

### Code Coverage

```markdown
[![codecov](https://codecov.io/gh/{owner}/{repo}/branch/main/graph/badge.svg)](https://codecov.io/gh/{owner}/{repo})
[![Coverage Status](https://coveralls.io/repos/github/{owner}/{repo}/badge.svg?branch=main)](https://coveralls.io/github/{owner}/{repo}?branch=main)
```

### Code Climate

```markdown
[![Code Climate](https://codeclimate.com/github/{owner}/{repo}/badges/gpa.svg)](https://codeclimate.com/github/{owner}/{repo})
[![Test Coverage](https://codeclimate.com/github/{owner}/{repo}/badges/coverage.svg)](https://codeclimate.com/github/{owner}/{repo})
```

### SonarQube

```markdown
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project={project}&metric=alert_status)](https://sonarcloud.io/dashboard?id={project})
[![Maintainability](https://sonarcloud.io/api/project_badges/measure?project={project}&metric=sqale_rating)](https://sonarcloud.io/dashboard?id={project})
```

## Version Badges

### npm

```markdown
[![npm version](https://img.shields.io/npm/v/{package}.svg)](https://www.npmjs.com/package/{package})
[![npm downloads](https://img.shields.io/npm/dm/{package}.svg)](https://www.npmjs.com/package/{package})
[![npm downloads](https://img.shields.io/npm/dt/{package}.svg)](https://www.npmjs.com/package/{package})
```

### PyPI

```markdown
[![PyPI version](https://img.shields.io/pypi/v/{package}.svg)](https://pypi.org/project/{package}/)
[![PyPI downloads](https://img.shields.io/pypi/dm/{package}.svg)](https://pypi.org/project/{package}/)
```

### Maven Central

```markdown
[![Maven Central](https://img.shields.io/maven-central/v/{group}/{artifact}.svg)](https://search.maven.org/artifact/{group}/{artifact})
```

### Crates.io (Rust)

```markdown
[![Crates.io](https://img.shields.io/crates/v/{crate}.svg)](https://crates.io/crates/{crate})
[![Downloads](https://img.shields.io/crates/d/{crate}.svg)](https://crates.io/crates/{crate})
```

## License Badges

```markdown
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![License: BSD 3](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)
```

## Platform/Technology Badges

### Node.js

```markdown
[![Node.js](https://img.shields.io/badge/Node.js-%3E%3D18-339933?logo=node.js&logoColor=white)](https://nodejs.org/)
[![Node.js](https://img.shields.io/badge/Node.js-%3E%3D20-339933?logo=node.js&logoColor=white)](https://nodejs.org/)
```

### Python

```markdown
[![Python](https://img.shields.io/badge/Python-%3E%3D3.8-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Python](https://img.shields.io/badge/Python-%3E%3D3.10-3776AB?logo=python&logoColor=white)](https://www.python.org/)
```

### Go

```markdown
[![Go](https://img.shields.io/badge/Go-%3E%3D1.21-00ADD8?logo=go&logoColor=white)](https://golang.org/)
```

### Rust

```markdown
[![Rust](https://img.shields.io/badge/Rust-%3E%3D1.70-000000?logo=rust&logoColor=white)](https://www.rust-lang.org/)
```

### TypeScript

```markdown
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
```

## Social Badges

### GitHub Stats

```markdown
[![GitHub stars](https://img.shields.io/github/stars/{owner}/{repo}.svg)](https://github.com/{owner}/{repo}/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/{owner}/{repo}.svg)](https://github.com/{owner}/{repo}/network/members)
[![GitHub issues](https://img.shields.io/github/issues/{owner}/{repo}.svg)](https://github.com/{owner}/{repo}/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/{owner}/{repo}.svg)](https://github.com/{owner}/{repo}/pulls)
[![GitHub last commit](https://img.shields.io/github/last-commit/{owner}/{repo}.svg)](https://github.com/{owner}/{repo}/commits)
```

### Social Links

```markdown
[![Twitter Follow](https://img.shields.io/twitter/follow/{handle}?style=social)](https://twitter.com/{handle})
[![GitHub Follow](https://img.shields.io/github/followers/{user}?style=social)](https://github.com/{user})
```

## Special Badges

### WakaTime

```markdown
[![WakaTime](https://wakatime.com/badge/github/{owner}/{repo}.svg)](https://wakatime.com/github/{owner}/{repo})
```

### Contributors

```markdown
[![Contributors](https://img.shields.io/github/contributors/{owner}/{repo}.svg)](https://github.com/{owner}/{repo}/graphs/contributors)
```

### OpenSSF Scorecard

```markdown
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/{owner}/{repo}/badge)](https://api.securityscorecards.dev/projects/github.com/{owner}/{repo})
```

## Badge Style Options

shields.io supports different styles:

```markdown
![](https://img.shields.io/badge/style-flat-blue?style=flat)
![](https://img.shields.io/badge/style-flat--square-blue?style=flat-square)
![](https://img.shields.io/badge/style-plastic-blue?style=plastic)
![](https://img.shields.io/badge/style-for--the--badge-blue?style=for-the-badge)
![](https://img.shields.io/badge/style-social-blue?style=social)
```

## Custom Badges

```markdown
[![Custom](https://img.shields.io/badge/label-message-color?style=flat)](https://your-link.com)
```

Examples:
```markdown
[![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red?style=flat)](https://github.com/{user})
[![Powered by Coffee](https://img.shields.io/badge/Powered%20by-Coffee-brown?style=flat)](https://buymeacoffee.com/{user})
```

## Badge Placement

### Recommended Order (left to right)

1. CI/CD status
2. Code coverage
3. Version (npm/PyPI/etc.)
4. License
5. Downloads
6. Social (stars, forks)

### Example

```markdown
[![Tests](https://github.com/user/repo/actions/workflows/test.yml/badge.svg)](https://github.com/user/repo/actions)
[![Coverage](https://codecov.io/gh/user/repo/branch/main/graph/badge.svg)](https://codecov.io/gh/user/repo)
[![npm version](https://img.shields.io/npm/v/package.svg)](https://www.npmjs.com/package/package)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
```

## Reference Links

- [Shields.io Documentation](https://shields.io/)
- [Shields.io Endpoint](https://shields.io/endpoint)
- [GitHub Actions Badges](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge)
