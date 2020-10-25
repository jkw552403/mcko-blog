---
Title: 在JupyterLab裡使用D3.js
Date: 2020-10-25 23:52
Category: Data Visualization
Tags: DataScience,D3,Jupyter
Slug: d3-in-jupyterlab
Lang: zh-tw
---

## 背景
之前工作上有需要對做 hierarchical clustering 結果做視覺化的 task。做資料處理以及建模這塊是使用 Python 相關的工具但Python的ecosystem似乎沒有可以像 [d3-hierarchy](https://github.com/d3/d3-hierarchy) 一樣提供互動性以及這麼多客製化選項的工具。而且考慮呈現方式時，也是使用 D3.js 這類工具整合網頁對stakeholder來說會比較方便。

在開發階段的問題主要就是我們在JupyterLab上面做調整，而JupyterLab現在並沒有支援可以呈現 D3.js 結果的 extension (在Jupyter Notebook上有[一個](https://github.com/ResidentMario/py_d3)，但目前看起來沒有要移植到JupyterLab的計畫)。造成開發上一些小不便。

這篇文章會用 [Observable](https://observablehq.com/) 上的這個 [Collapsible Tree](https://observablehq.com/@d3/collapsible-tree) 當作例子，試著改寫裡面內容讓它可以在JupyterLab裡面使用。

## 在JupyterLab裡面執行JavaScript
JupyterLab本身就是JavaScript或者是說TypeScript所寫成，IPython內建的magic裡面有支援[javascript magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html#cellmagic-javascript)，可以直接在Notebook裡面執行JavaScript的程式碼。也可以透過IPython的API使用Python執行含有JavaScript程式碼的字串：

```python
from IPython.display import Javascript
Javascript(
    'console.log("D3 is awesome!")'
)
```
執行完上面這段程式碼後可以在瀏覽器的Console中看到 "D3 is awesome!" 這段log。


要用D3.js以及d3-hierarchy前我們需要載入他們的script，這邊可以透過html magic來完成：
```html
%%html
<script src="https://d3js.org/d3.v6.min.js"></script>
<script src="https://d3js.org/d3-hierarchy.v2.min.js"></script>
```

## 改寫Observable的語法
Observable有支援一些特殊的語法，而我們要將 Observable 上特別的寫法成普通的D3 JavaScript。

```javascript
// 將Observable notebook最底下跟大小跟style有關的變數拿過來
const dx = 10;
const width = 1080; // 設一個適合你環境的寬度
const dy = width / 6;
const margin = ({top: 10, right: 120, bottom: 10, left: 40})
const tree = d3.tree().nodeSize([dx, dy]);
```

後面會把這部分跟Observable裡面chart的部分擺在一起來使用。

## 選取JupyterLab中的cell輸出 (修改 chart 裡面的 d3.select)

例子裡面chart的部分是會回傳 `svg.node()` 當作輸出，而正常使用D3.js的時候，通常會加一個 `svg` 的元素到HTML中，在JupyterLab裡面，我們希望是加到cell的output裡面，而JupyterLab每個cell會用一個 `element` 變數表示當前 output 的DOM，所以我們需要用 `d3.select` 選取這個DOM並且加我們要輸出的svg到裡面去：

```javascript
// 省略其餘的 JavaScript...
const svg = d3.select(element)
	.append("svg")
// 省略其餘的 JavaScript...
```

chart除了最後面 `return svg.node()` 需要拿掉，剩下部份就直接沿用即可。

## 將Python的資料傳給JavaScript來使用
這個例子裡面資料 (`flare-2.json`) 已經是D3可以接受的hierarchical格式，如果大家的資料不是這種格式，請參照 [d3.hierarchy](https://observablehq.com/@d3/d3-hierarchy) 來修改。我們這邊用Python的library來讀這個json：

```python
# 假設檔案在你的CWD
with open('./flare-2.json') as f:
    data_str = f.read()
```

這邊我們用一個簡單明瞭的方式把值傳到JavaScript裡面。例子裡面用`const root = d3.hierarchy(data)`的方式傳入資料，我們將 `data` 這個變數直接用上面讀好的json字串換成 `$data` ，然後把將上面幾個步驟處理完的JavaScript一起傳入Python stdlib中的 [Template](https://docs.python.org/3/library/string.html#template-strings)：
```python
tree_js_template = Template("""
// 省略其餘的 JavaScript...
const root = d3.hierarchy($data);
// 省略其餘的 JavaScript...
"""
)
```

接下來只要把Template中的$data替換成真正的data，傳到IPython的 `JavaScript` 函式就大功告成了：

```python
JavaScript(tree_js_template.safe_substitute(data=data_str))
```

## 完整範例
完整的程式碼可以參考[這裡](https://gist.github.com/jkw552403/c630ddfbbb1af97e86e17e1d0bf4eb83)。



## 總結
這邊很簡單地將一個Observable上的例子改寫，如果你的JavaScript程式碼比較複雜，可以考慮獨立寫成一個檔案來使用，也可以試功能比齊全的template library像是[Jinja](https://jinja.palletsprojects.com/en/2.11.x/)。看得懂日文的讀者可以參考[這篇](https://horomary.hatenablog.com/entry/2020/02/25/000818)。
