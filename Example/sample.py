import simple_image_download.simple_image_download as simp


my_downloader = simp.Downloader()
my_downloader.search_urls('Landscapes',limit=10, verbose=True)

# Get List of Saved URLs in cache
print(my_downloader.get_urls())

# Prints the Whole Cache
print(my_downloader.cached_urls)

# Download + search file
my_downloader.download('spaceship', limit=2)

# Now download all the Searched picture
my_downloader.download(download_cache=True)

# Flush cache
my_downloader.flush_cache()

# Change Directory
my_downloader.directory = 'my_dir/'
# Change File extension type
my_downloader.extensions = '.jpg'
print(my_downloader.extensions)
my_downloader.download('laptop', limit=10, verbose=True)


# Flush cache
my_downloader.flush_cache()
# Example with Google filters
my_downloader.download('space', limit=10, verbose=True, filters={'size': 'l', 'specific_color': 'orange'})