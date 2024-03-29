from django.contrib.syndication.views import Feed
from podcast.models import Podcast
from articles.models import Article, Attachment 
class LatestEntriesFeed(Feed):
    title = "Kaitlin and Caitlin in the Morning, at Night"
    link = "/feed/"
    description = "Get the latest episodes of Kaitlin and Caitlin in the Morning, at Night! Hot from the RSS feed and into your ears."

    def items(self):
        return Article.objects.filter(status__is_live=True).order_by('-publish_date')[:15]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_enclosure_url(self, item):
        a = Attachment.objects.filter(article=item)[0]
        return "http://kaitlinandcaitlin.com" + a.attachment.url

    def item_pubdate(self, item):
        return item.publish_date

    def author_name(self):
        return 'Kaitlin and Caitlin'

    def author_link(self):
        return "http://kaitlinandcaitlin.com"

    def item_link(self, item):
        return item.get_absolute_url()

    def item_enclosure_length(self, item):
        return 0

    def item_enclosure_mime_type(self, item):
        return "audio/mpeg"

