# Notes course of Python DevTalles

![Python Logo](https://www.python.org/static/img/python-logo.png)

## Instructions to install Python

### Windows

1. Go to [Python Page](https://www.python.org/)

2. Install the latest version in the section Downloads

3. Execute the installer

4. make sure in the installation mark the 'Add Python to path' option

5. one time the installation end check in the terminal with the command `python --version`

### MacOS and Linux

I use Linux so the tool i recommended for this Operative System is [Pyenv](https://github.com/pyenv/pyenv) this is a version manager like NVM for NodeJS but for Python

This tool works in windows but i don't know how this works in this OS so i don't recommend that

**In MacOS you can use Brew for the installation in this case i show how to install with curl**

1. Install Pyenv

   ```zsh
   curl -fsSL https://pyenv.run | bash
   ```

2. Set up your shell environment for Pyenv

   ```zsh
   ~/.pyenv/bin/pyenv init --install
   ```

3. Restart your shell

   ```zsh
   exec "$SHELL"
   ```

4. Install dependencies (this works in linux Ubuntu/Debian/Mint, for MacOS check [this link](https://github.com/pyenv/pyenv/wiki#suggested-build-environment))

   ```zsh
   sudo apt update; sudo apt install make build-essential libssl-dev zlib1g-dev \
   libbz2-dev libreadline-dev libsqlite3-dev curl git \
   libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev libzstd-dev
   ```

5. Install Python with `pyenv install <python version>`

6. Set python version has global `pyenv global <python version>`

7. Check version with `python --version` (with pyenv is not necessary use python3)

## Extensions for VsCode

1.  [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
2.  [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
3.  [Python Debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy)
4.  [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent)
5.  [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring)
6.  [AutoPep8](https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8)
7.  [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens)

## Commands for Python

the command python depends of OS if you are in Linux or MacOS is `python3` and for windows is `python` so i use python for reflex booth and the same time for `pip`, `pip3` for windows and the rest with `pip`

Pip is equal to pip install packages

- See version of Python installed

  ```zsh
  python --version
  ```

- Execute a python file

  ```zsh
  python <file>
  ```

- See PIP version

  ```zsh
  pip --version
  ```

- See all packages installed with pip

  ```zsh
  pip list
  ```

- Install package with pip

  ```zsh
  pip install <package>
  ```

- Update pip

  ```zsh
  pip install --upgrade pip
  ```
