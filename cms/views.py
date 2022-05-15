from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Notes on Wagtail Models:
# So wagtail's routing works by creating a tree structure of wagtail pages. You assign a page as the root page
# (analogus to assigning a page to "/") and then assign children to it. Children will inform wagtail what the
# url structure ought be. In other words, taking the wagtail page "Foobar" with a slug "bar", and assigning it 
# as a child  to "root page" as the root page, then you can access foobar by going to "domain.com/bar" and 
# access root page by going to "domain.com/"
#
# You can create a wagtail page by making a page model that inherits from wagtail's page model.