from downloader import Downloader
import unittest


class Test(unittest.TestCase):

    # def test_class(self):
    #     my_downloader = Downloader()
    #     self.assertTrue(my_downloader.extensions)
    #     self.assertTrue(my_downloader._directory)
    #     self.assertIn(my_downloader._directory, "simple_images/")
    #     my_second_downloader = Downloader()
    #     my_second_downloader._directory = 'custom_dir/'
    #     self.assertIn(my_second_downloader._directory, 'custom_dir/')
    #     self.assertNotEqual(my_second_downloader._directory, my_downloader._directory)
    #     self.assertFalse(my_downloader.get_dirs)
    #     self.assertIsNotNone(my_downloader.cached_urls)

    def test_search_urls(self):
        """Uncomment The line for testing URLs """
        my_downloader = Downloader()
        # my_downloader.search_urls('test',limit=1)
        # my_downloader.search_urls('test', limit=10, verbose=True)
        # self.assertTrue(my_downloader.search_urls('test spam eggs lumberjack', limit=5, verbose=True))
        # self.assertTrue(my_downloader.search_urls('test spam eggs lumberjack', limit=5, verbose=True, cache=False))
        # self.assertFalse(my_downloader.cached_urls)
        # self.assertTrue(my_downloader.search_urls('test', limit=2, cache=True))
        # self.assertTrue(my_downloader.search_urls('test', limit=2, cache=True))
        # self.assertTrue(my_downloader.search_urls('test', limit=2, cache=False))

    def test_download(self):
        """Uncomment THe line for testing the downloads """
        my_downloader = Downloader()
        # my_downloader.download('test', limit=1)
        # my_downloader.download('test', limit=5, verbose=True)
        # x = my_downloader.cached_urls
        # y = my_downloader.get_urls()
        # my_downloader.download('test', limit=5)

        # my_downloader.download(download_cache=True)


    def test_extension(self):
        my_downloader = Downloader(('.jpg',))
        # print(my_downloader.extensions)
        # my_downloader.search_urls('pizza', limit=2)
        # print(my_downloader.get_urls())
        # my_downloader = Downloader(('.gif',))
        # my_downloader.search_urls('car', limit=2, timer=2)
        # my_downloader.download(download_cache=True)
        # my_downloader.extensions = '.png'
        # my_downloader.download('monkey', limit=2, timer=2)

    def test_custom_dir(self):
        my_downloader = Downloader()
        # my_downloader.directory = 'custom/'
        # print(my_downloader.directory)
        # my_downloader.download('cat')

    def test_flush_cache(self):
        my_downloader = Downloader()
        # my_downloader.search_urls('pizza tomato lamborghini', limit=5, verbose=True)
        # self.assertTrue(my_downloader.get_urls())
        # my_downloader.flush_cache()
        # self.assertFalse(my_downloader.get_urls())



def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)


if __name__ == '__main__':
    run_tests(Test)