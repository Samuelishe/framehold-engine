from wagtail.models import Page


class HomePage(Page):
    parent_page_types = ["wagtailcore.Page"]
    subpage_types: list[str] = []
