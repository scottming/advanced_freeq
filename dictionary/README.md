## 说明

科斯林、朗高、剑桥高阶三本字典的 完整版 TXT 文件在 [base_meta.tar.xz](http://scott.imwork.net:51/scott/freeq/src/master/dictionary/base_meta.tar.xz) 这个文件里（后缀改成了html），下载后用 `tar -xJf base_meta.tar.xz` 解压。如果要测试全部数据，请下载这个，测试样本数据，请看最后。

完整版的学习词典下载链接 `链接: http://pan.baidu.com/s/1pL4HXMV 密码: hkii`，解压后安装到欧路词典即可。如果想体验下学习词典，可以安装试试。

朗高、剑桥高阶这2本词典应该算最好的入门级英英学习词典了，我想实现的大致效果是

- 命令行搜索单词，打印整个解释
- 命令行搜索词组，打印单行例子和当前单词用法

上面的两个功能，若有干净的数据做起来都不难，关键是直接反编译后的词典文件，包含太多 CSS 样式，不太熟悉，不知道怎么提取，试过 bs4 的 findall、get_text 效果不太好，单词的 Example 和解释会混掉， 参见 [这里](http://nbviewer.jupyter.org/github/scottming/freeq/blob/for_myself/ipynb/Scraping.ipynb)。

想获得的干净数据类似这个 [文件](http://scott.imwork.net:51/scott/freeq/src/master/dictionary/preview_sample.md)，测试样本数据是这个 [文件](http://scott.imwork.net:51/scott/freeq/src/master/dictionary/ldoce52_sample.html)。
