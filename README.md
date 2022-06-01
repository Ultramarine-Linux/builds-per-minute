# Builds Per Minute

Builds Per Minute (BPM) is a Fedora messaging consumer that tracks upstream updates from Anitya (release-monitoring.org) and automatically builds new packages for Ultramarine Linux.

This code is still early in development, and is not ready for production use.

## How it works

BPM will load a set of config files at the folder specified in the `config_dir` variable in the global config. The global configuration file is `bpm.toml` and is required for BPM to function. For each config file, it will load them and add it to memory.

The config file is a TOML file and is structured as follows:

```toml
[bpm]
tracking_name = "upstream-package" # Upstream project from Anitya
package_name = "umpkg" # Package name to build
method = "rpm" # Type, can be rpm, or shell. (TODO: Add support for other methods)
specfile = "umpkg.spec" # (RPM) Specfile to use
repo = "https://github.com/Ultramarine-Linux/pkg-umpkg" # HTTP URL to the repo
```

BPM will listen to the Anitya upstream updates topic, and check if the `tracking_name` variable matches the Anitya project name. If it does, It will clone the repo, perform the changes specified in the method, and push the changes to the downstream repo.

What happens next depends on how the repos are configured. One could set up an automatic CI system on each push to build the package, or manually build the package.

## Setup

TODO