'''
add ssh and don't use token

[page.md] => [content.html] => [specially-decorated-content.html] => [webpage.html]

# generate html from markdown
	python -m markdown input.md -f output.html
	import markdown

	problem:
		code block not language specific
		=> customize and learn regex?

# only generate edited files
	record last exported save time and compare to current save time
	os.path.getmtime('path-to-file')

# metadata for pages, headers etc.
	have a do-not-convert list (for games etc.)
	manual decoration in content?
		submit page-specific script to replace/overwrite
		create script tag to be converted and loaded (ex: <script: name> or <<define tag name>>)
		organize script and style files?
	format pages
	versions
	links to other pages/img in published dir and not draft. 

	store everything in json
	need to handle renaming. can we do this automatically?

# generate simple js with python
	pyjs

# master script to automate publish
'''

import markdown as md


