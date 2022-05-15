from django.db import models
from wagtail.core.models import Page # Page allows you to assign models into the wagtail tree structure
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.search import index
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from cms.blocks import CodeBlock

# Goals:
# - Get Blog Page Index fields
# - Display list of blog pages on blog index
# - Style Blog Index Page

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
    subpage_types = ['ContentPage']


class ContentTag(TaggedItemBase):
    """ See: https://docs.wagtail.org/en/stable/reference/pages/model_recipes.html#tagging """
    content_object = ParentalKey('cms.ContentPage', on_delete=models.CASCADE, related_name='tagged_content')

class ContentPage(Page):
    """
    A Content Page used for basic article content.
    """
    tags = ClusterTaggableManager(through=ContentTag, blank=True)
    date = models.DateField("Post date")
    body = StreamField([

        ('richtext', blocks.RichTextBlock(features=[
                    'h3','h4','h5','h6','bold','italic','ol',
                    'ul','hr','link','document-link', 'embed',
                    'superscript','subscript','strikethrough','blockquote'])),
        ('code', CodeBlock()),
        ('image', ImageChooserBlock()),
    ])

    # Search index Configuration
    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('date'),
    ]

    # Editor Panels Configuration
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        StreamFieldPanel('body'),
        FieldPanel('tags'),
    ]