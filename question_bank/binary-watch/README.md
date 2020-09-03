<h2>401. 二进制手表</h2><p>二进制手表顶部有 4 个 LED 代表<strong> 小时（0-11）</strong>，底部的 6 个 LED 代表<strong> 分钟（0-59）</strong>。</p>

<p>每个 LED 代表一个 0 或 1，最低位在右侧。</p>

<p><img src="https://upload.wikimedia.org/wikipedia/commons/8/8b/Binary_clock_samui_moon.jpg" style="height: 300px;"></p>

<p>例如，上面的二进制手表读取 &ldquo;3:25&rdquo;。</p>

<p>给定一个非负整数 <em>n&nbsp;</em>代表当前 LED 亮着的数量，返回所有可能的时间。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>输入: n = 1
返回: [&quot;1:00&quot;, &quot;2:00&quot;, &quot;4:00&quot;, &quot;8:00&quot;, &quot;0:01&quot;, &quot;0:02&quot;, &quot;0:04&quot;, &quot;0:08&quot;, &quot;0:16&quot;, &quot;0:32&quot;]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>输出的顺序没有要求。</li>
	<li>小时不会以零开头，比如 &ldquo;01:00&rdquo;&nbsp;是不允许的，应为 &ldquo;1:00&rdquo;。</li>
	<li>分钟必须由两位数组成，可能会以零开头，比如 &ldquo;10:2&rdquo;&nbsp;是无效的，应为 &ldquo;10:02&rdquo;。</li>
	<li>超过表示范围（<strong>小时 0-11，分钟 0-59</strong>）的数据将会被舍弃，也就是说不会出现 &quot;13:00&quot;, &quot;0:61&quot; 等时间。</li>
</ul>


 **难度**: Easy

 **标签**: 位运算、 回溯算法、 


------

<h2>401. Binary Watch</h2><p>A binary watch has 4 LEDs on the top which represent the <b>hours</b> (<b>0-11</b>), and the 6 LEDs on the bottom represent the <b>minutes</b> (<b>0-59</b>).</p>
<p>Each LED represents a zero or one, with the least significant bit on the right.</p>
<img src="https://upload.wikimedia.org/wikipedia/commons/8/8b/Binary_clock_samui_moon.jpg" height="300" />
<p>For example, the above binary watch reads "3:25".</p>

<p>Given a non-negative integer <i>n</i> which represents the number of LEDs that are currently on, return all possible times the watch could represent.</p>

<p><b>Example:</b>
<pre>Input: n = 1<br>Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]</pre>
</p>

<p><b>Note:</b><br />
<ul>
<li>The order of output does not matter.</li>
<li>The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".</li>
<li>The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".</li>
</ul>
</p>

 **difficulty**: Easy

 **topic**: Bit Manipulation, Backtracking, 

