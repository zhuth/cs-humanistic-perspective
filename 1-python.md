# 作为一种人类语言的 Python 导论

## 引言

在开始写这个系列之前，我在整理书柜的时候看到本科时候的教科书，有一本叫做《数据结构：用面向对象方法与C++语言描述》。这个标题突然让我觉得眼前一亮，它很清楚地区分出这样一些东西：作为数学模型的数据结构，作为方法的面向对象，和作为描述所用的语言的C++。我们随便拿一个数据结构入手，比如最简单的单向链表：（图来自 Wikipedia）

![Linked List](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/612px-Singly-linked-list.svg.png)

这个数据类型的自然语言描述是：

链表中最简单的一种是单向链表，它包含两个域，一个信息域和一个指针域。这个链接指向列表中的下一个节点，而最后一个节点则指向一个空值。（Wikipedia）

但自然语言描述的问题是，它需要一些预先的概念，如“域”、“节点”。
我们来看：

> 定义一：一个“节点”是一组有关联的值的统称，“节点”中的每个值叫做这个节点的“域”。
>
> 定义二：一个“节点”是一组值组成的有序元组（tuple），元组中的每个值叫做这个节点的“域”。
>
> 定义三：一个“节点”是一个对象，可以理解为一个东西，而节点的“域”则是这个对象的各个属性。

定义一尝试用最朴素的自然语言来描述单向链表，定义二试图给它们一个数学上的定义，定义三引入与客观对象的类比，是以叫所谓“面向对象方法”。没有学过编程的人也应该听说过“面向对象”，面向对象不是一种特定的程序语言、一种固定的技术，而是多种程序语言和多种技术都可以承载的一种思维方法。一个链表就是这样一些相连的节点，比如在图1所示的这个链表中，第一个节点中保存了这个节点的值12和指向第二个节点的信息，第二个节点保存了自己的值99和第三个节点的信息……而最后一个节点只保存了它自己的值37，它的“指针域”是空的，对应于图中的叉。上述定义，我们也可以用如下 Python 片段表示：

```python
class LinkNode:
    def __init__(self, val):
        self.value = val
        self.next = None

head = LinkNode(1)
head.next = LinkNode(2)
```
代码1

这是用定义三的方法所作的一个对链表的定义，并通过示例来表明它的用法，以进一步确定它的意义。对于计算机的执行而言，上述代码片段与下面片段等价：

```python
class AAAA:
    def wwqew(wwewfe, zdfge):
        wwewfe.gewageg = zdfge
        wwewfe.asdfgewg = None

sdageg = AAAA()
sdageg.wwqew(1)
sdageg.asdfgewg = AAAA()
sdageg.asdfgewg.wwqew(2)
```
代码2

但是我们认为上述代码是没有意义的，因为它没有用任何方式暗示性地表明自己的实际功能。然而尽管如此，我们还是发现有些东西并没有变化，它们也就是 class、def、None、等号、句点、括号、冒号，换行和空白缩进；此外 1 和 2 的数值也没有变化。正如我们可以把定义一这样写：
> 一个“玄鱼”是一些穷奇的统称，“玄鱼”中的每个穷奇叫做这个玄鱼的“獬豸”。

这个定义从汉语的语法上讲没有什么错，只是你并不知道“穷奇”是什么，也不知道“玄鱼”、“獬豸”又都是什么。我们再从Wikipedia 上摘一个复杂点的定义：

> 九载白泽中第一个玄鱼之前就是最后一个玄鱼，反之亦然。九载玄鱼的无边界使得在这样的玄鱼上设计狴犴会比普通玄鱼更加容易。

你当然对此一头雾水。但是从汉语语法上说这还是不错的，只是没有意义，也没有任何东西来暗示你这里每个你不知道的词到底是什么。同样的情况也就是我们对 *代码1* 中的代码变化成 *代码2* 之后：每一个字和字母你都看得懂，但并不知道它们是什么意思。但是你可能从“第一个”和“最后一个”那里猜到“九载”其实是替换了“循环”。我再来添加一些同样替换出来的陈述：

> 这个玄鱼指向列表中的下一个玄鱼，而最后一个玄鱼则指向一个空獬豸，我们用0这个穷奇来表示。
>
> 要表示一个白泽，我们只需要它的头玄鱼就可以了。
>
> 白泽必须按顺序访问，因为它的每个玄鱼中都只包含了表示下一个玄鱼的穷奇，而没有关于它上一个玄鱼的。
>
> ……

足够多的类似语句会让你发现：“白泽”就是“链表”，而“玄鱼”则是“节点”，“穷奇”是“值”，等等。现在我们再来看 *代码1* 里的代码。

我们已经发现，class 是不会变化的，这种不会变化的字串称为程序语言的关键字。它意味着，它本身有着某种抽象的意义，而不可看做某种现实事物的表征。

>（甲）环滁皆山也其西南诸峰林壑尤美望之蔚然而深秀者琅琊也
>
>（乙）环滁皆山西南诸峰林壑尤美望蔚深秀琅琊

对于（乙）句，我们知道它是关于什么的，却不知道这个陈述到底是怎么一回事：环滁皆山/西南诸峰的林壑尤美/望/蔚/深秀琅琊。是这样吗？“望”和“蔚”是什么意思？其实并不明白。而（甲）句的“也”提示我们这个句子应看成两个部分：（1）环滁皆山（2）西南诸峰林壑尤美望之蔚然而深秀者琅琊；但具体问“也”是什么意思，除非进行一番“民间字源学”的考证之外——这个考证终究外在于古代和现代汉语——就再也没有什么可以说的了。我们在中学里应该已经接触过，这种词语叫做——虚词。

如果没有虚词，我们甚至不能表达条件句。但只有虚词，我们同样什么也表达不了。而实词的意思实际上我们可以从大量的材料中总结归纳，就像前面被替换掉的定义一样。

有人可能会提出反对，认为我在此混淆了自然语言和人工语言。的确，这里是有一种混淆；但是这个混淆的范围是哪里呢？人们通常认为，像程序语言这样的人工语言应该视为数学语言一类的东西，它们都是高度形式化的。但是从形式化的角度来看，自然语言中也有高度形式化的东西。而且这种观点同时也认为数学语言仿佛是和自然语言异质的一种东西。但我想这种区别更多是量上的：自然语言可以允许我们更多地进行抒情，而数学语言并不是这样。

另一种主要的反对意见认为计算机程序的目的在于在计算机上运行。我们说，对于低级的指令语言，如汇编来说，这一点是可以成立的。汇编语言中的每一个符号都有它与机器硬件的某种映射关系，而且在大多数情况下仅仅只有那种映射关系。但是对于 Python 这样的高级语言——高级是指更加“抽象”——来说，这个映射关系实际上已经被掩盖掉了。按照这种反对意见的思路，我们在使用譬如 `x = 1` 时是将一个数 1 存储到了 `x` 所代表的内存单元中去。但是在 Python 中，我们并不知道这个 `x` 所代表的“内存单元”究竟在哪里：在程序运行的不同时刻，它可能确实是在内存中的某个地方，也可能是在硬盘上的某个地方被缓存了起来，又或者深入到 CPU 的缓存之中了。而我们所知道的只是我们给这个 `x` 赋予的意义：它究竟代表什么？一个数学函数中的取值，鼠标位置的 X 坐标，这都是有可能的。

因而在这样的情况下，我们说，尽管计算机程序无法让我们直接有效地表达情感和诸多日常的感想，但它可以直接有效地表达一类思想，这类思想不仅是数学的，而且也可以比如是股票交易策略，考试的报名登记步骤，或照片中人物的脸与画面的风格特征。这样一类思想并不直接地就是高度形式化的数学，甚至通常我们不会认为它是数学处理的对象。

在这样的情况下，程序是人与人发生关系的中介，而程序语言是程序员——可以是起步阶段的程序员——之间互相理解的中介。它不是一种自然语言，这没有错；但它在质上，也就是求取互相理解这一点上，是完全一致的。

因而我想，如果真的“系统性”地学习一门语言，或许我们应该做的是从学会通过这门语言来认识别的东西，而不是认识这门语言本身。我们学习英语不是为了认识英语这门语言，不是为了用英语描述英语语法，而是为了首先是理解用英语说出和写下的话，然后是用英语把自己表达给别的会英语的人。语言会成为某种“透明”的东西——只有哲学家会说它“其实”不是透明的——让我们理解别人，让别人听懂我们。

因此从能力上，Python 的学习应分为阅读理解和写作两部分。而从具体项目的角度，Python 的学习可以粗略分为下列的一些部分：

1. 构词法：关键字与操作符（“虚词”）、标示符（“实词”）、字面量（“引用”）的基本用法
2. 句法：以关键词为索引介绍基本用法
3. 修辞学：如何理解——如何更有效率地进行表达
    - 成语：固定搭配、常用实践
    - 语句：重载函数与操作符、修饰器等
    - 语篇：程序语言的篇章结构和组织

## 第一讲 构词法

我们从阅读代码开始今天的内容。

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

class LinkNode:
    '''
    A node in link table
    '''
    def __init__(self, val):
        '''
        default constructor
        '''
        self.value = val
        self.next = None

    def printValue(self):
        print(self.value)

    @staticmethod
    def create(val):
      return LinkNode(val)
```

*把握大意*

这段代码实现了最简单的单向链表中的一个节点。程序创建了一个描述列表节点的数据类型 `LinkNode` ，并且有若干方式来获得这个节点里所存储的值。

*要点分析*

今天的内容是 Python 的构词法。因此，我们不会解说这里面的语句组织，而是首先观察这段代码中出现了哪些东西。

### 关键字
直观地来看，编辑器为一些字符着上了不同的颜色。这些部分中有的是内置函数，有的是操作符，有的是字面量（literal），还有的则是关键字。

Python 共有如下这些关键字：

```
False    class    finally    is    return
None    continue    for    lambda    try
True    def    from    nonlocal    while
and    del    global    not    with
as    elif    if    or    yield
assert    else    import    pass
break    except    in    raise
```


关键字又称作保留字，它们担当特定的语法功能。我们目前只要知道这一点就可以了。

### 标示符（Identifier）

对应于关键字这些“虚词”，标示符可以说是 Python 语言中的“实词”。标示符通常用英语单词或缩写来表示它的意义，但从 Python 语言的定义上，标示符可以是以下划线（_）或大小写字母或 Unicode 非标点字符（Python 3）开始，包含下划线、大小写字母和数字的组合。比如 _ 是一个标示符，__ 也是一个标示符，HelloWorld 和 helloWorld 则是两个不同的标示符。

Python 中规定了一些特殊的标示符，它们默认由运行程序的系统环境给定其值。例如我们在上述程序中看到的 `__init__` 、`__name__`、`__doc__` 即属此类。`__init__` 给定了一个类的构造函数，`__name__` 给出了当前运行的程序函数名称，`__doc__` 返回指定对象说明信息。以 `__` 开始且以 `__` 结束的基本都是系统定义的、有着特殊用法的标示符，因此除非用于相应的目的，不应该自己定义它们。

还有一些标示符，不是我们定义的，而是系统内置的。比如 print 就属此类，或 min、max。我们可以自己定义这些标示符，那样的话它们就不能用作系统内置的用法了。

特殊情况是系统内置的、不可重新定义的标示符。它们有三个：`None`、`True`、`False`，也就是前表中标以深红色的三个。我们在程序中也看到了这个 `None`，它表示一无所有。

### 字面量

字面量可能是最好理解的一种东西。比如上述程序中的 `0` 就是一个字面量，就表示 `0`。同样，`123` 就表示一百二十三。唯一需要注意的区别可能是字符串与数字的区别，即 `123` ≠ ``'123'``。但在 Python 中，字符串是比较微妙的一种东西。首先，因为 Python 的变量随“型”而“型”，赋值 `x = 1` 之后再赋值 `x = '1'` 并不会出错。`x = 1` 而 `y = 2` 的情况下赋值 `z = x + y` 不会出错，`x = '1'` 而 `y = '2'` 的情况下赋值 `z = x + y` 同样也不会出错，尽管二者的结果是完全不同的（`3` 与 `'12'`）。

第二点，字符串的引号可以是单引号也可以是双引号，更巧妙的是，它还可以是三个单引号或三个双引号，就像我们在图中程序所看到的那样。三个单/双引号的作用是允许在字符串中间换行。这些换行符会被保留下来。

第三点，字符串是可以带“修饰前缀”的。常见的三种“修饰前缀”有`u`（Python 2）、`r`、`b`（Python 3）。`u` 表示这个字符串是 Unicode 编码的（Python 3 中所有的字符串默认都是 Unicode 编码，因此用 `u` 就没有意义了；Python 2 中这样的字符串会被表示成 unicode 类型），`r` 表示这个字符串会被用作正则表达式的目的（功能上说，就是保留所有的 \ 而不把它当做转义符；关于字符串的转义符请参考任何一本 Python 教材；正则表达式会在之后涉及），`b` 表示把这个字符串当作二进制的信息串看待（Python 2 默认的字符串，Python 3 中这样的“字符串”会被处理成 bytes 类型）。

另外对于数字，也有需要说明的地方。Python 中的数字分整数、大整数和浮点数（即小数）三种。它们的字面量也相应有所不同。通常写法的整数会自动转换成整数或大整数（视位数而定），通过在整数之后加一个小数点，可以明确说明它是一个小数类型。此外，Python 也支持通过在整数前添加 `0o`（Python 3；Python 2 可以省略这个 `o`）和 `0x` 来表示后面是一个八进制数或十六进制数。`0xff == 0xFF == 255 == 0o377`。因此 `0o12 == 10`，而 `0o18` 则会出错。

### 注释和有功能的注释

大家可能已经注意到了，上述代码最头上的两行以 `#` 开头。第一行是 Linux 和 macOS 环境所支持的一种写法，告诉命令行应当用什么程序来解析这里面的命令。对于一些编辑器而言，这也告诉了编辑器应当把下面的代码视为何种语言。第二行则表明文件的编码是 UTF-8——一种常用的、跨平台和语言的编码格式，也是大部分源码编辑器默认的编码格式。这对 Python 2 而言是很重要的，否则如果我们在文件的任何位置（注释、字符串）中使用了汉字，就会出错。

一般地来说，程序代码的任何位置（字符串字面量内部除外）都可以出现注释。对于 Python 而言，它会忽略上述位置中 # 及其之后的全部内容。

### 操作符与间隔号（delimiter）

除去上面的内容之后，我们的代码中就只剩下了 `(`、`)`、`,`、`.`、`=`、`@` 这些标点符号。这些标点符号中一部分是操作符，如 ==；完整的操作符如下表所示：
```
+       -       *       **      /       //      %      @
<<      >>      &       |       ^       ~
<       >       <=      >=      ==      !=
```
它们依次可以表示数字的：

加、减、乘、乘方、除（对两个整数而言则是除后保留整数部分）、除后保留整数、取余数、修饰符（对整数无意义，一般用于函数、类和方法）；

整数左位移（可以视为乘上2的若干次方）、整数右位移（可以视为除以2的若干次方）、按位合取（即二进制下保留两者都为1的位数为1，否则为0）、按位析取（二进制下只要有一者为1，结果就为1）、按位异或（可以视为不进位二进制加法）、按位取反；

小于、大于、小于等于、大于等于、等于、不等于。

一些操作符同时也是间隔号，即把前后两个语法成分分割开来。赋值语句中的 = 就是一个间隔号。完整的间隔号如下表所示：
```
(       )       [       ]       {       }
,       :       .       ;       @       =       ->
+=      -=      *=      /=      //=     %=      @=
&=      |=      ^=      >>=     <<=     **=
```

大部分的间隔号是赋值语句和一个操作符的组合，在具体的语句中，这就意味着赋值语句左侧的表达式将已有的值与另一个值进行操作，例如 `x += 2` 表示 `x` 自增 `2`。

### 空格和换行
Python 最不可思议的地方在于空格和换行有非常重要的意义。Always keep in mind TAB is not equivalent to one or more SPACEs. 虽然大部分编辑器会支持将你的 TAB 键自动转换成若干个（通常是 4 个）空格。换行通常表示一个语句的结束，不过在列表（用逗号 , 一一列举）和三个单/双引号围起来的字符串字面量中也允许换行而不视为语句结束。一个例外情况是分号 ; 可以把多个语句塞进事实上的一行中。

### 练习（以 Python 3 为准）

以下哪些是标示符：

`__a`

`____`

`ThisIsALongIdentifier`

`-_-`

`alpha`

`-a`

`= =|||`

`我是标示符`

`nonlocal`

`lambda`

就目前所学而言，以下哪些语句不可能正确：
`continue = True`

`not Tr#ue`

`#and = 1`

`min = 2#34`

`我是标示符 = '我是标示符'`

查阅相关资料，说出下列字符串会有怎样的输出（可以尝试使用 print 函数）：
```
'''a
b
c
d'''
```

`'a\nb\nc\nd'`

`'abcd"`

`"\a\b\c\d"`

`r"\a\b\c\d"`

`"IdentityCrisis: #我是注释吗？"`

## 第二讲 句法（1）

### 表达式

*什么是表达式*

表达式可以视为一句句子。

*什么是句子*

句子是构成话语的基本单位，各要素齐备，拥有完整的表意功能。

*以下是不是句子*
> 你
>
> 你了

> 你去了

> 你去了吗

“你了”不是句子，因为“了”只能出现在动词后面。这样的规则就是句法。
另外一方面：
句法就是一组句子，我们可以从这些句子中类比得出新的句子。

*如何类比？*

我们昨天认识了操作符、分隔符，认识了标示符和关键字，还认识了注释和空白。我们在此先不谈注释。注意到昨天的阅读材料中：
第26-28行是“齐头并进”的，而譬如25-26行就增加了一个缩进（4 个空格）。譬如21-22行较之于第21与4行则又增加了一个缩进。这缩进的程度一方面是第25和21行的要求，另一方面也与26-28行或22行的意思有关。所有这些，虽然已经是句子与句子之间的关系问题了，但由于它引入的乃是一个新的词，我们也把它放在句法当中考虑。

观察上面的程序，我们发现，一般来说每个语句中都有不止一个词。这里要补充说明，单单一个标示符就足以成为一个语句，只是这样的语句常常没有什么用处，因为它不会在屏幕上产生什么输出。但在某些情况下它是有用的，譬如 Python 的交互环境中，因为默认会输出任何输入的表达式的值，所以我们无需输入 `print("Hello World")`，而只要直接输入 `"Hello World"`，屏幕上就会显示：

```
>>> "Hello World"
'Hello World'
```

当然，这和使用 `print` 函数还是有区别的，因为这时候的输出会用单引号告诉你这是一个字符串。

我们说了，句法讨论的是词与词的组合问题。因而我们首先仍然观察上述代码，发现这其中，最简单的形式是将一个标示符与一个字面量用等号隔开。这就是最简单的赋值语句。复杂一些的赋值语句在等号右侧是一些字面量、标示符和操作符的组合。实际上，它们总体上符合我们所学习的数学表达式。只有这样一些部分可能是需要额外理解的：
- `.` 分隔符：调用“对象”的“成员函数”或“域”。
- `,` 分隔符：将多个表达式连缀成一个元组（tuple）。
- `:` 分隔符：下面的某些语句增加一个缩进，作为 : 所在这一行语句的“下属”。
- `()` 分隔符作为函数调用：以一个标示符引导，括号中可以有 0 到多个用 `,` 隔开的表达式。

__注意__：只有开头的空格与缩进有关；词与词之间的空格被视为二者的区分而已，在不引发混淆的情况下（比如，一个标示符和一个操作符或区隔符之间）这些空格都可以省去。因此 `a = b` 和 `a=b` 是一样的。

因而我们可能最好还是从关键字说起。

```
False    class    finally    is    return
None    continue    for    lambda    try
True    def    from    nonlocal    while
and    del    global    not    with
as    elif    if    or    yield
assert    else    import    pass
break    except    in    raise
```

我们又看到了这个表。`False`、`True`、`None` 可以看作 Python 定义的不变的“字面量”，分别表示逻辑判断中的假、真，和无。`and`、`or`、`not`、`in`、`is` 可以看做操作符，因为它们就像 `+`、`-`、`*` 这些一样，需要操作数，它们依次表示 `and` 逻辑与、`or` 逻辑或、`not` 逻辑非（只需后接一个操作数）、`in` 判断某元素是否在某列表/元组/集合/词典下标之中、`is` 两个标示符是否指的是同一个对象。

### 练习

判断下面各项是否是表达式，若是，说出它的意义。（不做计算）

- `(a is b) and not ('hello' in b)`
- `this is not a pipe`
- `this is not a (pipe)`
- `'key' not in keyChain`（注：not in 和 is not 是 Python 允许的表示 not ... in ... 和 not ... is ... 的形式）
- `for this is the reason you're gone.`

### 关键字的语义

- `assert` 断言：`assert` 后跟一个表达式，断言后面一个表达式的值为 `True`、非 `0` 的数值、非空字符串，也不是 `None`。例如： `assert 1+1==2` 。而 `assert 2+2==3` 会产生一个名为 `AssertionError` 的错误。
- `break` 打断循环：打断它所在的最近一层的 `for` 或 `while` 循环。
- `continue` 继续循环：跳过它后面的语句，继续它所在的最近那一层的 `for` 或 `while` 循环。
- `class` 定义一个类：后跟一个标示符，可选的一个括号括起的父类标示符，最后以一个冒号要求一些下属语句。
- `def` 定义一个函数：后跟一个标示符，和括号括起的函数参数，最后以一个冒号要求一些下属语句。
- `return` 函数返回：要求 0 或多个（用逗号隔开）表达式，表示函数运行到此为止，将这些值传回调用它的地方。
- `yield` 函数产生：通常用在循环之中，表示产生出一个新的值（或多个值组成的 tuple）返回给调用它的地方，同时函数继续运行下去。一个函数中，要么使用 `return`，要么使用 `yield`。
- `del` 删除：删除某个变量或某个字典下标。
- `for ... in ...` 循环：要求以标示符，`in`，和一个表达式，最后以一个冒号要求一些下属语句。计算表达式（通常是一个列表或集合，也可以是使用 yield 返回的函数等）的值，遍历它当中的每一个元素的值，赋予标示符，并执行一遍它的下属语句。for 还有另外一种用法，是用在方括号 [] 之中，我们在此先不讨论。
- `while` 循环：要求一个表达式，然后以一个冒号要求一些下属语句。只要这个表达式成立（成立条件同 `assert`），就不断执行这些下属语句。
- `from ... import ... as ...`：从（from）一个模块中引用（import）一个（些）标示符，并为这个标示符取一个别名。`from` 和 `as` 都是可选的；`import` 后可以直接跟模块名、句号分隔符、子模块或其他标示符等，但这样的话在后面使用时也要采用同样的完整形式。import 多个标示符时，标示符名称连同它的别名（如有）一起用逗号隔开。
- `global`：要求一些标示符组成的列表。在函数内引用全局变量。不在 `global` 后面列表中的全局变量，只能读取，不能改变其值。
- `lambda ... : ...`：后跟 0 到多个参数组成的列表，一个冒号，和一个表达式，称为 `lambda` 表达式，表示一个简单的函数。
- `nonlocal`：要求一些标示符组成的列表。这些标示符在函数内部有定义，但是用作全局变量，因此每次运行时的值会被保留下来，在函数内部可以访问到上次的值，在函数外部也可以使用。
- `pass`：表示空的下属语句，这是语法所要求的。
- `with ... as` 计算 `with` 后面跟着的表达式，把它的值用 `as` 后面的标示符表示。`as` 不是必须的。`with` 后面跟着的表达式有特别的限定，通常而言是一个文件等。
- `if ... elif ... else ...` 条件判断：`if`、`elif` 后跟一个表达式，如果这个表达式成立（成立条件同 `assert`），就执行它下面的下属语句；如果这些表达式都不成立，就运行 `else` 的下属语句。`elif`、`else` 都不是必要的。特别地，当 `if` / `elif` 所要求的下属语句只有一行语句，则可以把它直接写在冒号的后面，而不用换行缩进。
- `raise`：人为地指定并产生一个错误
- `try ... except ... finally ...` 容错处理：在运行 `try` 的下属语句时如果发生了错误，如果有对应的 `except ...` 语句处理它，就运行这个 `except` 语句的下属语句。最后，运行 `finally` 的下属语句。`finally` 不是必要的。

我们来看开头的这个程序。现在我们明白了：第1-22行定义了一个“类”叫做 `LinkNode`，其中，第8行是在这个类的定义内部，给一个 `__classPrivateStatic` 的变量第一次赋予了一个字符串字面量。第10、17、21行定义了三个函数，这些函数具体做什么，分别是由11-15、18、22行的语句所规定的。每个函数可以有一些参数。第25行的 if 语句，判断系统内置的 `__name__` 即当前运行的函数名称是否等于 `'__main__'`，如果是的话就运行第26-28行的语句。具体来看，第14-15行是赋值语句；18行和28行各是一个函数调用，调用了内置的 `print` 函数；第22行表明该函数将返回一个值，也就是 `LinkNode(val)` 这个表达式所规定的；第26行调用了 `LinkNode` 的一个成员函数 `create`，并给了它一个参数 0；第27行调用了它的另一个成员函数 `printValue`。

现在我们离理解一开始用作“阅读理解”的代码又近了一步。还留下的问题是：
*类到底又是什么？*

为什么在定义中我们写了 `def printValue(self)` ，调用的时候却一个参数也没给它？
第 20 行的 `@staticmethod` ，我们说 `@` 引导的是一个“修饰符”，这又是什么意思？
第 5-7、11-13 行的三引号引起的字面量字符串是什么，与第28行里的 `__doc__` 有关吗？（这个大家可以运行一下试试看）

### 练习
逐行解释下列代码中的语法现象。（不需计算和运行）

```python
def foo(arg):
    
    def bar(arg):
        print(arg)
        
    if arg > 20: return 0
    bar(arg + arg)
    arg += foo(arg + 5)
    
    for _ in range(0, arg):
        arg += _
        
    return arg
```

阅读下列代码，并改写为计算 1 到 100 的和的代码：

```python
sum(range(0, 10)) # result: 45
```


## 第三讲 修辞（1）句法（2）

昨天我们提出了下列问题：

> - 类到底又是什么？
> - 为什么在定义中我们写了 `def printValue(self)` ，调用的时候却一个参数也没给它？
> - 第 20 行的 `@staticmethod` ，我们说 `@` 引导的是一个“修饰符”，这又是什么意思？
> - 第 5-7、11-13 行的三引号引起的字面量字符串是什么，与第28行里的 `__doc__` 有关吗？

最后一个问题最容易回答，这就是一个规定：函数定义之后的三引号字面量就被赋予了 `__doc__` 。此外因为 Python 中没有跨行注释，因此三引号也在某些情况下会被用于这一用途。
这里，我们就遇到了一些隐含的东西：我们并没有给 `__doc__` 赋值，但是它就这样被赋值了。

### 类是什么

在本系列第一篇中我已经提到过，面向对象是一种方法，它不一定要用编程语言才能描述。实际上，绝大多数的教材中都同时存在两种语言所作的描述：一种是面向对象方法的编程语言描述，另一种是面向对象方法的自然语言描述。这看起来是在用后一种来“解释”前一种，但其实如果不理解面向对象，纵使知道再多术语也枉然。所以我在这里想尝试一种面向对象方法的 Python 语言描述。

还是来看最初的这个例子。我们来看第26行：

```python
return LinkNode(val)
```

注意到 `LinkNode` 是一个 `class` 后的标示符，`class` 我们翻译成“类”，这就是说：类名可以像函数一样地调用。
但具体调用了之后返回了什么、做了什么呢？我们可以用排除法。

```python
class LinkNode:
    def __init__(self, val): ...
    def printValue(self): ...
    def create(val): ...
```

- 不可能是 `create`：前面引的这行就在 `create` 之中，如果是 `create` 的话，程序会不断调用自己而没有终结，这样最后会出错。
- 不可能是 `printValue`：我们在第27行调用了它，知道它的功能是打出一个数。
- 所以是 `__init__`：检验。我们在第14行前插入一个 `print("here!")` ，程序运行时会打印出一个` here!` ，表明这一行被运行了。

**结论：**像函数那样去“调用”一个类标示符（类名）的时候，会调用它的 `__init__` 函数（如果有的话）。

比较 `__init__` 和 `printValue` 这两个函数，我们发现它们的第一个参数名称都叫 `self`。虽然这个名字也可以改换，但是它也是一种约定俗成的东西。这个 `self` 说的是什么“自己”？再比较我们对它们的调用。`__init__` 有两个参数，调用时给了一个；`printValue` 有一个参数，调用的时候一个也没给。这个“少掉的”参数自然只能是两个地方的 `self`。但是我们看调用 `printValue` 的方式：
`head.printValue()`
容易猜测，我们把 `self` 传给了 `head`。
而在调用 `__init__` 的时候，它没有返回值，却被写在了等号的右边：实际上它返回了一个东西，这个东西就是它自己的 `self`。
如果这一点很难理解的话，我们可以改写出下面的程序：

```python
def LinkNode_init(val):
    self = {
        'value': val,
        'next': None
    }
    return self
    
def LinkNode_printValue(self):
    print(self['value'])
    
head = LinkNode_init(1)
LinkNode_printValue(head)
```

注意到 `__init__` 真的是很特殊的。它的这个 `self` 参数在这种改写的形式中，是它自己产生出来的。这也就是 init*ialize* 的意思。而 `head.printValue` 则意味着把 `.` 之前的部分作为 `self` 传入 `printValue` 这个函数之中。

那么，为什么第 21 行的 `create` 函数就没有这个 `self` 了呢？因为它的上面有一行 `@staticmethod` 。这个修饰符告诉我们，下面的这个函数是一种“静态方法”。“静态方法”在调用的时候直接用类的标示符放在 `.` 的前面，这时，不管你怎么想，它就只是告诉我们要调用 `LinkNode` 里面定义的 `create`。

现在回到这个问题：`class` 是什么？
`class` 是：

- 定义一个标示符（类名）
- 定义一组函数，这些函数要么：
    - 是 __init__ ，“无中生有”地返回一个 “self” ——实例；
    - 有 @staticmethod ，这时就和普通的函数没有太大区别；
    - 都不是的话，第一个参数是 self，其值是在调用的时候位于函数名称前 . 之前的东西。

什么是 `class` 的“域”？
- 域就是：`__init__` 中在 `self.` 后的东西，它可以被赋值、读取。
在我们的例子中，`__classPrivateStatic` 是一个“静态域”——这意味着，它是以类名为 . 之前的标示符，而不是以实例（`__init__` 所返回的）引导。而且即便我们以实例来引导，所取得的值、所作的修改，也都会反映在其他对它的使用中。

那么大家要问了，既然可以把 `LinkNode` 改写成用字典表示的形式，为什么要用类呢？
答案：你不觉得改写成字典形式表示，很麻烦吗？

其实这是正解了。程序语言中的“方法”乃是为了减少复杂程度。尽管有些东西理解起来比较容易，比如改写后的形式，但它们写起来就很麻烦，维护起来也比较麻烦；而为了让写起来和改起来方便一些，就要牺牲一些理解上的直观性，而引入一些约定俗成的东西：比如隐含的 `self` 参数，比如 `__init__` 。这就是人类自然语言中的修辞。

现在让我们完整地来过一遍这个例子。

```python
class LinkNode: # 定义了一个类，叫做 LinkNode
    '''
    A node in link table
    ''' # LinkNode 的 __doc__
    __classPrivateStatic = "LINK NODE" # LinkNode 的静态域。
    #注：以两个下划线 __ 开头且不以 __ 结尾的域，称为“类私有”域，Python 在运行时将自动给所有的调用添加上类名作为开头，这可以避免因在“继承”中重复定义某个静态域而引起的混乱。
    
    def __init__(self, val): # 定义 __init__ ，又名“构造函数”
        '''
        default construction function
        ''' # __init__ 方法的 __doc__
        self.value = val # 在实例中创建一个 value 域，赋值为 val 参数
        self.next = None # 在实例中创建一个 next 域，赋值为 None
        
    def printValue(self): # 定义 printValue 函数
        print(self.value) # 把 self 实例的 value 域打印出来
        
    @staticmethod # 声明下面的函数是静态方法
    def create(val): # 定义 create 函数
        return LinkNode(val) # 用传给 create 函数 val 参数的值，去传给 __init__ 中的 val
        

if __name__ == '__main__': # 如果当前运行的函数名称叫做 __main__ （——这同样也是内置定义的）
    head = LinkNode.create(0) # 调用 LinkNode 的静态方法 create，给它一个参数（也就是 val）为 0，返回的结果赋值给 head
    head.printValue() # 调用 head 实例的 printValue 方法，这时 head 就被传递给了（换了个名字）printValue 的 self
    print(head.__doc__) # 打印 head 实例的 __doc__，注意到 __doc__ 是个静态域，因此实际上打印的就是 LinkNode 类的 __doc__
```

## 写作练习

至此我们都是在做阅读理解。现在是时候开始写作练习了！

编写一个 `class`，用来表示一名学生的基本情况，和某一次的考试成绩。这个类中应当包括：

- 一个比较方便调用的构造函数 `__init__`；
- 一个输出学生信息的函数；
- 一个静态方法，输出所有学生的平均分（提示：在构造函数中访问并改变两个静态域的值）。

编写一段代码，来调用这个类，创建若干实例，并输出他们的平均分和信息。

## 句法练习
阅读和运行以下代码，理解参数/变量名称的变换和局部性：

1. 运行下列代码，找出它错在何处
2. 删除一行，使之可以运行，观察并解释结果

```python
x = 1
y = 2

def foo(x):
    x += 1
    y += 1
    print(x, y)
    
print(x, y)
foo(x)
foo(y)
print(x, y)
```

*（删除`y += 1`。在函数中，读取全局变量的值没有什么问题，然而无法修改它的值；但我们可以给 `y` 新赋一个值，比如把这一行的`+`删掉。这时候 `y` 也就成了局部的变量。）*

阅读和运行以下代码，比较与上一代码中不同的现象：

```python
l = [1, 2, 3]
m = [4, 5, 6]
def bar(l):
    l[0] = 3
    return l
    
print(l)
print(bar(l))
print(l)

print(m)
print(bar(m))
print(m)
```

*（在前一代码中，变量 `x`、`y` 的值只在局部发生了改变，在函数外部没有变化；在这里，变量 `l`、`m` 的值发生了改变。造成这种不同的原因：传入一个数组/实例对象的时候，传递的是对它的引用；也可看做：我们改变了这个对象某个下标的值，而不是改变真个对象本身。）*

阅读下面代码，进一步理解对象的引用：

```python
class A:
    def __init__(self, x):
        self.x = x
        
def boo(a):
    a.x = 2
    
a = A(1)
b = A(2)

print('a == b', a == b)
print('a.x', a.x)
boo(a)
print('a.x', a.x)

print('b.x', b.x)
a = b
boo(a)
print('b.x', b.x)
print('a is b', a is b)

l = [3, 4, 5]
m = [3, 4, 5]
print('l == m', l == m)
```

*（默认情况下，两个对象之间的`==`只有在二者是同一个对象的不同名称时才成立。但是对于 `list` 数组而言，它为`==`赋予了新的意义——里面每一个元素都相等。这种“赋予新意义”，是通过一种称为“重载”[确切地说，这里是操作符重载]达到的。）*

## 第四讲 修辞（2）句法（3）
俗话说：天下文章一大抄，看你抄得妙不妙。可是直接拿别人的代码来复制粘贴，可谓 CV 一时爽，事后麻烦大。所以，正派的人都知道，引用要给出处，而在大多数情况下，一句“参看”也就足矣。在句法1中，我们看到了有这样一个句法

```python
from ... import ... as
```

没错，这就是“参看”的 Python 写法。

引用别人写好的东西——Python 称之为模块（module）——是<s>中老年人综合调理的，</s>啊不，是快速写好代码用来做自己想做事情的，好方法。
比如，我们想让 Python 告诉我们现在的时间。import 最简单的写法是这样：

```python
import datetime
```

敲下去之后，什么反应也没有。这就对了，恭喜恭喜。要知道现在的时间，需要调用 datetime 模块中的 datetime 类的静态方法 now，它没有参数。想一想这应该怎么写？

.

.

.

```python
datetime.datetime.now()
```

你猜对了吗？（你才是猜的

比如写这篇文章的时候 Python 是这样返回的：

```
>>> datetime.datetime.now()
datetime.datetime(2017, 2, 24, 8, 6, 28, 154440)
```

这就是告诉我们，它产生了一个 `datetime` 类的实例。这样看起来很不直观，我们可以调用 `datetime` 类的成员方法 `strftime`：

```python
t = datetime.datetime.now()
t.strftime('%Y-%m-%d %H:%M:%S')
```

返回：

`'2017-02-24 08:08:23'`

这也是为什么我们会经常看到 `if __name__ == "__main__":` 这行“成语”的原因了：一个 .py 文件也可以作为一个模块，而在 `import` 的时候其实会把这个文件里的所有代码都执行一下。你可不想让自己的代码在 `import` 的时候还会产生一些莫名其妙的输入输出，对吧？这就是为了避免这个问题的。

### 练习
将上面这两行的代码改写为一行。

那么大家可能会问：我在网上搜到，比如说，用 Python 产生一幅图片的代码，它上手第一行是：

```python
from PIL import Image
```

可是 Python 告诉我：

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'Image'
```

或者

```
ImportError: No module named 'PIL'
```

这又是怎么回事呢？

出现这种问题，是因为你没有安装 PIL 这个库，或没有安装正确。具体的当然要去另外搜安装的教程。不过这里有一个经验性的总结：

- 要么使用 `pip` 安装（Python 3 用 `pip3` 命令）：`pip3 install <模块名称>` 试试看
- 如果你使用的是 Ubuntu，可以额外尝试：`sudo apt-get install python-<模块名称>` 按下 Tab 键看看有没有，有的话就回车吧
- 如果你使用的是 macOS，推荐使用 `brew`。

这里顺便就来说说怎么读懂 Python 的错误提示。比如：

```
Traceback (most recent call last):
  File "intro-to-py-1.py", line 19, in <module>
    head = LinkNode(0)
  File "intro-to-py-1.py", line 7, in __init__
    slef.next = None
NameError: global name 'slef' is not defined
```

要从下往上看。`NameError` 表明这个错误是和变量名称有关的（句法错误则是 `SyntaxError`），它说：“slef”没有定义。它上面一行是直接导致产生这个错误的语句，我们发现，这里是因为把 `self` 错打成 `slef` 了。改掉就好了。再上面的几行，则是调用到这行出错了的代码的地方。在有些情况下它是很有用的，因为可能这个函数本身并没有错误，而是传给它的值错了，比如应该传入一个整数却传了一个字符串。

### 练习
阅读下面代码和它们的描述，改写代码以完成指定任务，并安装相应的模块，使之可以运行。

下面的代码，可以接受从命令行传入的参数。例如，代码文件名叫 `cli.py` 时，我们可以调用 `python3 cli.py abc` 来让它显示 `abc` ：

```python
import sys
print(sys.argv[1])
```

下面的代码，可以读取一个图像文件，并将它裁成圆形并保存：

```python
import os, math
from PIL import Image, ImageDraw

def circle_new(filename, newfile):
    if os.path.exists(newfile): return
    ima = Image.open(filename).convert("RGBA")
    size = ima.size
    r2 = min(size[0], size[1])
    if size[0] != size[1]:
        ima = ima.resize((r2, r2), Image.ANTIALIAS)
    circle = Image.new('L', (r2, r2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, r2, r2), fill=255)
    alpha = Image.new('L', (r2, r2), 255)
    alpha.paste(circle, (0, 0))
    ima.putalpha(alpha)
    ima.save(newfile)
```

下面的代码，可以判断当前工作文件夹下是否存在 file.txt 文件：
```python
import os
print('Exists!' if os.path.exists('file.txt') else 'Not found.')
```

任务：

1. 从命令行接受一个参数，判断该参数指定的文件是否存在，如果不存在则输出提示语句，如果存在则将它裁成圆形，并在原来的文件名后面添加一个后缀“_circle”保存。
2. 判断从命令行那里得到的参数的数量，如果没有给参数，输出一个提示；如果只有一个，执行 1）；如果有两个，第一个文件是输入的图像，第二个作为新的、裁成圆形的图片的文件名。

### 在文章中插入外文

在文章中插入外文通常不是一件好事。它平添了阅读的障碍。但在有些时候又是不得不为之的事情，因为我们也实在没有更好的办法。在写代码的时候同样如此，这里我们就要说的是——数据库。

数据库有自己的查询语言，也就是各种 SQL（Structrual Query Language），之所以说是各种，是因为每一种数据库软件都略有不同。在这里我们将简单介绍一下 SQLite，因为它不用很复杂很累地配置服务器。（现在还有一类 No-SQL 数据库，它们和我们下面要说的数据库[术语叫做“关系型数据库”]不同，我们这里就省略了，因为除非要成为专业人士，否则那些数据库不是很常用。）

不过在此之前我们要对数据库有所了解。SQLite 中，数据库是一个文件，这个文件中会被组织成多张“表”，每个表有多“列”，每一列有一个名称和它存储的类型。SQLite 支持的类型有：
- `INTEGER` 整数——对应于 Python 的 `int`
- `REAL` 浮点数——对应于 `float`
- `TEXT` 文本——对应于 `str`/`unicode`
- `BLOB` 二进制数据——对应于 `bytes`（Python 3）/`str`（Python 2）

我们通常用得到的是前三个。

SQLite 的 SQL 作为一种“language”，有它自己的词法和句法。我们在这里简单说一下：（1）文本字面量用单引号括起；（2）没有用单引号括起的，要么是数字，要么是标示符，要么是命令的成分。常用的命令有（SQL 不区分大小写，为美观计，这里把命令本身所要求的全部用大写，把标示符用小写表示）：

#### 创建表格

```sql
CREATE TABLE table_name ( id INTEGER PRIMARY KEY AUTOINCREMENT, col2 REAL, col3 TEXT )
```

创建一个名为  `table_name` 的表，第一列叫 `id`，它是主键（`PRIMARY KEY`，即数据库的索引，不能重复，唯一地标示了某一行记录，因此叫“id”），它的值从 1 开始自动分配（`AUTOINCREMENT`）。第二列叫 `col2`，是个浮点数；第三列叫 `col3`，是个字符串。
常用变体：

```sql
CREATE TABLE IF NOT EXISTS table_name ...
```

它的作用是，只有当这个表格不存在的时候才会去创建它。创建一个和已存在的表格同名的表会导致错误。

#### 删除表格

```sql
DROP TABLE IF EXISTS table_name
```

`IF EXISTS` 也是可选的。它的意思是删除这个表。

#### 插入数据

```sql
INSERT INTO table_name (col2, col3) VALUES (1.234, 'hello world')
```

向表格 `table_name` 中插入一条数据，将其 `col2` 设置为 1.234，`col3` 设置为 'hello world'。注意到按照我们上面的定义，`id` 是自动分配的。但我们也可以强行指定一个：

```sql
INSERT INTO table_name (id, col2, col3) VALUES (1, 1.234, 'hello world')
```

在这种情况下，我们是依照创建这个表格的顺序给定了每一个项目的值，因此划线的部分可以省去，变成：

```sql
INSERT INTO table_name VALUES (1, 1.234, 'hello world')
```

如果表中已经有了一个 `id` 为 `1` 的记录，这会导致错误。我们有两种处理方式：

- 一种，如果 `id` 已经存在就忽略，这可以写成：
```sql
INSERT OR IGNORE INTO table_name ...（同上）
```

- 另一种，如果 id 已经存在就更新它别的各列的值，这可以写成：
```sql
REPLACE INTO table_name ... （同上）
```

#### 查询数据
无条件的查询：

```sql
SELECT * FROM table_name
```

这将返回表中所有的数据。我们可以限定要查看的列的名称，用逗号隔开，替换掉这里的星号：

```sql
SELECT id, col2 FROM table_name
```

这样就会只得到 `id` 和 `col2` 列的值。
我们还可以给它添加一个 `WHERE` 语句，来限定返回哪些结果：

```sql
SELECT id, col2 FROM table_name WHERE col2 > 1 and col3 like '%hello%'
```

`WHERE` 语句的句法与 `Python` 中条件语句的写法大致相似，区别是：

- 用 `=` 而不是 `==` 表示相等
- 没有 `is` 操作符

对于字符串，有一个特殊的操作符叫 `like`，它的作用相当于 Python 中对字符串应用 `in` 操作符或调用字符串的 `startswith` 和 `endswith` 方法，这和后面的字符串字面量有关。`%` 代表匹配0个或多个任意字符，`_` 代表匹配一个任意的字符。例如上面的 `'%hello%'` 就表示任意字符后有 `'hello'` 这个字符串，然后再是任意字符，即相当于 Python 中的 `'hello' in col3` ；如果写 `'hello%'` 则相当于 `col3.startswith('hello')`

#### 删除数据

```sql
DELETE FROM table_name WHERE ...
```

这里的 `WHERE` 和查询语句中是一样的。

#### 更新数据

```sql
UPDATE table_name SET col2 = 2.345, col3 = 'goodbye' WHERE id = 1
```

同样，这里的 `WHERE` 语句写法和前面是一样的，而 `SET` 后面的也只要写需要更新的列名和值就好了。

### 写给 SQLite 的三行情书

那么，在 Python 中要怎么使用 SQLite 的数据库呢？
在这里我们用一下江老师抓取豆瓣日记时候写的代码：

```python
conn = sqlite3.connect('douban.db')
cur = conn.cursor()
cur.execute('''create table if not exists doubannotes (
id integer primary key autoincrement,
username text,
userlink text,
notelink text,
notetitle text,
notecontent text,
issuetime text)''')
```

虽然这段代码看起来很长，但其实只有三“行”。

第一行：
`conn = sqlite3.connect('douban.db')`

打开当前文件夹的 douban.db 文件，把它用作 SQLite 数据库，如果没有就创建一个；conn 是一个 sqlite3.Connection 的实例。

第二行：
`cur = conn.cursor()`

从这个 Connection 中创建一个“光标”，使我们可以访问它的数据。
第三行看起来很长，但它实际上就是：

`cur.execute(sql)`

其中 `sql` 是一个字符串。对，字符串，就是这么简单。把 SQLite 自己的“外国话”当字符串传给这个光标就好，它会告诉 SQLite 该干什么。
那么我们如何取得 `SELECT` 语句返回的值呢？其实，`cur.execute` 已经把它返回给我们啦：

```python
for id, col2, col3 in cur.execute("SELECT * FROM table_name")
    print(id, col2, col3)
```

但是记住，在这样的情况下，我们不可以在循环体中再使用 `cur.execute`。如果要在循环体中执行别的 SQL 语句，需要在循环的外面再创建一个光标。如果只要第一行的值，可以很简单地写成：

```python
id, col2, col3 = cur.execute("SELECT * FROM table_name").fetchone()
```

当然这时候最好是有个 `WHERE` 语句。

特别地，如果表中一无所有，`fetchone` 会返回 `None`，于是上面的代码会出错。有时，我们需要事先判断一下：
```python
res = cur.execute("SELECT * FROM table_name").fetchone()
if res:
    id, col2, col3 = res
```

最后不要忘记，如果对数据库做了任何改动，要保存，一定要调用：

```python
conn.commit()
```
其中 `conn` 是那个 `Connection` 对象。

啊，说了那么多，大家运行那第一行的 `conn = sqlite3.connect(...)` 的时候，一定会遇到 `ImportError` 之类的错误的。
所以别忘了安装和 `import` sqlite3 ：）

### 练习
1. 改写记录学生成绩的类，添加合适的成员方法，将学生信息保存到数据库中，在计算平均分时从数据库读取学生成绩并计算。
> 提示：你可能需要再学习学习 SQLite 中的函数，以理解下面这行代码片段：
> `socre_sum = cur.execute("SELECT sum(score) FROM students").fetchone()[0]`

2. 搜索“如何用 Python 获取网页内容”，完成一个简单的脚本，其作用是显示电脑当前的公网 IP 地址。
> 提示：一些网站提供了这种功能，比如在百度搜索“IP”。但还有的网站的返回值更加简单一些，比如 ip.cn 这个网站。最后，为了更有效率地处理字符串，你可能需要学习一下正则表达式——别太贪心，任何“15分钟速成正则表达式”都是不可能的，而且千万注意是得学 Python 中的正则表达式哦！

### 句法

我们昨天提到了“继承”，这是怎么回事呢？我们来看看。假设有这样的代码：
```python
class LinkNode:
    def __init__(self, val): 
        self.value = val
        self.next = None
        
    def printValue(self):
        print(self.value)
```

啊，这是我们的老朋友了。现在打东边来了个哑巴，哦不，`DoubleLinkNode`：

```python
class DoubleLinkNode(LinkNode):
    def __init__(self, val, prevNode):
        self.value = val
        prevNode.next = self
        self.prev = prevNode
```

这是什么呢？一个双向链表中的节点。它的名称后面有个括号，括号里写了 `LinkNode` ，这表示它继承了 `LinkNode` 的内容，但是允许在一些地方进行修改。比如，它的构造函数要求一个额外的参数 `prevNode`，这时候我们就说它重载了构造函数。另一方面，它并没有给出 `printValue` 的定义，但我们还是可以这样调用：

```python
if __name__ == '__main__': 
    head = LinkNode(0)
    second = DoubleLinkNode(1, head)
    third = DoubleLinkNode(2, second)
    third.printValue()
    third.prev.printValue()
```

这时候，它调用的实际就是它所继承的 `LinkNode` 所定义的那个 `printValue` 。
至于操作符重载等，就是重载了其它一些 `__` 始且 `__` 终的函数，这里就不介绍了，有兴趣的读者可以自己搜索一下。另外需要说明的是，所有的类，哪怕没有写括号，也都继承了 `object` 这个类。

### `for` 和 `if` 的另一种写法

```python
import os
files = os.listdir('/tmp')
txts = [_[:_.rfind('.')] for _ in files if _.endswith('.txt')]
这相当于
import os
files = os.listdir('/tmp')
txts = []
for _ in files:
    if _.endswith('.txt'): txts.append(_[:_.rfind('.')])
```
当然，`if` 是可选的，只有有必要的时候才用加上，例如：
```python
lst = [repr(_) for _ in some_iterating_function()]
```

至此，Python 导论篇就要告一段落了。欢迎大家继续提供意见和建议，会在将来的推送中补充遗漏而重要的知识点。此外，之后几篇可能按照大家的建议来写一些基本的算法和离散数学的内容。In Python if possible, of course.

最后，Happy Python-ing!


[第二部分：数据结构与算法分析](2-algo.md)
