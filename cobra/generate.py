#!/usr/bin/python3

from os import listdir

class generate(object):
	def __init__(self, config):
		self.config = config

	def generate_html(self):
		"""
		generate html from all posts
		"""

		files = listdir("posts")
		del files[0]
		print(files)
		for post in files:
			markdownfile = open("posts/"+post, 'r')
			markdown = markdownfile.read()
			markdownfile.close()
			print(markdown)
			html = self.translate_markdown(markdown)
			print(html)

	def translate_markdown(self, markdown):
		"""
		generate a post from given markdown
		"""

		from .thirdparty import markdown

		html = markdown.markdown(str(markdown), extensions=self.config["markdown_extensions"])
		return html

