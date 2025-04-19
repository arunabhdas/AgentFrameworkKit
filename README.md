# AgentFrameworkKit
AgentFrameworkKit is an agent orchestration framework built on top of Agent Development Kit


## Steps

* Initialize python virtual environment 
```
uv venv venv --python 3.11
```


* Activate python virtual environment as follows - 

```
source venv/bin/activate
```

* Install 

```
uv pip install google-adk
```


* Create the folder structure in in `agent_framework_kit_agent` folder



*  Rust installation

```
╰─❯ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
info: downloading installer
warn: It looks like you have an existing rustup settings file at:
warn: /Users/coder/.rustup/settings.toml
warn: Rustup will install the default toolchain as specified in the settings file,
warn: instead of the one inferred from the default host triple.

Welcome to Rust!

This will download and install the official compiler for the Rust
programming language, and its package manager, Cargo.

Rustup metadata and toolchains will be installed into the Rustup
home directory, located at:

  /Users/coder/.rustup

This can be modified with the RUSTUP_HOME environment variable.

The Cargo home directory is located at:

  /Users/coder/.cargo

This can be modified with the CARGO_HOME environment variable.

The cargo, rustc, rustup and other commands will be added to
Cargo's bin directory, located at:

  /Users/coder/.cargo/bin

This path will then be added to your PATH environment variable by
modifying the profile files located at:

  /Users/coder/.profile
  /Users/coder/.bash_profile
  /Users/coder/.bashrc
  /Users/coder/.zshenv

You can uninstall at any time with rustup self uninstall and
these changes will be reverted.

Current installation options:


   default host triple: aarch64-apple-darwin
     default toolchain: stable (default)
               profile: default
  modify PATH variable: yes

1) Proceed with standard installation (default - just press enter)
2) Customize installation
3) Cancel installation
> 1

info: profile set to 'default'
info: default host triple is aarch64-apple-darwin
warn: Updating existing toolchain, profile choice will be ignored
info: syncing channel updates for 'stable-aarch64-apple-darwin'
info: latest update on 2025-04-03, rust version 1.86.0 (05f9846f8 2025-03-31)
info: downloading component 'cargo'
  6.5 MiB /   6.5 MiB (100 %)   1.5 MiB/s in  4s         
info: downloading component 'clippy'
  2.5 MiB /   2.5 MiB (100 %)   1.6 MiB/s in  1s         
info: downloading component 'rust-docs'
 21.3 MiB /  21.3 MiB (100 %)   2.2 MiB/s in 10s         
info: downloading component 'rust-std'
 26.6 MiB /  26.6 MiB (100 %)   1.7 MiB/s in 16s         
info: downloading component 'rustc'
 57.9 MiB /  57.9 MiB (100 %)   2.1 MiB/s in 30s         
info: downloading component 'rustfmt'
info: removing previous version of component 'cargo'
info: removing previous version of component 'clippy'
info: removing previous version of component 'rust-docs'
info: removing previous version of component 'rust-std'
info: removing previous version of component 'rustc'
info: removing previous version of component 'rustfmt'
info: installing component 'cargo'
info: installing component 'clippy'
info: installing component 'rust-docs'
 21.3 MiB /  21.3 MiB (100 %)   5.1 MiB/s in  4s         
info: installing component 'rust-std'
 26.6 MiB /  26.6 MiB (100 %)  19.6 MiB/s in  1s         
info: installing component 'rustc'
 57.9 MiB /  57.9 MiB (100 %)  18.3 MiB/s in  3s         
info: installing component 'rustfmt'
info: default toolchain set to 'stable-aarch64-apple-darwin'

  stable-aarch64-apple-darwin updated - rustc 1.86.0 (05f9846f8 2025-03-31) (from rustc 1.85.0 (4d91de4e4 2025-02-17))


Rust is installed now. Great!

To get started you may need to restart your current shell.
This would reload your PATH environment variable to include
Cargo's bin directory ($HOME/.cargo/bin).

To configure your current shell, you need to source
the corresponding env file under $HOME/.cargo.

This is usually done by running one of the following (note the leading DOT):
. "$HOME/.cargo/env"            # For sh/bash/zsh/ash/dash/pdksh
source "$HOME/.cargo/env.fish"  # For fish
source "$HOME/.cargo/env.nu"    # For nushell
```

* Run

```
╰─❯ npm create tauri-app@latest

> npx
> create-tauri-app

✔ Project name · agentframework
✔ Identifier · app.agentframework
✔ Choose which language to use for your frontend · TypeScript / JavaScript - (pnpm, yarn, npm, deno, bun)
✔ Choose your package manager · npm
✔ Choose your UI template · Vanilla
✔ Choose your UI flavor · JavaScript

Template created! To get started run:
  cd agentframework
  npm install
  npm run tauri android init
  npm run tauri ios init

For Desktop development, run:
  npm run tauri dev

For Android development, run:
  npm run tauri android dev

For iOS development, run:
  npm run tauri ios dev
```

### Steps scaffold for agent_framework_kit_tauri

```
╰─❯ npm create tauri-app@latest               

> npx
> create-tauri-app

✔ Project name · agentframework
✔ Identifier · app.agentframework
✔ Choose which language to use for your frontend · TypeScript / JavaScript - (pnpm, yarn, npm, deno, bun)
✔ Choose your package manager · npm
✔ Choose your UI template · Vue - (https://vuejs.org/)
✔ Choose your UI flavor · TypeScript

Template created! To get started run:
  cd agentframework
  npm install
  npm run tauri android init
  npm run tauri ios init

For Desktop development, run:
  npm run tauri dev

For Android development, run:
  npm run tauri android dev

For iOS development, run:
  npm run tauri ios dev

npm notice
npm notice New minor version of npm available! 11.2.0 -> 11.3.0
npm notice Changelog: https://github.com/npm/cli/releases/tag/v11.3.0
npm notice To update run: npm install -g npm@11.3.0
npm notice

```

### Steps for develop for agent_framework_kit_tauri
```
cd agent_framework_kit_tauri

npm install

npm run tauri dev

```

### Steps for develop for agent_framework_kit_tauri iOS
```
npm run tauri ios init

npm run tauri ios dev
```

## Links for agent_framework_kit_tauri
https://youtu.be/YmDKih6oJK4?si=FE__y9L2xzeZaItx