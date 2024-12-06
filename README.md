<div align="center"><h1 align="center"> PostScript Interpreter </h1></div>

<!-- Table of Contents -->
<details open="open">
<summary align="center"><h2 id="table-of-contents"> 📖 Table of Contents </h2></summary>
<hr style="margin:0">
<a href="#general"><strong> ➤ General </strong></a><br>
<a href="#start"><strong> ➤ Getting Started </strong></a><br>
<a href="#owner"><strong> ➤ Owner </strong></a>
</details>


<!-- General -->
<div align="center"><h2 id="general">
📃 General
</h2></div>
<p align="justified">
<h4>Summary:</h4>
&emsp;This project uses Python to interpret Terminal inputs as PostScript commands and execute them. After each command, the operand stack will be shown to the user for convenience.
<h4>Supported Commands:</h4>
<ul>
    <li>"exch" - swap the top two items of the operand stack</li>
    <li>"pop" - remove the top item of the operand stack</li>
    <li>"copy" - create copies of the items at the top of the operand stack</li>
    <li>"dup" - create a copy of the top item of the operand stack</li>
    <li>"clear" - empty the operand stack</li>
    <li>"count" - prints the number of items in the operand stack</li>
    <li>"if" - given a bool and a procedure, perform the procedure if bool is true</li>
    <li>"ifelse" - given a bool and 2 procedures, perform the first procedure when true, or the second procedure when false</li>
    <li>"for" - given i, j, k, proc, do proc from i to k in steps of j</li>
    <li>"repeat" - given n, proc, do proc n times</li>
    <li>"eq" - given any1, any2, return true / false if the items are equivalent</li>
    <li>"ne" - given any1, any2, return true / false if the items are not equivalent</li>
    <li>"ge" - given any1, any2, return true / false if any1 >= any2</li>
    <li>"gt" - given any1, any2, return true / false if any1 > any2</li>
    <li>"le" - given any1, any2, return true / false if any1 <= any2</li>
    <li>"lt" - given any1, any2, return true / false if any < any2</li>
    <li>"true" - add bool True to operand stack</li>
    <li>"false" - add bool False to operand stack</li>
    <li>"length" - given str, print length of string</li>
    <li>"get" - given str, ind, print the character at str[ind]</li>
    <li>"getinterval - given str, ind, count, print the substring from str[ind]..str[ind+count-1]</li>
    <li>"putinterval - given str1, ind, str2, replace str[ind] with str2</li>
    <li>"and" - given 2 bools or ints, perform logical or bitwise and, respectively</li>
    <li>"not" - given a bool or int, perform logical or bitwise not, respectively</li>
    <li>"or" - given 2 bools or ints, perform logical or bitwise or, respectively</li>
    <li>"dict" - given int, create a dictionary of size int</li>
    <li>"length" - given a dict, print the length of the dict</li>
    <li>"maxlength" - given a dict, print the maximum size of the dict</li>
    <li>"begin" - given a dict in operand stack, add the dict to dictionary stack</li>
    <li>"end" - pop the top dictionary off dictionary stack</li>
    <li>"def" - given key, val, create dict entry in current dict</li>
    <li>"add" - given 2 nums, add the nums</li>
    <li>"sub" - given 2 nums, subtract num2 from num1</li>
    <li>"mul" - given 2 nums, multiply the nums</li>
    <li>"div" - given 2 nums, divide num1 by num2</li>
    <li>"idiv" - given 2 nums, perform integer division on num1 by num2</li>
    <li>"mod" - given 2 ints, perform int1 mod int2</li>
    <li>"abs" - given a num, add its absolute value to the operand stack</li>
    <li>"neg" - given a num, negate it</li>
    <li>"ceiling" - given a non-integer, retrieve the ceil</li>
    <li>"floor" - given a non-integer, retrieve the floor</li>
    <li>"round" - given a non-integer, round to the nearest int</li>
    <li>"sqrt" - given a num, retrieve the square root</li>
    <li>"print" - print the top item from the operand_stack to the terminal</li>
    <li>"==" - print the top item from the operand_stack to the terminal in PostScript interpretation</li>
    <li>"=" - print the top item from the operand_stack to the terminal</li>
</ul>
</p>

<!-- Getting Started -->
<div align="center"><h2 id="start">
💨 Running the Project
</h2></div>
Open this project in your favorite code editor, and simply run Main.py. All commands should be given in the terminal, and the appropriate outputs will be printed until 'quit' is given as an input.


<!-- Owner Info -->
<div align="center"><h2 id="owner"> 🧑‍🎓 Meet the Owner </h2></div>
<table> 
  <tr align="left">
    <th><b> Name </b></th>
    <th><b> Github </b></th>
    <th><b> E-mail </b></th>
  </tr>
  <tr align="left">
    <th> Tristan Miller </th>
    <th><a href="https://github.com/Obskyur"> Obskyur </a></th>
    <th> ecchojude@gmail.com </th>
  </tr>
</table>
<p>
&emsp;I am currently a Software Engineering major attending Washington State University.
</p>
