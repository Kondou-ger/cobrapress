#!/usr/bin/python3

class generate(object):
	def __init__(self, config):
		self.config = config

	def translate_markdown(self, markdown):
		"""
		generate a post from given markdown
		"""

		from .thirdparty import markdown

		html = markdown.markdown(str(markdown), extensions=self.config["markdown_extensions"])
		return html

