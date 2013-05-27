# CobraPress config
# Version 0.0.2

# massive dictionaries, biatch!
config = {
		"url":		"http://example.com/blog",	# make this the location where your blog's index will be
		"title":	"Blog-tastic!",			# the blog's title
		"subtitle":	"This is an awesome blog",	# the blog's subtitle
		"author":	"Somebody I used to know",	# The blog's author (as stated under posts)
		"search":	"https://google.com/search",	# How to search your blog

		"date_format":	["day", "month", "year"],	# what date-format to use

		"rss_feed":	"/feed",			# where your atom feed will be, switch to False to disable

		"link-struct":	"/%year/%month/%day/%title",	# what the link structure should be like

		"posts_per_page": 10,				# how many posts to show before using pages

		"readmore":	"Read more &rarr;",		# what to show after shortened articles

		"asides":	["recent_posts", "github"],

		"markdown_extensions":	["codehilite", "smartypants"],
}
