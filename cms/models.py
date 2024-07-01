from django.db import models
from django.core.paginator import EmptyPage, Paginator

from wagtail.core.models import Page # Page allows you to assign models into the wagtail tree structure
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.search import index
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from cms.blocks import CodeBlock

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

    def get_context(self, request):
        context = super().get_context(request)

        all_posts = self.get_children().live().order_by('-first_published_at')

        # Paging
        num_per_page  = 5
        paginator = Paginator(all_posts, num_per_page)
        page_num = request.GET.get("page") or '1'
        page = int( page_num ) if page_num.isdigit() else 1 # Try to get the ?page=x value
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
            posts.adjusted_elided_page = paginator.get_elided_page_range(page)
            posts.page = page
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the "Not Found" Page
            posts = []

        context['posts'] = posts
        return context

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