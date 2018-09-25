VerticalSelect
----

# 追記

これは、"select_lines"って機能とほぼ同等なんですが、MacだとMission Controlと被るのでkeybindを適当に変えておきましょう。

ちなみにsublime3で使うとなぜか一個ずつではなく一気に下まで選択されます。（この方が便利な気がして来た）


### 概要

カーソルを１つ下に追加できます

例えば、

```
touch data|.txt
touch data.txt
touch data.txt
touch data.txt
```

という状況（'|'はカーソルを表しています）で、VerticalSelectを３回使うと、

```
touch data|.txt
touch data|.txt
touch data|.txt
touch data|.txt
```

みたいにカーソルが増えます

おまけで、MultiNumberInsertというのも入っています

これをさっきの状況で使うと、

```
touch data01.txt
touch data02.txt
touch data03.txt
touch data04.txt
```

みたいになります


### 導入方法

1. PackageControlを入れてない場合は入れる（[PackageControle](https://packagecontrol.io/installation#st2)）
2. コマンドパレットを開いて（macなら⌘+shift+P、windowsはctrl+shift+P）「add rep」と入力してEnter
3. 「 https://github.com/snuke/VerticalSelect 」と入力してEnter
4. コマンドパレットを開いて「install」と入力してEnter
5. 「VerticalSelect」と入力してEnter
6. コマンドパレットを開いて「brow」と入力してEnter
7. 6で開いたPackagesフォルダからVerticalSelectフォルダを探して開く
8. 「Default (使っているOS名).sublime-keymap」を開いて、「"keys": ["なんちゃら"]」となってるところを好きなキーバインドに書き換える（僕はMacで"super+e"と"super+p"にしてます）

