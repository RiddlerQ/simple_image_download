# Google image downloader
=======================
Python script that lets you search for urls of images from google images using your tags and/or download them automatically onto you computer


## Documentation
-------------

### 1. Installation

Download simple-image-download.py from my github and use it in your project
Use command pip install simple_image_download

#### Note on Windows for [python-magic 0.4.18](https://pypi.org/project/python-magic/) which is used for this Project
You'll need DLLs for libmagic [Here](https://pypi.python.org/pypi/python-magic-bin/0.4.14)  the includes binaries to PyPI.
##### **Or Just run:**
``` pip install python-magic-bin==0.4.14```
##### Window 64-bit!!!
If you are using a 64-bit build of python, you'll need 64-bit libmagic binaries which can be found here: https://github.com/pidydx/libmagicwin64. 
Drop the dlls in C:\Windows\System32 and python magic will import correctly.
-- Newer version can be found here: https://github.com/nscaife/file-windows.


---------------------------------------------------------------------------------------------------------------

### 2. Quickstart

The main class is  Download import it in your project as so:
```
from simple_image_download import Downloader simp 
```
Then create a new class instance
```
response = simp.simple_image_download()
```
Next you can use response to activate methods:
```
response.download(keywords, [limit])
```
 
### Downloads Images
```
from simple_image_download import Downloader simp 
 
response = simp.simple_image_download()
response.download(‘bear supermario’, limit=5)
 
```
#### Get Only the Pictures URL and Store them in the Class cache:

```
from simple_image_download import Downloader simp 
response = simp.simple_image_download()
response.search_urls(‘bear supermario’, limit=15)
 
for url in response.cache:
    print(url)
 
```
 
---------------------------------------------------------------------------------------------------------------
 
### 3. API
 
#### *class* simple_image_download.Downloader(extensions=None)
 
**Parameters**:
* extension -- Type of extension allowed to be downloaded, if left None defaults are:
 {‘.jpg’, ‘.png’, ‘.ico’, ‘.gif’, ‘.jpeg’}
 
-------------------------------------------------------------

#### Functions
 
#### search_urls(keywords, limit, verbose=False, cache=True, timer=None)
 
This functions returns and Caches URLs of Pictures based on:
 
1. Keywords for the search
2. File Extensions based on the class instance you define
3. How many picture per keyword you need with the limit parameter
 
* verbose => Output the links in the terminal in real time

* cache => if set to False, the URLs won’t be stored in the class instance, default is True

* timer => Default is set to 100_000 Looks up, defines the number of WebPages's 'chunks' will search. In the function scan_webpage a 100_000 lookkup means that it will loop up to 100_000 before stop.

Usefule in case of a picture that is not been found, so won't allow to loop indefinitely.
 
#### download(keywords, limit, verbose=False, cache=True, download_cache=False, timer=None)

This functions downloads pictures into defined class instance’s directory:
 
1. Keywords for the search
2. File Extensions based on the class instance you define
3. How many picture per keyword you need with the limit parameter
4. The directory is named after the Keyword.
5. Pictures have a unique ID, so that multiple downloads can persome
 
* verbose => Output the links in the terminal in real time

* cache => if set to False, the URLs won’t be stored in the class instance, default is True

* download_cache => allows to download all the URLs stored in the Downloader's instance Cache. Remember to clear the cache afterwards with Downloader.flush_cache

* timer => Default is set to 100_000 Looks up, defines the number of WebPages's 'chunks' will search. In the function scan_webpage a 100_000 lookkup means that it will loop up to 100_000 before stop.

Usefule in case of a picture that is not been found, so won't allow to loop indefinitely.
 
#### flash_cache():
 
Clears the class instance’s cache which is stored in instance.cached_urls

-------------------------------------------------------------
 
#### Properties
 
#### directory
 
The directory where the Picture are saved, default is in ‘simple_images/’.
You can set the default directory like this:
```
my_downloader = simp.simple_image_download()
my_downloader.directory = ‘my_dir/bla/’

```

#### get_dirs


Set of all sub Direcotories where the picture where saved .
 
#### cached_urls

 
All of the cached urls perfomed with the seach of the function Downloader.get_urls()

Is a Dictionary with this schema:

{'file_name': [Dir_path, URL_content]}
 
User Downloader.flash_cache() to clear it or run mydownloader.download(download_cache=True)
to download the whole content.

---------------------------------------------------------------------------------------------------------------


### 3. Example

	
	Example are on my [github](https://github.com/Koubae/simple_image_download/tree/master/Example) 
	
End
---

If you have any ideas, try pull request or write to me so i will try to add new things in free time.
I know my code is pretty basic but i just started working with python and i needed that class for urls and images to pass my semester so i did only
what i needed. 

I hope that we will make this class more usefull together, i will try to post updates with yours and mine ideas

Ps. Thx to CharlesMogan for adding so many fixes and new features.
