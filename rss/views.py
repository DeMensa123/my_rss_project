from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import feedparser
from datetime import datetime

def index(request):

    if request.GET.get('url'):
        url = request.GET['url']    # get URL
        feed = feedparser.parse(url)    # Parse XML data
        #print(feed.feed.keys())
        #print(feed.feed.values())

        # sort entries ascending
        sorted_entries = sorted(feed.entries,key=lambda entry: datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %z'))

        feed['entries'] = sorted_entries

        if request.GET.get('dropdown'):
            dropdown = request.GET['dropdown']
            if (dropdown == 'descending'):
                sorted_entries.reverse()
                feed['entries'] = sorted_entries
                return render(request, 'rss/reader.html', {
                    'feed': feed,
                    'url': url,
                })
            if (dropdown == 'ascending'):
                feed['entries'] = sorted_entries
                return render(request, 'rss/reader.html', {
                    'feed': feed,
                    'url': url,
                })

    else:
        feed = None

    return render(request, 'rss/reader.html', {
        'feed': feed,
    })
