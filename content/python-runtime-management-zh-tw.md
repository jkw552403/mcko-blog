---
Title: 2021年了，該如何配置Python開發環境 - Part  1 Python 版本管理
Date: 2021-03-08 00:10
Category: Blogging
Tags: Python
Slug: python-runtime-management
Lang: zh-tw
---
我在工作上常需要同時維護以及開發多個Python專案。而在管理Python時，往往會遇到一些問題：

1. 你會需要管理Python runtime。你的作業系統通常會已經安裝一個比較舊的Python版本而你為了一些工具或者新功能需要用新一點的Python版本。
2. 不同的專案往往需要不同的套件。你會需要一個工具來管理專案裡的套件。你可以自由地增加以及移除套件，而那個工具要保證reproducibility，讓你同事的機器或者生產環境可以保持一致。
3. 而有些時候你會需要安裝一些全域工具，但你不知道應該要把它裝到哪裡或者如何管理他們。

在這個系列裡面，我會介紹一些用來管理Python runtime以及套件的工具。我會用兩篇來介紹他們，現在這個第一篇會著重在Python runtime管理，會介紹 [pyenv](https://github.com/pyenv/pyenv)、 [asdf](https://asdf-vm.com/)、以及 [conda](https://docs.conda.io/en/latest/)。

## pyenv
如果我們只討論只能做runtime管理的工具，那我想 `pyenv` 是裡面最受歡迎的工具。你可以非常輕易地用 `pyenv` 安裝多個Python版本並且在它們之間切換。除了大家最常用的CPython外，也支援很多不同的distributions。另外一個很重要的功能是，你可以用 `pyenv` 來幫各個專案設定不同的Python環境或者是全域的版本。 

### 安裝
如果你是Mac使用者，你可直接用Homebrew安裝，不是的話可以參考 [pyenv-installer](https://github.com/pyenv/pyenv-installer). 另外 `pyenv` 會需要改一些系統變數以及加初始化指令到你的shell裡，如果跟我一樣使用 `zsh` 的話，可以直接下面加到 `~/.zshrc`。

```bash
export PYENV_ROOT="$HOME/.pyenv
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

如果你使用不同的shell，請參考[這裡](https://github.com/pyenv/pyenv#installation)。

一般來說，我也會建議安裝[pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)來管理virtualenv. 跟 `pyenv` 一樣，你可以用Homebrew安裝或者參考他們的[指示](https://github.com/pyenv/pyenv-virtualenv)。記得也要將 `eval "$(pyenv virtualenv-init -)"` 加到你的shell裡。

### 用法
有幾個比較重要的指令：
#### 列出所有可安裝的Python版本
在安裝前通常你會想知道你有什麼版本可以安裝：
You will need to know which version you can install:
```bash
pyenv install --list
```

![pyenv-install-list.png]({static}/images/pyenv-install-list.png)

### 安裝某個Python版本
假設我們想安裝CPython 3.9.1，需要執行
```bash
pyenv install 3.9.1
```

#### 設定全域Python環境以及專案的Python環境
有些時候你會想設定一個全域Python當作預設的環境：
```bash
pyenv global 3.9.1
```

而有些時候你會想替每個專案設置設定不同的Python環境
```bash
# 假設你已經在專案目錄下
# 這個指令會產生一個名為 `.python-version` 的檔案
pyenv local anaconda3-5.3.1
```

#### 跟 `pyenv-virtualenv` 一起使用
`pyenv-virtualenv` 提供幾個簡單的指令來管理virtualenv以及conda環境：
```bash
# 用之前安裝好的3.9.1建立一個名為 venv-3.9.1 的 virtualenv
pyenv virtualenv 3.9.1 venv-3.9.1
# Activate 這個新的 virtualenv
pyenv activate venv-3.9.1
# 刪除這個 virtualenv
pyenv virtualenv-delete venv-3.9.1
```

這些創建出來的virtualenv同樣可以被前面的 `pyenv local/global` 利用。這可以說是我最常用來管理專案環境的方法：先建立一個新的virtualenv或者conda環境，然後在專案目錄執行 `pyenv local a-new-venv` 來設定環境。之後我會將需要的套件給裝到這個環境中，而所有在這個目錄底下執行的指令都會使用這個獨立的環境。


## asdf
[asdf](https://asdf-vm.com/)是一個可以管理多個語言runtime的工具。 `asdf` 的設計是基於plugin，你要安裝任何語言或者是工具都要先加入對應到的plugin。這也讓 `asdf` 的生態系非常易於擴充，可以到[這裡]()看 `asdf` 已經支援的列表。當初我是發現 `nvm` 拖慢了我zsh的啟動時間，在解決的過程中發現了 `asdf` 這個工具。然後也發現它可以用來安裝 Python，並且用法跟 `pyenv` 十分相似。

### 安裝
跟 `pyenv` 一樣，我用Homebrew來安裝 `asdf`：
```bash
brew install asdf
```

並將下面這行加到我的 `~.zshrc`：
```bash
. $(brew --prefix asdf)/asdf.sh
```

如果不是用Mac，可以參考 `asdf` 的[官方文件](https://asdf-vm.com/#/core-manage-asdf?id=install)。

### 用法

#### 設定 Python plugin
在正式安裝Python之前，會先需要設定Python plugin：
```bash
asdf plugin-add python
```

#### 安裝某個Python版本
如果你需要安裝CPython 3.9.1
```bash
asdf install python 3.9.1
```

`asdf`的Python plugin實作裡面其實也是基於由 `pyenv` 社群所維護的一款名為 [python-build](https://github.com/pyenv/pyenv/tree/master/plugins/python-build) 的工具。所以基本上你可以用 `asdf` 安裝所有 `pyenv` 支援的版本。

#### 設定全域Python環境以及專案的Python環境
這邊用法基本上與 `pyenv` 是類似的。唯一的差異是你會需要在指令中指定 plugin 名稱。在我們的例子裡面就是 `python`。
```bash
asdf global python 3.9.1
# 假設你已經在專案目錄下
# 這個指令會產生一個名為 `.tool-version` 的檔案
asdf local python anaconda3-5.3.1
```

### 注意：沒有像 `pyenv-virtualenv` 一樣方便管理 virtualenv 的功能
雖然 `asdf` 幾乎支援所有常見的語言，但我還是使用 `pyenv` 來管理 Python runtime。最主要的理由是 `asdf` 目前還不能拿來管理virtualenv。issue裡面已經有人提出 [issue](https://github.com/asdf-vm/asdf/issues/636)。也有人提出用 `virtualenv` 搭配 `asdf-direnv` 來做到同樣的效果。不過我現在還是覺得直接使用 `pyenv` 會更加便利。

## conda
[conda](https://docs.conda.io/en/latest/)是在科學計算方面較為受歡迎的套件管理工具。Python的科學計算套件常常需要用編譯器以及一些系統套件來進行安裝。對新手來說，有些時候安裝過程並不輕鬆。而 `conda` 可以幫助你解決大部分的問題。通常你只需要執行 `conda install {PACKAGE-YOU-NEED}` 進行安裝。`conda` 會依照你的環境下載他們已經編譯好的版本。


### 安裝
我自己偏好用 `pyenv` 來安裝 `conda`。你也可以從他們官網上找到安裝檔進行安裝。

### 用法
`conda` 也提供一些Python runtime。像是CPython跟PyPy。如果你需要安裝Python 3.6的conda環境，可以執行：

```bash
conda create -n py36 python=3.6
```

`conda` 會幫你創建一個新環境而你可以用 `conda activate` 來 activate 這個環境到你的shell。


conda所創建的環境其實也可以被 `pyenv` 所管理。我自己就偏好用 `pyenv` 來管理所有環境：
```
# 假設你已經有安裝好的 conda
# 這個 pyenv 指令會用 anaconda3-2019.03 這個版本裡的 conda 來創建一個新的環境
pyenv virtualenv anaconda3-2019.03 conda-test-env
# 設置這個資料夾底下的Python環境
pyenv local conda-test-env
# 這個指令可以用來刪除環境
pyenv virtualenv-delete conda-test-env
```

## 結論
* 我會推薦 `pyenv` 給大部分的Python開發者，因為 `pyenv` 跟 `pyenv-virtualenv` 的組合可以同時管理Python runtime以及virtualenv。
* 個人認為 `asdf` 算是在語言版本管理工具裡面十分有潛力的一個。不過在Python的管理上目前還沒有 `pyenv` 來得方便。

下一篇會介紹如何進行套件管理。Stay tuned!
