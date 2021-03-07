---
Title: Python Environment in 2021 - Part  1, Python Runtime Management
Date: 2021-03-08 00:10
Category: Blogging
Tags: Python
Slug: python-runtime-management
Lang: en
---
I need to maintain and develop multiple Python projects in my work. And I found Python environment management is never easy:

1. You need to manage Python runtimes. Your operation system might already install an older version of Python, and you need to use new Python runtimes for new features or some tools. How to switch seamlessly between multiple Python runtimes is a problem.
2. Different projects are using different packages. You will need a tool to manage your dependencies in your project. With the tool, you can add or delete a new dependency freely, and the tool must ensure the reproducibility for your coworkers and the production environment.
3. Sometimes, you want to install tools/applications written in Python globally, but you don't know the best way to install or manage them.

I will introduce Python runtime and dependency management tools, which can help developers manage their Python environments in two posts. This first post will focus on Python runtime management. Three tools, [pyenv](https://github.com/pyenv/pyenv), [asdf](https://asdf-vm.com/), and [conda](https://docs.conda.io/en/latest/) will be introduced.

Note: I only use MacOS and Linux in my work, so please check Windows or WSL supports of these tools if you are Windows users.

## pyenv
If we only discuss pure Python runtime management tools, I think `pyenv` is the most popular solution. With `pyenv`, you can easily install multiple Python runtimes to your environment and switch between them. It supports not only CPython but some other distributions like Jython. Another critical feature is users can configure Python runtimes for each project or globally.

### Installation
You can install `pyenv` using Homebrew (if you're using Mac) or [pyenv-installer](https://github.com/pyenv/pyenv-installer). `pyenv` will also need you to modify a few variables and add `pyenv init` to your shell. If you are a `zsh` user like me, add the following lines to `~/.zshrc`:

```bash
export PYENV_ROOT="$HOME/.pyenv
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Please refer to the [Installation](https://github.com/pyenv/pyenv#installation) part if you are using a different shell.

I also suggest installing [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) to manage your virtualenv. Like `pyenv`, you can install `pyenv` with Homebrew or follow their [instructions](https://github.com/pyenv/pyenv-virtualenv) if you're not using Mac. Don't forget to add `eval "$(pyenv virtualenv-init -)"` to your profile to enable `pyenv-virtualenv` for your shell.

### Usage
There are a few important commands:
#### Show all available Python versions
You will need to know which version you can install:
```bash
pyenv install --list
```


![pyenv-install-list.png]({static}/images/pyenv-install-list.png)

#### Install a Python version
Assume we need to install CPython 3.9.1, execute
```bash
pyenv install 3.9.1
```

#### Set Python environment globally and locally
Sometimes you want to set a global Python environment: 
```bash
pyenv global 3.9.1
```


When you need to set up a local Python environment for a project:
```bash
# Assume you are under the project directory
# This command will create a `.python-version` file
pyenv local anaconda3-5.3.1
```

#### Use with `pyenv-virtualenv`
`pyenv-virtualenv` provides simple commands to manage virtualenv and conda environments:
```bash
# Create virtualenv with 3.9.1 installed by pyenv
pyenv virtualenv 3.9.1 venv-3.9.1
# Activate virtualenv
pyenv activate venv-3.9.1
# Delete virtualenv
pyenv virtualenv-delete venv-3.9.1
```

You can also use `pyenv local/global` with the environments created by `pyenv-virtualenv`. This is my favorite way to manage the Python environment for a new project: I'll make a virtualenv or a conda environment and execute `pyenv local a-new-venv` under the project directory. Then I can install all the dependencies to this environment, and every command run in this directory will use this separated environment.


## asdf
[asdf](https://asdf-vm.com/) is a CLI tool to manage runtime versions for different languages. It provides a plugin system to extend supports for different languages easily. If you want to install a new language or a new tool, you will need to add the related plugin first. You could click [here](https://github.com/asdf-vm/asdf-plugins/tree/master/plugins) to check the plugins supported by `asdf`. The reason I started to use `asdf` is to replace `nvm`, which significantly slowed down my zsh startup. And I found `asdf` can also manage Python versions, and the usage is similar to `pyenv`.

### Installation
Same as `pyenv`, I use Homebrew to install `asdf`:
```bash
brew install asdf
```

And add this line to my `~.zshrc`:
```bash
. $(brew --prefix asdf)/asdf.sh
```

Please read the official documentation [here](https://asdf-vm.com/#/core-manage-asdf?id=install) if you're not using Mac.

### Usage

#### Set up Python plugin
You will need to install the Python plugin first:
```bash
asdf install python
```

#### Install a Python version
If you need to install CPython 3.9.1
```bash
asdf install python 3.9.1
```

`asdf` Python plugin also relies on [python-build](https://github.com/pyenv/pyenv/tree/master/plugins/python-build), which is maintained by `pyenv` community to build Python runtimes. Hence, `asdf` can install every version you find in `pyenv`.

#### Set Python environment globally and locally
Usages here are almost the same as `pyenv`. The only difference is you need to specify the plugin name (`python` in our case) in your commands:
```bash
asdf global python 3.9.1
# Assume you are under the project directory
# This command will create a `.tool-versions` file
asdf local python anaconda3-5.3.1
```

### Notice: no simple virtualenv management like `pyenv-virtualenv` in `asdf`
Although `asdf` can manage runtimes for most popular languages, I'm still using `pyenv` for Python runtimes because `asdf` can't manage virtualenv at the time of writing. There are already some [issues](https://github.com/asdf-vm/asdf/issues/636) related to this feature. So far, what you can do is to use `virtualenv` and `asdf-direnv` together to make virtualenv work in your local directory. I feel `pyenv` is more convenient for virtualenv management.

## conda
[conda](https://docs.conda.io/en/latest/) is one of the popular environment management tools for scientific packages. Python scientific packages usually require a compiler with some system packages, and the whole installation process could be tiring for beginners. But with `conda`, you don't need to deal with the complex installation process anymore! Most of the time, you just need to `conda install {PACKAGE-YOU-NEED}` for installation. `conda` will automatically download pre-built binary and their dependencies.

### Installation
I prefer to use `pyenv` to install `conda`, and you can also use binaries from conda site.

### Usage

`conda` also provides some Python runtimes like CPython or PyPy, so when you create a new runtime environment with Python 3.6, run:
```bash
conda create -n py36 python=3.6
```

This will create a new conda environment, and you can use `conda activate` to enable it in your shell.

conda environments can be managed by `pyenv` as well, and I prefer to use `pyenv` to manage everything:

```bash
# Assume you already installed conda using pyenv
# Use pyenv command to create a conda environment
pyenv virtualenv anaconda3-2019.03 conda-test-env
# Set local Python environment for the current directory
pyenv local conda-test-env
# Use pyenv command to delete a conda environment
pyenv virtualenv-delete conda-test-env
```

## Conclusions
* `pyenv` + `pyenv-virtualenv` can help you manage both runtimes and virtualenv. I will recommend it to most Python users.
* `asdf` has great potential to unify runtime managements for popular programming languages, but it's not as good as `pyenv` for Python users now.

Stay tuned for the next post!
