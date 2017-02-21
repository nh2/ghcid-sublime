# Showing Haskell compile errors in Sublime with ghcid

## Installation

1. Copy `ghc-output-joinlines.py` into `$HOME/bin`, and add this directory to your `PATH` in your shell's config.
2. Put `haskell-ghcid.sublime-build` into `$HOME/.config/sublime-text-3/Packages/User/`
3. Restart Sublime

Then you can select it in the Sublime menu via `Tools -> Build System -> haskell-ghcid`.

## Per-project setup

1. Set up a command that builds/typechecks your code when you save your files in Sublime, and writes the compiler error messages to `ghcid.txt`. That works with many different build tools; examples of how that can be done:
  * With **plain GHC** and bash: `while inotifywait -e close_write myfile.hs; do ghc --make myfile.hs 2>&1 | tee ghcid.txt; done`
  * With **stack**: `ghcid "--command=stack repl" -o ghcid.txt --restart=myproject.cabal`
  * With **cabal**: `ghcid "--command=cabal repl" -o ghcid.txt --restart=myproject.cabal`
  * With **plain ghcjs** and bash: `while inotifywait -e close_write myfile.hs; do ghc --make myfile.hs 2>&1 | tee ghcid.txt; done`
2. If you use `inotifywait` above, save the file at least once so that `ghcid.txt` is created.
3. Add the directory that contains `ghcid.txt` to Sublime (`Project -> Add Folder to Project`).

Then you can press the build shortcut (`Ctrl+B` by default on Linux) to have your error messages appear in Sublime.
