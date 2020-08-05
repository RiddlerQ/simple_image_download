Google image downloader
=======================
Python script that lets you search for urls of images from google images using your tags and/or download them automatically onto you computer

Documentation
-------------

1. Installation

   - Download simple-image-download.py from my [github](https://github.com/RiddlerQ/simple_image_download) and use it in your project
   - Use command **pip install simple_image_download**
   
2. Methods

   In my script simple_image_dowload is a class so the correct way to use it in you project would be to import simple_image_download
   from simple_image_download like this **from simple_image_download import simple_image_download as simp** and then create new variable
   for example **response = simp.simple_image_download**.
   
   Next you can use response to activate methods:
   
   - response().download(keywords, limit, extensions={'.jpg', '.png', '.ico', '.gif', '.jpeg'}) -> downloads images to new directory
     - keywords - for instance -> 'bear, Mario'
	 - limit - for instance -> 5
	 
   - response().urls(keywords, limit, extensions={'.jpg', '.png', '.ico', '.gif', '.jpeg'}) -> returns urls of google images
     - keywords - for instance -> 'bear'
	 - limit - for instance -> 5

3. Example
	
	Example are on my [github](https://github.com/RiddlerQ/simple_image_download) in sub-respository named example
	
End
---

If you have any ideas, try pull request or write to me so i will try to add new things in free time.
I know my code is pretty basic but i just started working with python and i needed that class for urls and images to pass my semester so i did only
what i needed. 

I hope that we will make this class more usefull together, i will try to post updates with yours and mine ideas

Ps. Thx to CharlesMogan for adding so many fixes and new features.
