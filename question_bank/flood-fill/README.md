<h2>733. 图像渲染</h2><p>有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。</p>

<p>给你一个坐标&nbsp;<code>(sr, sc)</code>&nbsp;表示图像渲染开始的像素值（行 ，列）和一个新的颜色值&nbsp;<code>newColor</code>，让你重新上色这幅图像。</p>

<p>为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，&hellip;&hellip;，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。</p>

<p>最后返回经过上色渲染后的图像。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
<strong>输出:</strong> [[2,2,2],[2,2,0],[2,0,1]]
<strong>解析:</strong> 
在图像的正中间，(坐标(sr,sc)=(1,1)),
在路径上所有符合条件的像素点的颜色都被更改成2。
注意，右下角的像素没有更改为2，
因为它不是在上下左右四个方向上与初始点相连的像素点。
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>image</code> 和&nbsp;<code>image[0]</code>&nbsp;的长度在范围&nbsp;<code>[1, 50]</code> 内。</li>
	<li>给出的初始点将满足&nbsp;<code>0 &lt;= sr &lt; image.length</code> 和&nbsp;<code>0 &lt;= sc &lt; image[0].length</code>。</li>
	<li><code>image[i][j]</code> 和&nbsp;<code>newColor</code>&nbsp;表示的颜色值在范围&nbsp;<code>[0, 65535]</code>内。</li>
</ul>


 **难度**: Easy

 **标签**: 深度优先搜索、 


------

<h2>733. Flood Fill</h2><p>
An <code>image</code> is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
</p><p>
Given a coordinate <code>(sr, sc)</code> representing the starting pixel (row and column) of the flood fill, and a pixel value <code>newColor</code>, "flood fill" the image.
</p><p>
To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on.  Replace the color of all of the aforementioned pixels with the newColor.
</p><p>
At the end, return the modified image.
</p>
<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
<b>Output:</b> [[2,2,2],[2,2,0],[2,0,1]]
<b>Explanation:</b> 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
</pre>
</p>

<p><b>Note:</b>
<li>The length of <code>image</code> and <code>image[0]</code> will be in the range <code>[1, 50]</code>.</li>
<li>The given starting pixel will satisfy <code>0 <= sr < image.length</code> and <code>0 <= sc < image[0].length</code>.</li>
<li>The value of each color in <code>image[i][j]</code> and <code>newColor</code> will be an integer in <code>[0, 65535]</code>.</li>
</p>

 **difficulty**: Easy

 **topic**: Depth-first Search, 

