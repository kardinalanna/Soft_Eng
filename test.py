from youtube_search import YoutubeSearch

def searcher(text):
    res = YoutubeSearch(text, max_results=1).to_dict()
    return res


def test_Searcher():
    search_list = ["pepe the frog - music clip", "Как (почти) понять «Евангелион»"]
    answer = [{'id': 'vJMP7RBsoms', 'thumbnails': ['https://i.ytimg.com/vi/vJMP7RBsoms/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLAdscd5RtMB7g8mF3yRyq6W4rXZow', 'https://i.ytimg.com/vi/vJMP7RBsoms/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLD4XGjj19jucNVNC00Wlc7wGDdIMA'], 'title': "Pepe the frog - music clip (Marvel83' - Golden Dawn)", 'long_desc': None, 'channel': 'sad pepe frog', 'duration': '5:02', 'views': '2\xa0098\xa0486 просмотров', 'publish_time': '11 months ago', 'url_suffix': '/watch?v=vJMP7RBsoms'}, {'id': 'eKX9UEnD5ug', 'thumbnails': ['https://i.ytimg.com/vi/eKX9UEnD5ug/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLBJNdhSfqrYlNc1GNUJqTRJKkGSsA', 'https://i.ytimg.com/vi/eKX9UEnD5ug/hq720.jpg?sqp=-oaymwEXCNAFEJQDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBXiwWDsHblWiIYU-d61oVtAF1MrA'], 'title': 'Как (почти) понять «Евангелион»', 'long_desc': None, 'channel': 'Кинопоиск', 'duration': '21:09', 'views': '1\xa0766\xa0599 просмотров', 'publish_time': '1 year ago', 'url_suffix': '/watch?v=eKX9UEnD5ug'}]
    for ind, search in enumerate(search_list):
        res = searcher(search)[0]
        for key in res.keys():
            if key != 'views':
               assert res[key] == answer[ind][key]

def test_emptry_query():
    search_list = ["", ".?.,", "^^^^", "/..", "<.>"]
    answer = []
    assert searcher("") == answer
    for search in search_list:
        print(search)
        assert searcher(search) == answer