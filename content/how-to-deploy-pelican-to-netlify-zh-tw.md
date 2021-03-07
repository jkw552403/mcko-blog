---
Title: 如何在Netlify上部署以Pelican搭建的靜態網站
Date: 2020-05-26 20:00
Category: Blogging
Tags: Pelican,Netlify,Blog
Slug: how-to-deploy-pelican-to-netlify
Lang: zh-tw
---

這篇文章會介紹如何將以Pelican搭建的靜態網站部署至Netlify上。你會知道這個部落格是如何部署而成的。

# 為什麼使用Pelican跟Netlify

作為一個軟體工程師，我偏好支援Markdown的靜態網站產生器。在考慮的時候也看到其他選擇，像是 [GatsbyJS]([https://www.gatsbyjs.org/](https://www.gatsbyjs.org/)) 這種基於比較新潮的技術的。Pelican雖然不是最新最潮的，不過它的主題以及外掛系統對一般使用者來說也非常夠用。最重要的是Pelican是用Python實作的，所以有問題的時候我可能可以自己修。

# Pelican

這個部分是跟著Pelican提供的 [Quickstart]([https://docs.getpelican.com/en/stable/quickstart.html](https://docs.getpelican.com/en/stable/quickstart.html)) 。`pelican-quickstart` 會讓使用者輸入幾個基本的設定，包括部落格的標題、要使用的網域等等。其中有一個設定是 `Do you want to generate a tasks.py/Makefile to automate generation and publishing?`

。這邊我是填 yes，後面會對這個 Makefile 做一些修改。我會讓 Netlify 用這個 Makefile 來 build 最後的靜態檔案。

再來你可能會想如何客製化你的部落格。Pelican社群已經有許多現成的[主題]([https://github.com/getpelican/pelican-themes](https://github.com/getpelican/pelican-themes))以及[外掛]([https://github.com/getpelican/pelican-plugins](https://github.com/getpelican/pelican-plugins))可以使用。要將主題跟外掛加到部落格的話，我們需要讓Pelican知道主題跟外掛的路徑。因為最後是 Netlify 來 build 這些靜態檔案，我這邊就是簡單地將主題跟外掛的程式碼放在我們的repository裡面。一個做法是用 `git submodule/subtree` ，我自己是用了 [peru]([https://github.com/buildinspace/peru](https://github.com/buildinspace/peru)) 來管理。peru 讓開發者用一個yaml來管理外部的 dependencies，而且也是基於Python實作的。這邊我會加入我所選的主題以及外掛的repository。我用的主題是 [Elegant]([https://elegant.oncrashreboot.com/](https://elegant.oncrashreboot.com/)) ，Elegant其實也在官方repository裡面，不過引用Elegant自己的 repository 可以少 clone 一些程式碼。可以參考我下面的 `peru.yaml` 。我也將 `peru sync` 加到 Makefile 裡面的 `make html` 。所以當Netlify執行時也會下載最新的程式碼。

```yaml
# peru.yaml
imports:
  elegant: blog-theme/elegant
  plugins: plugins

git module elegant:
  url: git://github.com/Pelican-Elegant/elegant

git module plugins:
  url: git://github.com/getpelican/pelican-plugins
  recursive: true
```

```makefile
# Makefile
html:
    peru sync && $(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
```

然後我們可以在 `pelicanconf.py` 設定主題跟外掛的路徑。

```python
# pelicanconf.py
...
root_path = pathlib.Path(__file__).parent

PLUGIN_PATHS = [str(root_path.joinpath('plugins'))]
THEME = str(root_path.joinpath('blog-theme/elegant/').absolute())
...
```

在部署到Netlify之前，我建議可以先在 local build 看看。要注意你至少要有一篇文章才能 build 成功。如果你 local 有遇到問題的話，可以讀一下 Pelican CLI 的文件，Pelican 已經有提供一些方便的 option 來讓使用者 debug 。

# Netlify

在進入Netlify專案設定之前，我們需要準備兩個檔案來設置Python的環境：

1. [requirements.txt]([https://github.com/jkw552403/mcko-blog/blob/8c08bbb60ddfc786588c22b1f8a241b52b33384f/requirements.txt](https://github.com/jkw552403/mcko-blog/blob/8c08bbb60ddfc786588c22b1f8a241b52b33384f/requirements.txt)): 這邊就是準備Python的 dependencies，基本上就是從Pelican跟peru來的。下面的 `requirements.txt` 是我local執行 `pip freeze` 的結果。
2. [runtime.txt]([https://github.com/jkw552403/mcko-blog/blob/8c08bbb60ddfc786588c22b1f8a241b52b33384f/runtime.txt](https://github.com/jkw552403/mcko-blog/blob/8c08bbb60ddfc786588c22b1f8a241b52b33384f/runtime.txt)): 這個檔案會被 Netlify 用來決定 Python 版本。在我寫這篇文章的時候，Netlify可以支援到 Python 3.7。

```
# requirements.txt
blinker==1.4
docopt==0.6.2
docutils==0.16
feedgenerator==1.9.1
Jinja2==2.11.2
Markdown==3.1.1
MarkupSafe==1.1.1
pelican==4.2.0
peru==1.2.0
Pygments==2.6.1
python-dateutil==2.8.1
pytz==2019.3
PyYAML==5.3.1
six==1.14.0
Unidecode==1.1.1
```

```
# runtime.txt
3.7
```

然後我們就可以將目前為止所準備的檔案放到一個 git repository 到 GitHub (或者是你偏好的git服務) 。上傳完畢我們就可以來設定 Netlify。我是跟著[這篇]([https://docs.netlify.com/cli/get-started](https://docs.netlify.com/cli/get-started))，使用 Netlify CLI 來設定。

```bash
# Install netlify cli
npm install netlify-cli -g
# Log in with Netlify. This command will open a browser
# and you need to grant access to Netlify CLI
netlify login
# Set up Netlify project
netlify init
```

`netlify init` 會讓你輸入一些基本的設定、包括要使用哪個 GitHub team、網站名稱以及你要使用的 build command。如果你都跟著我上面的步驟，build command 就輸入 `make html` 就可以讓Netlify順利建置我們的網站了。

# 補充

網域設定：可以從Netlify的專案設定頁上找 **Settings → Domain Management** 然後點擊 **Add domain** **alias** 設定你想設定的網域。底下是我現在的配置。

![Netlify-setting.png]({static}/images/Netlify-setting.png)

整合第三方工具: 如果你需要 Google Analytics，可以透過在 `pelicanconf.py` 中 `GOOGLE_ANALYTICS` 這個變數來設定你的tracking ID。細節可以參考官方文件或者是找找看外掛如果官方不支援你想使用的工具。

這篇文章中的配置檔案都會放到[這裡](https://github.com/jkw552403/mcko-blog)。希望這篇文章幫助到你建立自己的部落格。如果有遇到任何問題也歡迎留言。
