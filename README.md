# Builds Per Minute

Builds Per Minute (BPM) is a Fedora messaging consumer that tracks upstream updates from Anitya (release-monitoring.org) and automatically updates the downstream repository for that project.

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


## Why?

Tracking upstream is hard. Sometimes, a new version of your upstream project is released, but you're too busy or lazy to automatically update the repo downstream. BPM will help you do that.

Ultramarine Linux has issues with gaining maintainers for our packages, And the main maintainer is not always available to repackage every single package with our downstream patches. BPM ensures the sanity of Ultramarine Linux developers by automatically repacking packages when upstream updates are released. This is a great way to ensure that Ultramarine Linux is always up to date. As new packages will get pushed automatically to the users, and bugs are then fixed by manual intervention.

There has been many attempts to automate the repackaging process, most of them very specific to their respective parent projects, like the [Chaotic-AUR] or Fedora's [the-new-hotness]. BPM is supposed to be a general solution that can be used for any package and any language.

## What's the difference from the-new-hotness?

While BPM is fundamentally and architecturally similar to the-new-hotness, it technically does not do the same thing. BPM automatically updates git repos and pushes them to the specified downstream repo, and is supposed to be a general purpose CD system that reacts to upstream updates.

[the-new-hotness] is a more specialized system that is designed for Fedora. Instead of directly editing downstream, it posts an issue onto Red Hat's Bugzilla to notify the Fedora maintainers that a new upstream version is available, then builds the package as a test in Koji. BPM directly edits the downstream repo, and the CI system for that repo is responsible for building the package. Thus BPM can be used for any repository, unlike the-new-hotness which can only be used for RPM packages.

## Setup

TODO

[the-new-hotness]: https://github.com/fedora-infra/the-new-hotness
[Chaotic-AUR]: https://aur.chaotic.cx/