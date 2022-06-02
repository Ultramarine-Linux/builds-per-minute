# Builds Per Minute

Builds Per Minute (BPM) is a Fedora messaging consumer that tracks upstream updates from Anitya (release-monitoring.org) and automatically builds new packages for Ultramarine Linux.

This code is still early in development, and is not ready for production use.

## How it works

BPM will load a set of config files at the folder specified in the `config_dir` variable in the global config. The global configuration file is `bpm.toml` and is required for BPM to function. For each config file, it will load them and add it to memory.

The config file is a YAML file and is structured as follows:

```yaml
upstream_name: umpkg
package_name: umpkg
build:
  method: rpm
  specfile: umpkg.spec
repo: https://github.com/Ultramarine-Linux/pkg-umpkg
```

BPM will listen to the Anitya upstream updates topic, and check if the `tracking_name` variable matches the Anitya project name. If it does, It will clone the repo, perform the changes specified in the method, and push the changes to the downstream repo.

What happens next depends on how the repos are configured. One could set up an automatic CI system on each push to build the package, or manually build the package.

## Setup

TODO