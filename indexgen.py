# write in markdown and convert to html with script

import os

index_fn = "./index.html"

header = "<h1>minds all the way down</h1>"
wilt_header = "<h2>what i've learned today (basically tweeting in private):</h2>"

f = open(index_fn, "w")

f.write(header + "\n" + wilt_header + "\n")

wilt_list = []
for filename in os.listdir('./wilt'):
	wilt_list.append(filename)

wilt_list.sort(reverse=True)

for i in wilt_list:
	f.write(f"<a href=\"./wilt/{i}\">{i[:-5]}</a>\n")

f.close()
