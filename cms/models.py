from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.search import index
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase

class BlogPageTag(TaggedItemBase):
    """ See: https://docs.wagtail.org/en/stable/reference/pages/model_recipes.html#tagging """
    content_object = ParentalKey('cms.BlogPage', on_delete=models.CASCADE, related_name='tagged_items')


# Goals:
# - Display fields on template page
# - Get Blog Page Index fields
# - Display list of blog pages on blog index
# - Style Blog Page
# - Style Blog Index Page

# Ok. So.
# Wagtail is a CMS, so the idea with wagtail is that we create content, and manage it via wagtail.
# Which means, any sort of page that you want to integrate into an interface means you need to build a page
# (any sort of webpage with custom content) through wagtail's interfacing. That's here in this page.
# 
# So wagtail's routing works by creating a tree structure of pages. You assign a page as the root page
# (analogus to assigning a page to "/") and then assign children to it. Children will inform wagtail what the
# url structure ought be. In other words, assinging the page "Foobar" with a slug "bar" as a child to "root page"
# as the root page, then you can access foobar by going to "domain.com/bar" and access root page by going to "domain.com/"

class BlogIndexPage(Page):
    """
    Index page for blogs.
    """
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
        
    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
    ]
    subpage_types = ['BlogPage'] # Only BlogPages can live under this.

class BlogPage(Page):
    """
    A Blog Page used for basic article content.
    """
    # DB Fields
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")

    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    # Search index Configuration
    search_fields = Page.search_fields + [
        #index.SearchField('body'),
        index.FilterField('date'),
    ]

    # Editor Panels Configuration
    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        StreamFieldPanel('body'),
    ]