number = 1
number = input("how many exercises?")
for i in range(1, int(number) + 1):
    string = "<div class=\"box-exercise\">\n<p class=\"box-legend\"><span>Exercise \(\PageIndex{" + str(i) + "}\)</span></p>\n<p>Add exercises text here.</p>\n<dl>\n<dt><strong class=\"emphasis bold\">Answer</strong></dt>\n<dd>\n<p>Add texts here. Do not delete this text first.</p>\n</dd>\n</dl>\n</div>\n"
    print(string)



