#!/usr/bin/python3

from os import listdir
from shutil import copyfile

class generate(object):
	def __init__(self, config):
		self.config = config

	def generate_html(self):
		"""
		generate static html
		"""
		posts = self.generate_post_html()
		print(posts)
		templates = self.generate_template_html()

		for template in templates:
			if True: # If theres a post to insert
				pass# Somehow merge posts and templates here

			# write template to the proper location now
			templateoutput = open(self.config['htmldir'] + template[0], 'w')
			templateoutput.write(template[1])
			templateoutput.close()

			

	def generate_template_html(self):
		"""
		generate html from templates
		returns a list with lists in it - [x][0] is the filename, [x][1] is the html
		"""
		return [["index.html", "<html></html>"]] # dummy

	def generate_post_html(self):
		"""
		generate html from all posts and return a list with all posts and their metadata
		[x][0] is the metadata, [x][1] is the post
		"""

		files = listdir("posts")
		del files[0]
		posts = []
		print(files)
		for post in files:
			markdownfile = open("posts/"+post, 'r')
			markdowntext = markdownfile.read()
			markdownfile.close()
			print(markdowntext)
			translated = self.translate_markdown(markdowntext)
			posts.append(translated)

		return posts

	def translate_template(self, templatepath, templatename, params):
		"""
		Translate a template file to html
		"""

		from jinja2 import Environment, FileSystemLoader

		env = Environment(loader=FileSystemLoader(templatepath))
		rendered = env.get_template(templatename).render(params)

		return [templatename, rendered]

	def translate_markdown(self, markdowntext):
		"""
		generate a post from given markdown
		returns a list, [0] are the infos, [1] is the html
		"""

		from .thirdparty import markdown
		import re

		regex = re.compile(r"\+\+\+(.+?)\+\+\+(.+)", re.DOTALL)
		matches = regex.match(markdowntext)

		#try:
		html = markdown.markdown(matches.groups(2), extensions=self.config["markdown_extensions"])
		#except AttributeError:
		#	print(markdowntext + "does not look like markdown!")
		#	exit(6)

		return [matches.groups(1), html]

