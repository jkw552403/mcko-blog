---
Title: 使用Zsh + Zim + Powerlevel10k打造屬於自己的Terminal環境
Date: 2021-01-26 00:30
Category: Tooling
Tags: Terminal
Slug: zim-zsh-powerlevel10k
Lang: zh-tw
---

## 背景
從2017年底換到目前工作之後就一直保持著Zsh + Oh My Zsh + Powerlevel9k的配置。最近從公司拿了新的MacBook Pro，想說新電腦新氣象，可以來換個配置。大概研究了一下後就換成了 Zsh + Zim + Powerlevel10k。

換掉Powerlevel9k的理由很簡單，因為官方不再支援也deprecated的repository裡面也推薦使用powerlevel10k。至於Oh My Zsh的話是Zim號稱速度在這些configuration framework裡面是最快的。有些舊一點或者是來自Oh My Zsh 的 plugin可能沒有直接列出使用Zim的安裝方式，不過通常去看一下程式碼以及載入方法後也是可以支援(後面會提)。以下會說明一下如何安裝以及配置這套環境。


## 安裝Zsh
如果你的環境跟我新電腦都已經是macOS Catalina(10.15)以上，預設shell都已經是Zsh了。如果不追求新版本也不需要手動安裝Zsh。不過我自己手上還有比較舊的Mac，所以還是用Homebrew安裝了新版本保持一致。
```bash
brew install zsh
```
如果你是使用其他Linux的distro或是WSL，請自行查閱所在環境Zsh的安裝方法。


## 安裝Zim
Zim的 [repository](https://github.com/zimfw/zimfw) 上有透過curl或者wget的安裝方法：
```bash
# curl
curl -fsSL https://raw.githubusercontent.com/zimfw/install/master/install.zsh | zsh
# wget
wget -nv -O - https://raw.githubusercontent.com/zimfw/install/master/install.zsh | zsh
```
如果你之前已經有安裝其他framework(像是Oh My Zsh)，請在執行上面命令之前移除舊的framework。

我第一次安裝也是使用了上面自動安裝的命令，不過因為我有在用 [yadm](https://yadm.io/) 管理Dotfiles的關係，有再研究了一下[手動安裝的方式](https://github.com/zimfw/zimfw#manual-installation)。
簡單來說，會需要手動準備下面幾個檔案到你的家目錄底下，點開連接並複製到所需的路徑即可。

- [~/.zshenv](https://github.com/zimfw/install/blob/master/src/templates/zshenv)
- [~/.zshrc](https://github.com/zimfw/install/blob/master/src/templates/zshrc)
- [~/.zlogin](https://github.com/zimfw/install/blob/master/src/templates/zlogin)
- [~/.zimrc](https://github.com/zimfw/install/blob/master/src/templates/zimrc)
- [~/.zim/zimfw.zsh](https://github.com/zimfw/zimfw/releases/latest/download/zimfw.zsh)

如果你本來環境裡面已經有這些檔案的話，可能要注意一下不要覆蓋到現有的環境。像是我已經有將 `~/.zshrc` 加入版本管理，所以我是將zshrc template的內容加到現有的 `~/.zshrc` 裡面而不是覆蓋。
檔案都準備好後執行底下的install命令Zim就安裝完成了。
```bash
zsh ~/.zim/zimfw.zsh install
```

### 用Zim安裝plugin/module
Zim使用了 `~/.zimrc` 這個檔案來管理plugin。如果稍微看一下Zim install的實作，其實可以發現install所做的是將GitHub上的script給下載下來並且更新 `~/.zim/init.zsh `來讓Zsh每次打開都會載入這些script。
對於普通的使用者，通常我們只需要看一下我們想用的套件裡面Zim的安裝指示，然後照著指示更新 `~/.zimrc` 並且執行 `zimfw install` 就可以了。
像是[powerlevel10k](https://github.com/romkatv/powerlevel10k/blob/master/powerlevel10k.zsh-theme#zim)，我們只需要加一行 `zmodule romkatv/powerlevel10k` 到 `~/.zimrc` 再執行 `zimfw install` 就大功告成了。

如果你使用的套件沒有列出使用Zim的安裝方法只是或者它是Oh My Zsh的官方套件，可能就需要改一下 `zmodule` 的參數來讓Zim找到需要載入的script。譬如說我想使用Oh My Zsh裡面[docker-compose](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/docker-compose)以及[kubectl](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/kubectl)兩個plugin。因為 `zmodule` 預設只會找根目錄底下的檔案，我們需要使用 `-f` 來指定將子目錄加到file path以及使用 `-s` 來告訴Zim我們要載入的script在哪裡。這邊是我安裝上面兩個plugin的寫法：
```bash
# ~/.zimrc
# Other plugins in ~/.zimrc...
zmodule ohmyzsh/ohmyzsh -f 'plugins/kubectl' -s 'plugins/kubectl/kubectl.plugin.zsh' -f 'plugins/docker-compose' -s 'plugins/docker-compose/docker-compose.plugin.zsh'
```

更詳細的參數可以參考[官方文件](https://github.com/zimfw/zimfw#usage)或者是這個 [issue](https://github.com/zimfw/zimfw/issues/374)。

## Powerlevel10k
Powerlevel10k我上面也有提到，是用Zim來安裝的。只要加一行 `zmodule romkatv/powerlevel10k` 到 `~/.zimrc` 再執行 `zimfw install` 就可以了。如果你之前有的配置檔裡面已經Powerlevel9k的設置，[官方文件](https://github.com/romkatv/powerlevel10k#does-powerlevel10k-always-render-exactly-the-same-prompt-as-powerlevel9k-given-the-same-config)是說跟之前幾乎會長得一模一樣。不過這次我是有透過Powerlevel10k提供的[Configuration Wizard](https://github.com/romkatv/powerlevel10k#configuration-wizard)來重新設置：
```bash
p10k configure
```

官方文件裡面有提到說在跑前 `p10k configure` 要先安裝他們推薦的字體，不過你在使用的terminal emulator是iTerm2或Termux，也可以透過Powerlevel10k自動安裝。

## 成果
這個是我搭配iTerm2內建的Color Presets(Smoooooth)最後長的樣子：
![zsh-zim-powerlevel10k-result.png]({static}/images/zsh-zim-powerlevel10k-result.png)  
所有Dotfiles都可以在[這裡](https://github.com/jkw552403/dotfiles)找到，如果是直接想看這個Powerlevel10k配置的也可以直接點這個 [.p10k.zsh](https://github.com/jkw552403/dotfiles/blob/b693fb91b02f85d1627e1a77191789af6f4185b9/.p10k.zsh)。在使用體驗上，載入速度來說有比Oh My Zsh快一些些。如果對速度有要求的朋友可以參考，但真的很慢的話最好還是透過profiling研究一下載入的時候做了什麼比較好。以我的例子來說 載入 `kubectl` 的補全就佔了很大一部分時間，但也捨不得拿掉XD。希望這篇文章有幫助大家打造屬於自己的環境。
