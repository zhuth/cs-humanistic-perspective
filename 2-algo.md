> 说明：为正常显示本文中的数学公式，请使用 Chrome 浏览器并安装 [GitHub with MathJax](https://chrome.google.com/webstore/detail/github-with-mathjax/ioemnmodlmafdkllaclgeombjnmnbima/related) 插件。

# 数据结构与算法分析

## 第一讲 算法分析基础；链表

休息一周，我们来继续“作为人类语言的 Python 导论”未完成的部分。在“导论”引导下学习了 Python 语言之后，应该可以完成诸如给出若干不同功能的片段，然后把它们组装成一个脚本用于自己的目的这样的工作，而这实际上涵盖了大部分我们日常中可能用到 Python 的情形。

但是，如果我们试图走得更深一些，或者就像“导论”中所说的那样，用 Python 作为一种语言来认识世界上的一些事物，理解一群人的话，我们可能需要一种更激进的观点，把计算机科学视为一种人文学科看待。

计算机科学作为人文学科的意义是：它最终实际上也就是为了增进人之间的理解。这种特性不是由于它关涉硬件的部分，而是由于它的程序，它关涉到数学的部分。

数学问题的求解是对一个不清晰的问题换用一种清晰的、完善定义了的方式来回答。譬如我们说，鸡兔同笼问题中的鸡有 $x$ 只而兔有 $y$ 只，并列出方程如 $x + y = 35$ 且 $2x + 4y = 94$，这时（可以证明）$x$ 与 $y$ 都是唯一的，因此我们也可以说“鸡兔同笼问题中，鸡的数量是如上定义的 $x$，兔的数量是如上定义的 $y$”。但是这个问题本身作为对 $x$ 和 $y$ 的描述太过冗长，未若 $x = 23$ 而 $y = 12$ 者。数学家的工作可以看做不断完善这种描述的语言，并将一种形式的描述转换成另一种形式。我们可以说他们的工作，就这个层面而言，是句法的。数学并未因此关涉到任何一种客观实在——那将是（在各种意义上的）物理学的工作——而作为一种语言的运用，它就是人文的。相反，各种意义上的物理学，作为严格的自然科学，乃是要用语言，包括数学的语言，去逼近现实。一种物理的理论可以描述和（哪怕是极其有限地）预测现实。而一种数学的理论是一种句法，是数学语言自我产生的方式。

计算机科学建立在数学的基础上，并且如我们所见，它有自己的语言。它没有要用现成语言逼近现实的冲动，而是像数学那样更多地表现出规定性。何以 1 + 1 = 2？这是由于人们的规定。谈论“1”到底“是什么”是没有意义的，而说“1”只有在一个数学的系统之中有意义，也就是说它实际上只有句法的意义，正如“我”这个词一样。

因而计算机科学可以视为（1）被数学规定的部分和（2）自身作出规定的部分的融合。算法分析与数据结构也就分别属于这两个部分。不过既然我们在标题中说“人文观点”，为照顾这个词通常狭窄含义，我们就不可能对算法分析中的数学作出深入的讲解。作为这个系列的第一篇，不妨直奔主题，先将算法分析的部分作个简单的交代。

### 什么是算法

解决某一问题的确定而可操作的步骤。

问题：如何把大象塞进冰箱？

- 步骤 1：打开冰箱门
- 步骤 2：把大象搬进去
- 步骤 3：关上冰箱门



问题：如何找出房间里的大象？

- 步骤 1：呼唤大象
- 步骤 2：等待回应
- 步骤 3：如果没有等到回应，告知“没有大象”



问题：如何求雨？

- 步骤 1：请神（仪式步骤另附）
- 步骤 2：念咒（咒语另附），在念咒时不要想到大象
- 步骤 3：送神

### 最初的符号，最后的意义

算法分析要做什么？简单地来说，我们主要做时间复杂度分析和空间复杂度分析，两者中又以前者为主要。计算机作为某种物质性的同时也是 *ästhetische* 的东西（在这个词的哲~学意义上），必然要求了时间和空间两种“感性直观的纯形式”（KrV: A22/B36），我们的分析从作为人的角度来说也就只能限制在这两个范围之内。时间之所以重要，从实用的角度来说，是因为我们哪怕再有钱，拥有最高级的设备，也无法可观地减少运行所用的实际时间，而一个好的算法则可以仅仅凭其本性而为我们节省下不少的时间，毕竟人生苦短（所以要用 Python 对不对）。而空间的复杂度还在于，我们不仅没有大把大把的时间，我们还缺钱。所以如果能减少内存的占用量或其它相关存储和通信资源，我们还可以省下一笔钱。算法分析在这个意义上就为我们选择使用何种方法提供了参考。

但从根本上，算法分析的意义在于，帮助你自己写出更好或更合适的代码。在远古时代人们并没有 `List.sort()` 之类的方法实现排序，而需要诸如自己去写一个排序函数。这时候你就要看了，如果时间紧而任务简单，列表固定只有 10 个数值，写一个冒泡排序就打发了；而列表的长度成千上万，对不起，请你还是写一个快速排序吧。因而进行算法分析，对于我们从程序编写入手的人（而不是理论的建构者）来说，就是理解程序代码的时间、空间代价。只有意识到这些代码不是免费的咒语，而是实实在在地蕴含了运行时的代价，编写代码的“认真”态度才有了用武之地，否则就只是一种姿态而已。

#### 符号与术语

- $f(x)$ —— 一个关于 $x$ 的函数
- $f(x) = O(g(x))$ —— 我们在此只需知道，它的意思表示，$f(x)$ 随着 $x$ 的增长而变化的“速度”，不会超过 $g(x)$ 随 $x$ 增长而变化的“速度”。在算法分析的语境中，这些函数 $f$、$g$ 可以认为都是随着自变量 $x$ 的增长而增长的，因为 $x$ 常常代表了问题的规模。
- 问题的规模 —— 使用算法求解的问题的一个量化的指标，譬如，冰箱的大小和大象的体重。

#### 公式

以下公式均假设，时间复杂度 $T(n) = O(f(n))$ ，$S(n) = O(g(n))$

- $ T(n) + S(n) = O(max(f(n), g(n))) $
- $ T(n) S(n) = O(f(n) g(n)) $
- $ n^2 + n + 1 = O(n^2) $ —— 一般地，最高为 $k$ 次方的多项式（希望你还没有忘记这个中学数学的概念）$P(k)= O(n^k)$
- $c = O(1)$（c 为常数）
- 由上可知，$cT(n) = O(f(x))$

#### 常用的顺序：

$O(1)$ “<” $O(\log n)$ “<” $O(\log^k n)$ “<” $O(n)$ “<” $O(n^k)$ \[随 k 增大而越“大”\] “<” $O(c^n)$ \[随常数 c 增大而越“大”\]

这里的小于号都加了引号，是因为我们实际上无法这样给若干个 $O$ 记号作比较。从数学上说，合适的符号是$=$，因为我们前面的定义中并没有说 $O$ 记号括号里的公式必须最为接近原来的那个式子 $f$，而只说“不超过”，尽管要想得出有用的分析，我们总得尽可能得出接近的式子。

### 面向代码

#### 循环的时间复杂度

算法分析经常从 `for` 循环入手，因为它的次数通常来说最方便。考虑如下 Python 代码片段：

```python
s = 0
for _ in range(0, 100):
    s += _
```

`for` 循环内部给 `x` 自加的步骤执行了 `100` 次（`_` 取 `0` 到 `99`），因此我们可以说上面这段代码的时间复杂度是 $O(100) = O(1)$ 。

啊，对，因为我们在这里并没有可变的“问题的规模”。
我们修改一下代码，再试一次：

```python
s = 0
for _ in range(0, n):
    s += _
```

上述代码，自加的步骤执行了 $n$ 次，$n$ 是我们这里的“问题的规模”。所以上述代码的时间复杂度是 $O(n)$。

但如果我们的问题是求 1 到 $2n$ 的和，上述代码写成

```python
s = 0
for _ in range(0, 2*n):
    s += _
```

它的时间复杂度仍然是 $O(n)$。

接下来，考虑如下嵌套的循环：

```python
for y in range(0, maxy + 1):
    first = True
    for x in range(0, maxx + 1):
        if not first: sys.stdout.write(',')
        if (x, y) in m:
            sys.stdout.write(m[(x, y)])
        else:
            sys.stdout.write('_')
        first = False
    sys.stdout.write('\n')
```

看起来复杂很多。我们先看里面一个关于 $x$ 的循环，无论怎样运行，这个循环内部的指令数量都与问题的规模无关。因此它就可以看做一个常数项，而所有的常数我们都可以看作 1。于是内部这个关于 $x$ 的循环时间复杂度是 $O(maxx + 1) = O(maxx)$。

再看外面关于 y 的循环，它包含了两条（因此也是常数项）语句和一个 `for` 循环，因此它的时间复杂度，也就是整个这个代码片段的时间复杂度为：$O(maxy * (O(maxx) + 1))$ = $O(maxy * maxx)$ 。

从上述观察我们可以看出，多重循环的时间复杂度，通常就是各级循环迭代规模相乘——除非，在某一级中调用到了一个复杂度超过其内部循环的函数之类。比如：

```python
for x in range(0, n):
    for y in range(0, m):
        print(x+y)
    print(sum(mat[x,:]))
```

在这里，我们假设 `mat` 是一个 $n \times w$ 的矩阵而 $w$ 总是大于 $m$，并假设 `sum` 函数的时间复杂度为相对其规模是线性的（即，如果规模是 $n$，它就是 $O(n)$；此 $n$ 非彼 `n`），因此就是 $O(w)$ 。而根据 $w + m = O(max(w, m))$ ，$for x$ 的循环体内部时间复杂度就是 $O(w)$ 而不是 $O(m)$，因此整个片段的时间复杂度就是 $O(nw)$ 而不是 $O(nm)$。

#### 递归程序的复杂度分析

嗯哼，这是一个非常有趣的问题。
比如说下面这个代码片段计算著名的斐波那契数列：

```python
def fib(n):
    if n == 1 or n == 2: return 1
    return fib(n - 1) + fib(n - 2)
```

如果用 T(n) 表示取某个值 n 时上述代码所需进行的基本操作数量，我们会有：

$$T(n) = T(n - 1) + T(n - 2) + c$$

显然 $T(n) > Fib(n) $（Fib 表示“数学上的”斐波那契数列）
我们知道，斐波那契数列的通项公式是：
$$Fib(n) = \frac{\sqrt{5}}{5}\left[\left(\frac{1+\sqrt{5}}{2}\right)^n-\left(\frac{1-\sqrt{5}}{2}\right)^n\right]$$

因此 $Fib(n) = O(cn)$，$c = (1 + \sqrt{5}) / 2 < 2$。

而，做一些扩大，我们有 
$$ T(n) ≤ 2T(n - 1) + c $$

忽略常数项，我们可以有 $T(n) ~ 2T(n - 1)$ 。即 $T(n) = O(2^n)$，这样就有：

$$Fib(n) < T(n) = O(2^n)$$

所以上面这个 `fib` 代码怎么看都逃不掉是一个指数级别的时间复杂度了。

相反，如果我们可以在常数时间内计算出一个数的任意次方（在浮点数允许的范围内，我们确实可以！），直接用上面的通项公式计算斐波那契数列，时间复杂度将是——

$$O(1)$$

你看，于是我们如果知道了通项公式，不用花很多时间很多钱，就可以算出比如 $Fib(1000)$ ，而用上面的 `fib` 这个函数则要花许许多多的时间。指数增加是极其可怕的。但不幸的是，我们恐怕并不总是那么幸运，可以有一个别人已经算好了的通项公式来用，而且有时确实也算不出这样一个通项公式来。

在运行时节省下来的时间，是我们为之付出的脑力——和时间——给它买了单。

### 数据结构

我们将在后面讲解数据结构的时候运用到一些关于算法分析的内容，这将为我们展现出，人们**为什么**要去发明这样一种数据结构。但首先恐怕还是要明确一下，数据结构大致上是什么？

不要把它和数据库或 Python 里的类搞起来。数据结构指的是数据的组织方式。它尽管常常可以用 Python 里的“类”来实现，却不是“类”这个概念本身：重要的是数据之间关联的结构，而不是数据**自身**有什么样的结构。因此，“学生”有“姓名”、“学号”和“成绩”，这不是数据结构考察的内容；数据结构考察怎样将这些信息排列起来，例如存成链表，还是依照学号存成一个搜索二叉树，而这将决定我们访问这些学生信息的**效率**。

但是，毕竟在运用 Python 实现具体的数据结构时，我们常常利用“类”。这些类除了种种数据之外，额外地包含了**描述**某种数据结构所要求的数据间关系的信息。

今天我们就讲一个非常简单的，也是大家的老朋友了——链表。我们看到过链表是这个样子的：

```python
class LinkNode:
    def __init__(self, val):
        self.value = val
        self.next = None
```

后来我们又看到了双向链表：

```python
class DoubleLinkNode(LinkNode):
    def __init__(self, val, prevNode):
        self.value = val
        prevNode.next = self
        self.prev = prevNode
```

这里，`next` 和 `prev` 字段就属于上面所说的，单向和双向链表所要求的数据间关系。不过，我们其实还没有很好地定义一些操作，以将某个值插入到链表中某个节点的后面。我们在这里就先只实现一个单向链表的完整操作：

```python
class LinkNode:
    def __init__(self, val):
        self.value = val
        self.next = None

    def append(self, val):
        self.next = LinkNode(val)
        return self.next
    
    @staticmethod
    def iterate(head, act):
        n = head
        while n is not None:
            act(n.value)
            n = n.next
            
if __name__ == '__main__':
    head = LinkNode(1)
    tail = head
    for i in range(2, 10):
        tail = tail.append(i)
        
    LinkNode.iterate(head, print)
```

屏幕上将输出：

```
1
2
3
4
5
6
7
8
9
```

在这个过程中，我们发现，单向链表只能从头到尾地走一遍，因此保留一个“头”（`head`）就非常重要。这个“头”使我们得以**几次三番从头再来**。

我们还可以用下面的语句，寻找某个值 n 是否在链表中，如果存在的话就输出“Exists”：

```python
LinkNode.iterate(head, lambda x: print('Exists') if x == n else 0)
```

而双向链表由于多了一个 `prev` 字段，就保留了前一个数据的位置信息（姑且这么说吧），所以不仅可以正过去，还可以倒过来。实现 `DoubleLinkNode` 的任务当然就交给诸君留作练习了。一并留作思考的是：上述寻找某数 n 的代码，其时间复杂度是多少？（将访问一个链表节点视为一个基本操作）

## 第二讲 栈与队列；树与图初步
### 栈与队列

栈（Stack）与队列（Queue）是两种特殊的链表，它只允许从一端（分别是“头”和“尾”）进行插入操作，同时也只允许从一端读取（都是“头”）。容易想见，它们都可以用单向链表直接实现。我们就来实现一下。

```python
class Stack:
    def __init__(self):
        self.head = None
        
    def put(self, val):
        n = self.head
        self.head = LinkNode(val)
        self.head.next = n
        
    def pop(self):
        v = self.head.value
        self.head = self.head.next
        return v
        
    def empty(self):
        return self.head is None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def put(self, val):
        if self.empty():
            self.head = LinkNode(val)
            self.tail = self.head
        else:
            self.tail = self.tail.append(val)
    
    def pop(self):
        v = self.head.value
        self.head = self.head.next
        return v
    
    def empty(self):
        return self.head is None
```

然后我们来试一下，把 1~9 插入到这两个不同的数据结构之中，再来读取它们，会得到什么样的结果：

```python        
if __name__ == '__main__':
    print('Queue:')
    q = Queue()
    for i in range(1, 10):
        q.put(i)
    while not q.empty():
        print(q.pop())
    
    print('Stack:')
    s = Stack()
    for i in range(1, 10):
        s.put(i)
    while not s.empty():
        print(s.pop())
```

屏幕上输出

```
Queue:
1
2
3
4
5
6
7
8
9
Stack:
9
8
7
6
5
4
3
2
1
```

答案是：对于队列，先插入进去的数值也被先读取到了；而对于栈，后插入进去的数值反而先读取到。队列可以看做排队，而栈则可以看做叠起来的盘子；队伍有先来后到的原则，而叠起来的盘子却只能先拿走上面的盘子才能拿到下面的盘子。

实际上，没有人会用这种原始的方式来在 Python 中使用队列和栈。这些都可以非常简单地使用 Python 自己的 `list` 来实现。要实现一个队列，完全可以这样写：

```python
class Queue:
    def __init__(self):
        self.l = []
        
    def put(self, val):
        self.l.append(val)
    
    def pop(self):
        v = self.l[0]
        self.l = self.l[1:]
        return v
    
    def empty(self):
        return len(self.l) == 0
```

**练习**

模仿上例，用 `list` 实现栈。

#### 队列和栈的用途

队列和栈有很多种用途。譬如在批量处理一些文件时，我们会遍历一个列表，实际上就已经使用了队列的思想，尽管这时候我们并不显式地删除数组中的元素。栈看似是不可理喻的，但是如果我们把上面这个输出9 ~ 1 的代码用如下形式改写：

```python        
def printWithStack(num):
    if num == 10: return
    printWithStack(num + 1)
    print(num)
    
if __name__ == '__main__':
    printWithStack(1)    
```

输出是一样的，而这时候的栈存在于何处呢？存在于系统的函数调用之中。它首先调用了 printWithStack(1)，然后又调用 printWithStack(2)，然后再调用 printWithStack(3) …… 最后它调用到 printWithStack(10) ，再逐层退出。

可以看出，虽然 1 ~ 9 是依顺序作为参数传入的，但是先执行的部分要等待后执行的部分退出之后才打印自己的参数，这就导致我们看到的仍然是 9 ~ 1 的逆序。而如果把 `print(num)` 放置在递归调用 `printWithStack` 之前，我们就会看到输出 1 ~ 9 的顺序。

现在，这就解释了我们已经提到过许多次的 StackOverflow 网站名称的来历。当我们把边界条件 `if num == 10: return` 注释掉，我们将收获一个货真价实的 Stack Overflow：

——等一下，为什么卡住了？

——因为这个程序正在耗尽你的内存呀。

我们可以看成系统（Python 环境）维护了一个函数调用的栈，存储了每个函数运行到的位置和参数、局部变量等信息，而在函数中调用函数，则是把新的函数、参数等压入这个栈；等这个函数运行完毕，它再会从栈中弹出。

### 树（1）

地上的树根在下，数据结构中的树根在上。一张典型的树图是这个样子的：

![Bin Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Binary_tree.svg/330px-Binary_tree.svg.png)
（图：Wikipedia）

上面这个图中，这棵树上每个节点最多有两个分叉，因此叫做二叉树。（并不是因为它很2啦！）那些下面没有分叉的节点称为“叶节点”，而高高在上孤零零的那一个叫做“根节点”。到根节点的路径长度决定了节点所在的层数，每一层的上下级节点分别叫做“父节点”（parent）和“子节点”（child）。

在树中（也许我们应该说，在树上？）每一根枝杈都是从上一级的节点上分支出来的，这也就是说，除了根节点，每个节点都有且仅有一个父节点。同时，叶节点之间也不会有直接的联系。我们发现，这种关系仍然是单向链表的变体。事实上，我们只需要把原先的 `LinkNode` 改成下面这个样子：

```python
class BinTreeNode:
    def __init__(self, val):
        self.value = val
        self.child1 = None
        self.child2 = None
```

它就可以表示二叉树中的一个节点。而如果我们要更一般地表示一个树节点，也许可以写成这个样子：

```python
class TreeNode:
    def __init__(self, val):
        self.value = val
        self.children = []
```
而 `self.children` 里的元素，或上面的 `self.child1`, `self.child2` 都将是一个 `TreeNode` 或 `BinTreeNode` 。但不像单向链表我们有且只有一条从头到尾的路，从根节点到叶节点之间的路有许多条，而每一条也同时意味着你没法走到那些错过了的点。Two roads diverged in a wood ——

好了，现在让我们来做一个练习。

#### DFS 与 BFS

你是 Robert Frost 的传人，你坚信一定要走人迹罕至的一条路。现在你进入了森林中，森林它一丛丛。每一个岔口都只分成两条路，你可以看到上面都有一个记号，表示这条路有多少人走过（每条路都不会超过 30000 人）。请补完下面的代码，以从森林的入口（root）走到它的一个出口（没有岔路），一路上记下选择的分岔路上走过的总人数。

```python
class BinTreeNode:
    def __init__(self, val):
        self.value = val
        self.child1 = None
        self.child2 = None
        
    @staticmethod
    def traverseLikeRobertFrost(root):
        n = root
        totalTravellers = 0
        while n.child1 or n.child2:
            totalTravellers += n.value
            n1 = 30000 if not n.child1 else n.child1.value
            n2 = 30000 if not n.______ else n.____________
            if ______:
                n = n.child1
            else:
                n = n.child2
        totalTravellers += n.value
        return totalTravellers
```

可以发现，我们尽管是在（现实意义上的）森林中走，对于数据结构来说，我们却是在“树”上走。我们走的是（现实意义上）每个“岔路点”之间的路径，但对于数据结构来说，我们重要的是访问每一个“节点”。

像 Robert Frost 这样走路的话，我们可不一定能保证使最终走过的道路的“总人数”最少。什么情况下可以呢？那就是说，每个先前走过的人都不会半途而废、折返，也不会有什么直升机降下绳索来把他们从这里捎到那里，如此等等，以至于对于数据结构来说，“树”的父节点上记录的访问人数总是精确地等于其所有子节点的访问人数的和。由于人数不可能是负的，所以每次我们选择“少有人的走的路”，最后这些访问人数的总和就一定是最小的。

像 Robert Frost 这样在树上游历的方式，我们称之为——贪心。贪心是一种思想，每次选择当前情况下“代价最小”或能使某种评价最高的选择，而不及其余。因此如果 Robert Frost 在第一张图上的树上行走，他就不会发现 2-7-2 这样一条路，而会去走 2-5-9-4。

有没有什么办法能保证走到的路一定是最短的，而不利用别的额外信息呢？有！那就是*几次三番从头再来*，不破楼兰终不还，把每一条路都走一遍！

——那么，这不是很浪费时间吗？

——也对，那么，就每次只退回到上一个岔路口，再去走那没有走过的路吧！

```python

class TreeNode:
    def __init__(self, val):
        self.value = val
        self.children = []
        
    @staticmethod
    def findMin(start):
        def DFS(start, total):
            if len(start.children) == 0:
                ans = min(ans, total)
                return
                    
            for _ in start.children:
                DFS(_, total + _.value)

```

这个 `findMin` 方法帮助我们把每一条可能的路径都走了一遍，并最终返回一条路径的节点上 `value` 的总和的最小值。而完成主要工作的是这个称为 DFS 的嵌套函数。只要可能，它总是往树的深处走，走到不可走的时候也就找到了一条路，然后再去更新最小值 `ans`。因此，它叫做深度优先搜索——Depth-First Search。

那么，大家可能会想，是不是还存在一种和它策略不同的搜索方法呢？Bingo！那就是——广度优先搜索（Breadth-First Search，BFS）。
观察到 DFS 的递归调用，我们说，其实隐含了一个栈；而在这里，我们就要用到一个——队列。

```python
def BFS(start):
    q = [{'node': start, 'total': start.value}]
    idx = 0
    ans = float('inf')
    while len(q) > idx:
        n = q[idx]['node']
        t = q[idx]['total']
        idx += 1
        if len(n.children) == 0: ans = min(ans, t)
        q += [{'node': _, 'total': t + _.value} for _ in n.children]
    return ans
```

我们发现，由于不需要递归调用，BFS 可以自己独立地返回答案。

**练习**

1. 参照 BFS 函数，用栈改写 DFS 函数。
2. BFS 和 DFS 的时间复杂度相对于树的总节点数 N 是多少？如果是二叉树，那么相对于二叉树的总层数 M 而言又是多少？
3. 如果每个节点上的代价相同，即我们不考虑 value 的总和之类的东西，而只考虑总层数，那么，BFS 最先走到的叶节点一定是层数最小（即，距离根节点最近）的那个叶节点，试说明之。BFS 的这个特性使之在寻找根节点到叶节点的最短路径时运行得往往比 DFS 快，但时间复杂度二者仍是一样的，试说明之。

更多关于树的定义和一些崎岖的反例，请参考 https://en.wikipedia.org/wiki/Tree_(data_structure)  。


### 图（1）

现在我们在树的某两个节点之间再添加一条边。
如我们所知，它就不是树了。
它是什么？
它叫做——图（Graph）。

不要把这里的图和图片、图像或图形相混淆。我们在这里不讲图像处理或图形生成。

![Graph](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/6n-graf.svg/375px-6n-graf.svg.png)
无向图的例子（图：Wikipedia）

上图中画出的一个图称之为无向图，而无向图其实是有向图的一个特例：任何两个节点之间，要么没有边，要么就有正反两个方向的边。

![Directed Graph](https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/4-tournament.svg/150px-4-tournament.svg.png)
有向图的例子（图：Wikipedia）

要描述一个图，我们当然也可以像 TreeNode 那样来表示，比如说：

```python
class Node:
    def __init__(self, val):
        self.value = val
        self.adjacent = []
```

直观地来说，如果 `adjacent` 字段里存储的每个元素又都是一个 `Node`，这样我们只是存储了图中节点之间的邻接关系——也就是两个节点之间边的方向，而并没有存储关于这条边本身的信息，譬如，长度。所幸，Python 强大而原生的 `dict` 类型弥补了这一点。

但是也因为有 `dict` 类型，因此，我们甚至可以用一种更方便的方式来存储节点之间的关系。这就是图的邻接矩阵表示——尽管我们实际上用的是 `dict` 。假设 `A` 和 `B` 各是一个节点，我们用 `adj[(A, B)]` 来存储从 `A` 到 `B` 的一条边的信息。如果 `(A, B)` 这个元组（tuple）不在 `adj` 这个 `dict` 中，就认为 `A` 到 `B` 之间没有边。显然，图可以从任何一点出发，但并不一定能够走完全部的点。此外，图中还可以有环。

为此，我们既不可以像对于树那样二话不说就 DFS / BFS 伺候，也不可能通过简单记录有没有到达过某个点来避免陷入循环——譬如说，假设一个星形的图：中心节点 A 和周围的几点 B、C、D、E 之间都有无向边，而 B、C、D、E 之间没有边。这时，从任何一点出发实际上都还是能够把别的点访问到，但是 A 节点就要访问 4 次。为什么是 4 次呢？——因为 A 节点一共只有四个相邻节点呀！如果访问 5 次，那么肯定就又有另外某个节点多访问了一次，也就是说，白跑了。比如：
A-B-A-C-A-D-A-E 这是合理的，而
A-B-A-C-A-C-A-C-A-C-...-A-D-A-E 这之中就有了一个循环 A-C-A 。

一般地，我们把从某个节点“往外”连接到其它节点的边的数量称为“出度”，而把其它节点连到它的边的数量称为“入度”。对于无向图的每个节点，入度等于出度。对于有向图的节点则不然。

因此我们现在可以说：限制在一条路径中每个节点访问的次数不超过它的出度，就可以在一定程度上避免出现循环的情况。这种对搜索添加有理有据的限制条件的做法，称为**剪枝**。自然，这也是从搜索遍历树的隐喻之中产生出来的。事实上，它是说：搜索不仅遍历一棵树，而且可以产生一棵树，而剪枝就是说不去产生那一部分的枝杈。这又是怎么回事呢？如果我们现在在 1-2-3-4 这个有向图上从 1 出发进行一次有上述限制的 BFS，我们写出它每个时刻队列中的变化：

```
a. 从队列中取出1，1相邻的2，4添加到队列
b. 取出2（路径：1-2），2相邻的4又添加到队列
c. 取出4（路径：1-4），4相邻的3添加到队列
d. 取出4（路径：1-2-4），4相邻的3又添加到队列
e. 取出3（路径：1-4-3），3相邻的1添加到队列
f. 取出3（路径：1-2-4-3），3相邻的1又添加到队列
g. 取出1（路径：1-4-3-1），1相邻的2添加到队列（4的访问次数已经到达了它的出度）
h. 取出1（路径：1-2-4-3-1），1相邻的2、4的访问次数都已经到达了它的出度，找到一条路径：1-2-4-3-1
i. 取出2（路径：1-4-3-2），2相邻的4访问次数已经到达了它的出度，找到一条路径：1-4-3-2
```

我们取每一个状态的标号作为节点，可以发现，这里有一棵树：
```
a - b -- d -- f -- h
  \ c -- e -- g -- i
```
搜索会生成出一棵树，而这其中的每个节点又对应于图中的节点，尽管有些节点被对应了多次。但如果没有那个限制，我们可以想象，这棵树中就会有无限多个节点了。

## 第三讲 散列；排序

### 散列

我们至此还没有专门讨论过 Python 中 `dict`（字典）。一个字典对象可以用标注的构造函数来初始化：

```python
d = dict()
```

也可以像这样，用 `{}` 来初始化：

```python
d = {}
```

或者这样，在初始化的时候给定一些**键值对**：

```python
d = {
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D': 1.0,
    'F': 0
}
```

这样我们就建立了一个等第与绩点的换算表。对于字典的访问是这样的：

```
>>> d['A']
4.0
```

像 `list` 一样，用 `[]` 来表明字典中的“键”。在 Python 中，我们用这样的方式来判定某个字典中有没有指定的“键”：

```python
'D-' in d
```

而用给 `list` 中元素赋值一样的方法来给字典的某个键赋值。字典的好处在于，它可以以常数时间（$O(1)$）来访问每一个元素，而不必像 `list` 那样，只有挨个寻找才能找到合乎条件的东西。比如说，上面这个换算表也可以用下面这个 `list` 来实现：

```python
l = [('A', 4.0), ('A-', 3.7), ('B+', 3.3), ('B', 3.0), ('B-', 2.7), ('C+', 2.3), ('C', 2.0), ('C-', 1.7), ('D', 1.0), ('F', 0)]

def getScore(grade):
    for g, s in l:
        if g == grade: return s
    return None

```

这样的话，完成一个匹配就需要 $O(N)$ 的时间，其中 $N$ 为 `l` 的长度。在这里，我们这个长度是不会变的；但如果它会变，运行的程序就会受到它的影响。不得不说，这是一种非常慢而傻的方法。

那么大家就要问了，为什么完成同样的操作，字典就要比列表快呢？这就是散列的作用了。

散列（Hash）是一个函数，将指定的对象转换成一个（不唯一的）数。这个数，我们音译为哈希值，相应地这个函数也可以称为“哈希函数”。Python 中每个类都会有一个哈希函数，它可以是系统（`object`）默认的，也可以是类中显式声明的 `__hash__` 成员函数。比如：

```python
import time
class A:
    def __init__(self):
        self.hashvalue = int(time.time() * 1000)
        
    def __hash__(self):
        return self.hashvalue
```

在这里，我们用对象创建时的时间戳（即，距离 1970 年 1 月 1 日世界协调时 0 时整的毫秒数）来作为这个对象的哈希值。对象哈希值可以用下面的方法得到：

```python
x = A()
hash(x)
```

当然，这里的 `x` 也可以是任何一个 Python 的对象。我们在这里只需知道，哈希值是讲对象用一个整数来代表的函数。当然它不可能是唯一的。事实上，我们也不需要它是唯一的。

散列的思想，便是将某个对象的哈希值对某个数取余，然后将它存储到某个列表中（通常称之为“桶”）：

```python
class MyBuckets:
    DEFAULT_BUCKETS = 32
    
    def __init__(self):
        self.buckets = [[]] * MyBuckets.DEFAULT_BUCKETS
    
    def getBucketIndex(self, key):
        return hash(key) % len(self.buckets)
    
    def put(self, key):
        self.buckets[self.getBucketsIndex(key)].append(key)
        
    def contains(self, key):
        l = self.buckets[self.getBucketsIndex(key)]
        return key in l
```

上面，我们实现了一个叫做 `MyBuckets` 的类。它像一个集合一样——但是允许多个重复的 `key`，可以用 `put` 来添加元素，也可以用 `contains` 来判断是否含有某个键 `key`。对于哈希值取余相同的键，它用一个列表来保存所有的键。

现在我们来分析这两个操作的时间复杂度。显然，添加到桶中的操作时间复杂度是常数级别的。而判定某个元素是否在桶中，可以看到，在最坏情况下，所有的键都不幸落入同一个桶中，这样的时间复杂度便是 $O(N)$，$N$ 为键的总数。这时，一定是我们选取的桶的数量不合适，或者哈希函数本身选取不当。

但是我们的运气不可能一直那么差。在平均的情况下，哈希函数的值取余数应该可以看做是平均分布的，因此每个桶里平均有 $N$ 除以桶的数量 $M$ 个元素，这时查询某个键是否存在于桶中，其时间复杂度就是 $O(N/M)$ 。但没有用，$M$ 在上面的代码中是不会变的。但如果我们事先知道了 $N$ 大概会有多少，并取 $M$ 为 $N/c$ 其中常数 $c$ 称为装填因子，也就是桶中元素与桶的数量之比。这样，我们判定桶中有没有某个元素的时间复杂度就骤然变成了 $1/c$，也就是一个常数了！

可是，我们怎么才能估计出 $N$ 的规模呢？难道，字典中的键不是一个个添加进去的吗？这里便涉及到所谓的“再散列”。我们可以在实际的装填因子大于某个数值时将桶的数量扩大一倍，同时改变对待哈希值的方式（也就是更改取余的那个数）。这样，可以保证装填因子始终小于这个设定值，从而判断桶中有没有某个元素的时间复杂度可以预期保持为一个常数。不过，在我们这种实现方式中，再散列过程本身所花的时间可是不小，足足 $O(N)$ 呢！

**练习**

改写 `MyBuckets`，使之可以随时进行再散列。不考虑元素删除导致桶的数量减少，也不考虑键有重复的情形。

```python
class MyBuckets:
    DEFAULT_BUCKETS = 32
    COEF_LIMIT = 0.7
    
    def __init__(self):
        self.buckets = [[]] * MyBuckets.DEFAULT_BUCKETS
        self.bucketsCount = len(self.buckets)
        self.size = 0
    
    def rehash(self):
        self.buckets += [[]] * self.bucketsCount
        self.bucketsCount *= 2
        # TODO: 在此填入你的代码。
        # 提示1：删除列表中的元素，可以使用列表的 .remove 方法。
        # 提示2：如果循环在遍历某个 list，这时候不能用 .remove 来改变它，但可以先将这些要删除的值保留下来，然后再删除。
    
    def getBucketIndex(self, key):
        return hash(key) % self.bucketsCount
    
    def put(self, key):
        self.buckets[self.getBucketsIndex(key)].append(key)
        self.size += 1
        if float(self.size) / self.bucketsCount > MyBuckets.COEF_LIMIT:
            self.rehash()
        
    def contains(self, key):
        l = self.buckets[self.getBucketsIndex(key)]
        return key in l
```

这样一来，我们就理解了：只要把值和键一起存入桶中，我们就实现了一个字典，而且可以保证预期是常数时间里（或者说，差不多是常数时间里）可以搞定的了。可是再散列的问题还是没有得到很好的解决。有办法让它也快一些吗？

### 树（2）

上次我们提到了二叉树，不过当时我们称它的两个子节点为 `child1` 和 `child2`，这实在有点委屈它们，因为它们本来是有名字的，分别叫左节点和右节点，而以左右节点为根节点的树称为左子树和右子树。区分左右是因为这种顺序对我们来说完全可以是有用的。我们现在来设想这样一个二叉树：它的左节点的值总是小于自己的值，而右节点的值则总是大于自己。这样的二叉树叫做**二叉搜索树**。

![Bin Search Tree](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/225px-Binary_search_tree.svg.png)
（图：Wikipedia）

我们这就来实现一下看看。

```python
#!/usr/local/bin/python3
import sys

class BSTNode:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        
    def find(self, x):
        if x == self.value: return self
        elif x < self.value: return self.left.find(x) if self.left else None
        else: return self.right.find(x) if self.right else None
        
    def put(self, x):
        if x == self.value: return
        elif x < self.value: 
            if self.left:
                self.left.put(x)
            else:
                self.left = BSTNode(x)
        else:
            if self.right:
                self.right.put(x)
            else:
                self.right = BSTNode(x)
                
    def BFS(self):
        q = [{'node': self, 'level': 1}]
        idx = 0
        lLevel = 0
        while len(q) > idx:
            n = q[idx]['node']
            level = q[idx]['level']
            idx += 1

            if lLevel < level:
                sys.stdout.write('\nLevel %d:' % level)
                lLevel = level
            
            sys.stdout.write(' %.1f' % n.value if n else ' -')
            if n is None: continue
                
            q += [{'node': _, 'level': level + 1} for _ in [n.left, n.right]]
        

if __name__ == '__main__':
    import random
    
    bst = BSTNode(0.5)
    for _ in [0.8, 0.7, 0.1, 0.2, 0.5, 0.3, 1.0, 0]:
        print('Insert:', _)
        bst.put(_)
        
    bst.BFS()
```

程序输出：

```
Insert: 0.8
Insert: 0.7
Insert: 0.1
Insert: 0.2
Insert: 0.5
Insert: 0.3
Insert: 1.0
Insert: 0

Level 1: 0.5
Level 2: 0.1 0.8
Level 3: 0.0 0.2 0.7 1.0
Level 4: - - - 0.3 - - - -
Level 5: - -
```

换句话说，这时候的树是这个样子的：

```
                    0.5
        0.1                    0.8
    0.0        0.2            0.7        1.0
                0.3
```

可以想见，这样一个插入和查找的操作其实都是深搜，它在最坏情况下的时间复杂度是 $O(N)$ ——数按照次序插入，这时，这个二叉树退化成一个单向链表；而在最好的情况下，则是 $O(\log N)$，也就是满二叉树的树高。容易想见，用二叉搜索树代替列表，可以改善散列实现 `MyBucket` 进行再散列的时间：只要规定（比如）左节点中哈希值的二进制表示中某一位是1，右节点的同一位是0，等等，就能够把再散列时的桶中元素的拆分操作变成左右子树的整体移动。

同样，考察到上面这个列表中，根节点的选择非常重要——如果我们第一个插入的元素是 0，那么显然就会平白无故多了一个层高出来。因此，人们发明了诸如 AVL 树（平衡二叉树）、B+ 树（不是二叉树）等方式，提高搜索效率并具有比较好的存储效率，等等。其主要思想也是运用树的特点进行一些节点的移动，这里就不一一介绍了。

#### 最小堆

在讲树的时候我们提到了一句平衡二叉树。在这里我们不打算展开讲它的实现，而是提到了它的主要思想：如果插入一个节点之后二叉树不再平衡——不再尽可能地“满”（有大量节点只有一个子节点），那么就让一些子节点和父节点位置交换。

同样的思路，可以设想，我们也能够维持一个尽可能满的二叉树，它的父节点值大于它的所有左右子树里的节点。就像这样：

![Min Heap](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Min-heap.png/360px-Min-heap.png)

把一个节点插入到最后一个节点位置上，然后去看它是否比它的父节点小，是的话就交换位置并对父节点递归进行相同的操作，否则就停止。这样的话，就能够保证根节点一定是整棵树里最小的。这样一个二叉树我们称之为最小二叉堆（Heap）。相应地，也有最大堆，不过其实也是一回事了。

Python 为我们实现了最小堆操作，只需引用 `heapq` 即可。我们摘引一段 `heapq` [文档](https://docs.python.org/3.0/library/heapq.html) 中的例子：

```python
from heapq import heappush, heappop
heap = []

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
for item in data:
    heappush(heap, item)

while heap:
    print(heappop(heap))

```

屏幕输出：
```
0
1
2
3
4
5
6
7
8
9
```

可见，无论以什么次序插入（`heappush`）到最小堆中，弹出的时候（`heappop`）都是从小到大的顺序。因为这个缘故，最小堆有时也被称为优先队列（priority queue）。其插入和弹出操作的时间复杂度都是 $O(\log N)$ ，因此插入和弹出 $N$ 个数的时间便是 $O(N \log N)$。

最小堆让我们想到了一件事情，那也就是第一讲中我们所提到过的，没有 `sort()` 方法的时候人们是怎么做排序的呢？

### 排序

我们现在有了最小堆，所以我们知道，用 $O(N \log N)$ 的时间复杂度就可以完成排序的动作。这也是快速排序（qsort）的时间复杂度，而且在相当程度上，我们也可以说，最小堆的思想，同时也就是快速排序的思想。

相反，我们讲的冒泡排序又是怎么回事呢？闲话少叙，用 Python 来说说怎么给一个列表 `a` 做冒泡排序：

```python
def bubble_sort(a):
    l = len(a)
    for i in range(0, l):
        for j in range(i, l):
            if a[i] > a[j]:
                a[j], a[i] = a[i], a[j]
```

**练习**

写出冒泡排序的时间复杂度。

下面这种叫做插入排序。

```python
def insert_sort(a):
    l = len(a)
    for i in range(1, count):
        t = a[i]
        for j in range(i - 1, -1, -1):
            if a[j] < t: break
            a[j + 1] = a[j]
            a[j + 1] = t
```

**练习**

1. 说明插入排序的思想。
2. 写出插入排序的时间复杂度。

**练习**

阅读有关快速排序的 [Wikipedia 词条](https://en.wikipedia.org/wiki/Quicksort) ，编写 Python 代码。


## 第四讲：图；动态规划

### 最短路径问题

正如我们在谈到图、树时举的例子那样，图最重要的用途也许就在于描述地点之间的关系。一些抽象的情形也可以转换为图，不过我们在此就姑且略过不提了。我们讲到，DFS 和 BFS 可以在树上找出从根节点出发（实际上，也是从任何一个节点出发）到达树中（子树中）叶子节点的路。同样的情况想必也适用于图，而我们在[上回](#图1)也已经提到了，如果图中有一条路不断地来回跑，我们要对 DFS 和 BFS 加以剪枝。

现在问题来了，对于一个比较“正常”的情形，我们如何才能找到从一条路到另一条路之间的最短路呢？注意到这并不是 BFS 所能解决的，因为每一条边的长度（或者说权值）并不相等，所以访问过最少的节点不一定是最短的路。

有一位叫 Dijkstra 的壮士，提出了下面这个方法：

```python
def Dijkstra(start, nodes, adj): # start：开始的点；nodes：图中节点的列表；adj：存储边的信息的 dict
    s = set() # 这个集合中保存作为最短路径而考虑过的节点
    dist = {} # 这个字典以节点为下标，保存的是从 start 点到某点之间的最短距离
    prev = {} # 这个字典同样以节点为下标，保存最短距离中，到达某一节点之前的节点是哪个；可以参见 get_path_from_prev 函数，它将返回一个字符串，表示完整的路径
    
    for n in nodes:
        if (start, n) in adj:
            prev[n] = start
        dist[n] = float('inf')
        
    dist[start] = 0
    s.add(start)
    
    for n in nodes:
        if n == start: continue
        mindist = float('inf')
        u = start
        for m in nodes:
            if m in s or m not in dist: continue
            if dist[m] < mindist:
                u = m
                mindist = dist[m]

        s.add(u)
        for m in nodes:
            if m in s or (u, m) not in adj: continue
            if dist[u] + adj[(u, m)] < dist[m]:
                dist[m] = dist[u] + adj[(u, m)] # 注1
                prev[m] = u
    
    return prev, dist
    
def get_path_from_prev(prev, dest):
    s = ''
    n = dest
    while n:
        s = n.name + ' ' + s # 假设节点的名称存储在 .name 中
        n = prev[n]
    return s
```

容易看出， Dijkstra 算法并不是找出某个起点到**某个**终点之间的最短路径，而是找出它到所有节点之间的最短路径。它的方式是这样的：对于我们考虑的起点 `start`，一个中间点 `u` 和下一个中间点 `m`，首先让 `start` 到 `u` 之间的距离最短，这样的话，从 `start` 经过 `u` 到达 `u` 相邻的点 `m` 之间的最短距离，也就是从 `start` 到 `u` 的最短距离加上 `u` 到 `m` 的距离。（`注1`）依次遍寻各个可能的中间节点，就得出了这样一个距离；而依照节点的顺序，总是能够经过不断的更新而得到真正的最短距离。

**练习**

写出 Dijkstra 算法的时间复杂度。

这里我们就遇到了动态规划（Dynamic Programming，DP）。动态规划是一种算法设计的思想，它和贪心有些类似，都要依靠目前所能得到的最好结果。所不同的是，它的当前最优会得到更新。而它运用的前提则是所谓的“无后效性”：当我们寻找图中从A点到B点的最短路径时，我们不关心这之间都会经过哪里，只关心所得到的距离是最近的就好。这样的话，就可以利用之前得到的各种其它两点间的最短路径来构建我们所需要的两点间的最短路径。这件事情，显然，DFS 或 BFS 也都能做。但在进行搜索时，我们并未保存每次搜索的这种局部状态，于是导致大量重复的求解。比如说，有A、B、C、D、E、F六个节点，两两之间都有边但边长并不符合三角形法则，这时从C出发，CDE是到达E的一条最短路径，而ABCDE是从A到达E的一条最短路径。在寻找A到E的最短路径时，无论是经过了B点还是经过了F点而到达C点，又或者直接经过C点，BFS / DFS 都将重复求解C点到E点的最短路径，于是就增加了许多重复的工作。动态规划利用了路径访问的无后效性而避免了这一点。

### 启发式搜索和分治策略

但在现实中，我们还可能遇到一些状态会随访问的顺序或路径改变的情况。设想有这样一台小车，它的任务是根据地图的信息，从某个节点出发，采集三个不同类型的样本并最终回到起点。在寻找一条可能的路径方案时，因为每次走到了不同的点就意味着采集到了不同类型的样本，所以访问的中间结果就不是无后效的了；我们对此就很难再用动态规划的方法。

好在除了 BFS / DFS 之外，还有若干种“聪明”一些的搜索方法。比如，我们可以定义一个评价函数，来评估目前状态下，下一步走到各个节点预期的损失或收益。在这个情况下，我们就可以将现在已有的样本类型和数量，与下一个可能节点的距离、样本类型进行比较。代价更小的节点优先得到进一步的处理（搜索求解）。这样，虽然我们不能保证第一个得出的路线就是最优的，但至少它可以比较快地得到，而不像 DFS / BFS 那样可能要等很久。这种有评价函数的搜索叫作启发式搜索。它的时间复杂度和 DFS / BFS 相同，但是在实际运行时，如果选取评价函数得当，会快一些得到结果。

此外，动态规划中实际上还隐藏了一种分而治之的思想。寻找A到E的最短路径被分割为寻找A到B、C、D、F各点的最短路径，而这又可以进一步拆分（或相互关联而使结果得到重复利用）。这就是分治策略（divide and conquer）。分治策略不仅是一种算法设计的思想，而且是一种分割求解问题的思想。


### 随机化算法：蒙特卡洛

最后，正如我们在启发式搜索中牺牲了解的最优性而为了得到一个解，如果我们进一步愿意忍受错误的解的话，我们可以采用一些随机化了的方法来在有限的时间和代价下获得结果。这其中著名的例子便是蒙特卡洛算法。譬如说，我们有一个非负函数$f$，要求其$x$在$(a, b)$上的定积分。积分可以视作求解$x$轴上$(a, b)$区间内函数图像下方到$x$轴之间所夹的阴影面积。如果我们无法知道这个被积函数的表达式，或者这个表达式过于繁冗，以至于难以事先计算出它的不定积分（或并不存在），我们就可以随机地选择一些$(x, y)$坐标点，代入函数之中，通过比较 $f(x)$ 与 $y$ 就可以判断这个点是否在阴影面积中。多随机几次，我们便能够得到这个面积的估计值。这样，尽管我们完全不知道这个函数有什么表达式，但仍然计算出了它的不定积分的近似数值解。当然，由于运气的原因，这个解也完全有可能是错误的。

```python
def MonteCarlo(f, a, b, miny=0., maxy=100., iters=10000): # 假设被积函数的值总是在 [0, 100] 之间，默认随机取 10000 个点
    import random
    def rand(l, u):
        return l + random.random() * (u - l)
        
    totalSpace = (b - a) * (maxy - miny)
    hit = 0
    
    for i in range(0, iters):
        x = rand(a, b)
        y = rand(miny, maxy)
        if f(x) > y: hit += 1
    
    return hit * totalSpace / float(iters)

if __name__ == '__main__':
    for i in range(0, 5):
        print('Run %d: %.4f' % (i + 1, MonteCarlo(lambda x: x**2+1, 0, 1, 0, 2)))
```

输出：

```
Run 1: 1.3158
Run 2: 1.3508
Run 3: 1.3506
Run 4: 1.3308
Run 5: 1.3400
```

**练习**

写出上述蒙特卡洛方法求定积分的时间复杂度。

而我们知道，$f(x)=x^2+1$ 的不定积分是 $F(x)=x^3/3+x+C$ ，所以 $f(x)$ 在 $(0, 1)$ 上的定积分是 $F(1)-F(0)=4/3$，这就显示出了蒙特卡洛方法的误差。当然，我们可以通过增加随机选取的次数来提高精度。这里便存在着随机次数（意味着更多时间）和精确度之间的平衡。而我们常常两者都不能兼顾到。这也就是数据结构与算法让我们发现的现实，同时也是那个真正的屏幕之外的“计算机世界”。

### 并非结语的结语

和友邻的讨论使关于数据结构与算法分析的这部分过早地结束了。当然，有非常多的东西还没有讲，而我仍然认为数据结构和算法本应作为最好的 Python 语言和自然语言的共同讨论对象。不过看来现在来写这部分还为时尚早，希望有朝一日可以将它完善。

[第一部分：语言](1-python.md) [第三部分：网站](3-web.md)
