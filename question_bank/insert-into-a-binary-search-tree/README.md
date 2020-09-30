<h2>701. 二叉搜索树中的插入操作</h2><p>给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据保证，新值和原始二叉搜索树中的任意节点值都不同。</p>

<p>注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。</p>

<p>&nbsp;</p>

<p>例如,&nbsp;</p>

<pre>给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和 插入的值: 5
</pre>

<p>你可以返回这个二叉搜索树:</p>

<pre>         4
       /   \
      2     7
     / \   /
    1   3 5
</pre>

<p>或者这个树也是有效的:</p>

<pre>         5
       /   \
      2     7
     / \   
    1   3
         \
          4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>给定的树上的节点数介于 <code>0</code> 和 <code>10^4</code> 之间</li>
	<li>每个节点都有一个唯一整数值，取值范围从 <code>0</code> 到 <code>10^8</code></li>
	<li><code>-10^8 &lt;= val &lt;= 10^8</code></li>
	<li>新值和原始二叉搜索树中的任意节点值都不同</li>
</ul>


 **难度**: Medium

 **标签**: 树、 


------

<h2>701. Insert into a Binary Search Tree</h2><p>Given the root node of a binary search tree (BST) and a value to be inserted into the tree,&nbsp;insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.</p>

<p>Note that there may exist&nbsp;multiple valid ways for the&nbsp;insertion, as long as the tree remains a BST after insertion. You can return any of them.</p>

<p>For example,&nbsp;</p>

<pre>
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
</pre>

<p>You can return this binary search tree:</p>

<pre>
         4
       /   \
      2     7
     / \   /
    1   3 5
</pre>

<p>This tree is also valid:</p>

<pre>
         5
       /   \
      2     7
     / \   
    1   3
         \
          4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the given tree will be between <code>0</code> and <code>10^4</code>.</li>
	<li>Each node will have a unique integer value from <code>0</code>&nbsp;to -<code>10^8</code>, inclusive.</li>
	<li><code>-10^8 &lt;= val &lt;= 10^8</code></li>
	<li>It&#39;s guaranteed that <code>val</code> does not exist in the original BST.</li>
</ul>


 **difficulty**: Medium

 **topic**: Tree, 

