# `youtube-search-python`


*   https://github.com/alexmercerind/youtube-search-python


```shell
pip3 install youtube-search-python
```

```python
from youtubesearchpython import VideosSearch

videosSearch = VideosSearch('NoCopyrightSounds', limit = 2)

print(videosSearch.result())


from youtubesearchpython.__future__ import VideosSearch

videosSearch = VideosSearch('NoCopyrightSounds', limit = 2)
videosResult = await videosSearch.next()
print(videosResult)
```