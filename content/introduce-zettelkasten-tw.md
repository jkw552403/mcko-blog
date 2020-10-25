---
Title: Zettelkasten筆記法介紹
Date: 2020-06-22 22:30
Category: Knowledge Management
Tags: Zettelkasten,Note
Slug: introduce-zettelkasten
Lang: zh-tw
---

我一直對知識管理的議題很感興趣，現在一直在使用的相關的工具主要有心智圖跟基於 SRS(Spaced Repetition System)的 Flashcard。這兩個工具滿足了我一些對長期記憶的需求，而最近在 Hacker News 以及 Reddit 上經常看到一種叫 Zettelkasten 的知識管理方法。所以想說幫自己做個整理，就寫下了這篇介紹。

## Zettelkasten 簡介

Zettelkasten 是一個德文詞彙，可以拆成 Zettel 跟 Kasten 來看。Zettel 是卡片或者筆記的意思。而 Kasten 則是盒子的意思，合在一起看就是收納筆記的盒子。當我們在談知識管理或者是筆記的方法論的時候，這個詞通常是指由一位著名的德國社會學家 Niklas Luhmann 所採用的**整理筆記**方式。而 Niklas Luhmann 透過使用 Zettelkasten 成為生產力極高的學者。在三十年內發表了七十本書以及五百篇文章。

所以 Zettelkasten 到底是什麼呢？我這邊先直接翻譯 Reddit 上的[解釋](https://www.reddit.com/r/Zettelkasten/comments/b566a4/what_is_a_zettelkasten/)：

- Zettelkasten 是一種**儲存**以及**管理知識**的方法。可以延伸你的記憶並且促發記憶的連接以及新的想法。
- **Zettel**是筆記的單位(接下來在說筆記的部分大多就是指 Zettel)。每個筆記會跟著一個唯一的 ID，讓筆記之間可以互相連接。因為筆記的量可能非常多，[zettelkasten.de](http://zettelkasten.de/) 的建議是使用時間戳當 ID。這對檢查時間也很方便。
- 在使用 Zettelkasten 的原則裡，常會提到**原子性** (**principal of atomicity**)。一份筆記或者是說一份筆記應該只包含一個主要的想法跟知識。如果你有比較複雜的內容需要寫下的話，應該是將內容拆成多份，再用連接的方式把它們串在一起。
- **連接筆記**。在加入新筆記的時候，要去看過去是否已經有相似的筆記。如果有，可以將相似筆記的 ID 加入到這篇新的筆記形成連接。如果是用軟體來實現 Zettelkasten 的話，用筆記 ID 做搜尋可以找出所有有連接這篇筆記的筆記。另外一個常見的整理方式是標籤(Tag)。
- 不用在文件的結構上花太多心思。不管是分類或是階層系統都會多少限制想法之間的連接。若之後有發現有一些主題相關的筆記，也可以用 meta-notes 來連接這些筆記。也建議應該要有一個方法可以簡單地瀏覽所有的筆記。
- 寫**永久性筆記**。盡量把筆記寫得很清楚並簡明扼要。可以想像成寫 wiki 一樣，這可以讓你在之後忘記當初寫的脈絡還能理解自己的筆記。
- 不要只複製資訊，一定要試著用自己理解的話寫。要對筆記的原始資料處理成你可以理解的資訊。
- 最好還是放上參考。這對學術寫作特別有用因為你會需要引用別人的資料。

簡單來說，Zettelkasten 跟一般筆記最大的差別就是內容之間的連接。有了這些連接，筆記裡面除了內容以外，還能引用到相關的知識，促發你的創造力。可以說這樣非線性的連接方式比起傳統筆記更接近我們的大腦。Zettelkasten 這個方法可以幫我們打造第二大腦。

## Zettelkasten 流程

Niklas Luhmann 的原始做法是使用實體卡片記下內容、標上一個唯一的 ID 做索引、尋找是否有相關的筆記並且紀錄、最後放到抽屜裡面收藏。細節可以 Niklas Luhmann 本人寫的[文章](<(https://luhmann.surge.sh/communicating-with-slip-boxes)>)。這篇原文是德文，是由 [Manfred Kuehn](http://takingnotenow.blogspot.com/) 所翻譯。

以下是我對參考的幾篇文章所總結出的流程：

1. **閱讀原始材料**。在這個步驟你可能會先畫線、寫下摘要或者寫下較短的心得。通常是不會在讀的當下就寫下永久性的筆記。因為永久性筆記需要消化、理解而且要用自己的話寫出。我自己認為邊讀邊寫會非常花時間。比較常見是先閱讀完整份資料，讀完後你會可以判斷哪些部分重要或者是哪些部分不重要。
2. (非必須)閱讀跟寫下永久性筆記之間的**緩衝時間**。這段時間基本上就是用來沈澱，你可能會在這段時間有一些新的想法，也有可能發現有些想法並沒有那麼重要。原則上也是不建議這段時間太長，畢竟閱讀後過幾天就會忘掉不少內容。
3. **寫下永久性筆記**。這份筆記應該包括筆記內容、一個一目瞭然的標題以及唯一的 ID。ID 是 Zettelkasten 的重要元素，用來表示筆記之間的關係。如果你是使用實體卡片要自己設計一個取 ID 的系統，如果是用 Zettelkasten 軟體的話通常在創建筆記時就會給筆記一個 ID。筆記內容需要符合上面所述的原子性，而且要讓未來忘記脈絡的你也可以讀懂。寫的時候要當作是寫給其他人看一樣在寫。有參考的話最好附上。
4. **連接相關筆記**。簡單說就是找出相關的筆記然後在內容底下記下相關筆記的 ID。除了簡單記下 ID 以外，可以的話也寫下為何連接這兩篇筆記的理由。如果你使用的軟體有支援雙向連接(或者是說 backlink)，看相關筆記的時候也會顯示有其他筆記引用。
5. **創建 meta note**。有些時候你可能會需要創建一份 meta note (也有人稱作 index note 跟 structure note) 來將相關的筆記放在一起。這對寫作或者是要整理一個主題相關的筆記相當方便。

## Zettelkasten 軟體

即使是現在是電子化時代，還是有不少人偏好用實體卡片或紙張紀錄的方式。因為習慣的關係，我暫時是沒有考慮實體筆記，如果想找參考的朋友，可以看 LessWrong 上的[這篇文章](https://www.lesswrong.com/posts/NfdHG6oHBJ8Qxc26s/the-zettelkasten-method-1)。內容很詳細然後也有列出所需的工具。

我從 Reddit 社群的 [Wiki](https://kuratoro.zettel.page/software-comparison.html) 找出比較熱門或者是我會考慮的幾個軟體。這邊我沒有列一些常見的筆記服務如 Evernote 以及 Notion，因為它們沒有直接支援上面講到的 ID 系統以及雙向連接。然後我這邊列出的軟體其實我自己都還沒深入使用過，所以下面只是我對看到的評價或是心得的總結。如果想知道更多支援的軟體可以看一下原文以及社群裡面的討論。

### Roam Research

[Roam Research](https://roamresearch.com/) 是一款強調連接的 web based 筆記軟體。用軟體的術語來解釋的話，整個筆記軟體可以看成一個 graph database，筆記裡面的一句話或者是一個段落都可以互相連接，可以説比起 Zettelkasten 的要求更加彈性。前一陣子都還限制著註冊，現在已經完全開放了。我個人認為 Roam Research 看起來非常棒，暫時沒有想試的原因是希望可以自己管理筆記檔案，而不是這種平台類的工具。

### TiddlyWiki

[TiddlyWiki](https://tiddlywiki.com/) 是一款開源的 web based 非線性筆記軟體。支援 meta programming，除了寫筆記以外還可以自己客製化筆記本的行為，擴充性非常高。當然也可以做到 Zettelkaskten 所需要的雙向連結。而且已經有十幾年歷史，社群有為數不少的外掛讓你選擇。我覺得如果是喜歡在工具上面折騰的人可以試一下。

### Zettlr

[Zettlr](https://www.zettlr.com/) 從名字就可以看出來它天生就想支援 Zettelkasten，在功能上可以把它想成一個有雙向連接以及特別在學術寫作上加強的 Markdown 編輯器。Zettlr 是開源的桌面端軟體，使用者可以自己管理在本地端筆記檔案，也能做到一定程度的客製化。我自己認為功能都十分實用，可能缺乏一些 fancy 的功能，例如將連結視覺化。但如果想要馬上開始寫作或是打造自己的 Zettelkasten 系統，我覺得 Zettlr 也是個不錯的選擇。

### Obsidian

[Obsidian](https://obsidian.md/) 是一套比較新的筆記工具，現在只有桌面端。它的介紹中就直接寫著想成為人的第二大腦。我會說它是一個更多功能的 Zettlr，例如說支援視覺化。但沒有 Zettlr 對學術寫作支援，像是整合 reference manager。一些特有的功能像是 Note Multiplexer(同時顯示多篇筆記)跟 Random note(隨機打開筆記以方便回顧跟發現新想法)，我覺得都讓 Obsidian 往第二大腦更接近了一點。明顯的缺點就是它不是開源，不過使用者還是可以自己管理檔案。

### Neuron

[Neuron](https://neuron.zettel.page/) 跟上面列舉的軟體差別比較大，它是一個 command line tool，使用者可以用來管理純文本的筆記以及生成一個展示用網頁。筆記裡面需要用 Markdown 配合一些 Neuron 語法跟 ID 來寫內容以及連接筆記。Neuron 是完全開源，Reddit 的 Zettelkasten 版也在用 Neuron 來做社群的 Wiki。Neuron 會比較適合有技術背景以及想自己管理檔案的人。

### 其它

其實現在支持的服務非常多，Reddit 社群列表就沒列到 [supernotes](https://supernotes.app/)。有心去關注社群的話應該可以找到更多。另外，如果是做軟體相關的讀者可以看看常用的編輯器有沒有支援的外掛。自己有看到 Vim、Emacs 以及 VS Code 都有一些選擇。

除了 Zettelkasten 軟體之外，有些時候你可能會需要 reference manager 來管理你所參考的資料來源。有些人也會用另外的筆記軟體來暫存還沒寫成永久性筆記的草稿。

## 實行要注意的地方

- Zettelkasten 需要時間來累積筆記。這並不是一個短時間會有效果的方法。需要持之以恆，讓筆記達到一定的數目產生乘數效應。
- Zettelkasten 只能算是大腦或者說是記憶的延伸。在我的第二篇參考資料中有引用一句話：

  > Cognitive tools only offload our cognition, but they don’t have the ability to know, think, and understand. They do extend our cognitive capabilities, but we still do the thinking. (Dror & Harnad, 2008)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;這些方法或者是說工具多多少少減低了我們一些負荷。但理解跟思考還是要靠自己來做。不要寫下你自己不理解的東西。

- Zettelkasten 也不是像 GTD 一樣的時間管理方法。不會在短期內增加你的生產力。

## 參考

1. [https://zettelkasten.de/posts/create-zettel-from-reading-notes/](https://zettelkasten.de/posts/create-zettel-from-reading-notes/) 如何整理實體書的筆記成 Zettel 的形式。
2. [https://improveism.com/zettelkasten-method-smart-notes/](https://improveism.com/zettelkasten-method-smart-notes/) 介紹為何要用 Zettelkasten、跟常見的整理系統如 Tag、Search 有何不同。也列出一些實作需要注意的地方，值得一看。作者還有在教跟 Anki 相關的課程，對相關議題有興趣的讀者可以看看。
3. [https://www.reddit.com/r/Anki/comments/gi6iep/zettelkasten_and_anki/fqcur28](https://www.reddit.com/r/Anki/comments/gi6iep/zettelkasten_and_anki/fqcur28) 如果你也有在使用 Anki，這篇留言很值得一看。他的 Workflow 有整合 Anki 以及 Zettelkasten。
4. [https://news.ycombinator.com/item?id=23386630](https://news.ycombinator.com/item?id=23386630) 蠻建議開始做之前看一下這個 Hacker News 討論串，參考一下正反兩方的意見。
