import os
import time
import urllib
import requests
import magic
import progressbar
from urllib.parse import quote
from collections.abc import Iterable


class simple_image_download:
    def __init__(self):
        pass

    def urls(self, keywords, limit: int, extensions={'.jpg', '.png', '.ico', '.gif', '.jpeg'}):
        """"
        Get URLs of images by provided keywords

        Arguments:
        -----------
        keywords : str or [str]
            String of keywords separated by column or list of strings (keywords)
        limit : int
            Number of images to download for each keyword
        extensions: set(str)
            Allowed extensions of images to download
        main_directory : str
            directory to store subdirectories for each keyword

        :returns list of URL's
        """

        return self.search(keywords, limit, extensions, should_download_images=False)

    def download(
            self,
            keywords,
            limit: int,
            extensions={'.jpg', '.png', '.ico', '.gif', '.jpeg'},
            main_directory='simple_images/'
    ):
        """
        Downloads 'limit' images to subdirectory of 'main_directory' named same like keyword
        
        Arguments:
        -----------
        keywords : str or [str]
            String of keywords separated by column or list of strings (keywords)
        limit : int
            Number of images to download for each keyword
        extensions: set(str)
            Allowed extensions of images to download
        main_directory : str
            directory to store subdirectories for each keyword
        """

        self.search(keywords, limit, extensions, should_download_images=True, main_directory=main_directory)

    @staticmethod
    def search(
        keywords,
        limit,
        extensions={'.jpg', '.png', '.ico', '.gif', '.jpeg'},
        should_download_images=False,
        main_directory=None
    ):
        if should_download_images:
            simple_image_download._preprocess_output_dir(main_directory)

        keywords_to_search = simple_image_download._preprocess_keywords(keywords)

        bar = simple_image_download._init_bar(num_ticks=len(keywords_to_search) * limit)
        bar.start()

        urls_to_return = []
        for keyword_index in range(len(keywords_to_search)):
            keyword = keywords_to_search[keyword_index]
            urls = simple_image_download._process_keyword(
                keyword=keyword,
                limit=limit,
                extensions=extensions,
                should_download_images=should_download_images,
                main_directory=main_directory
            )
            urls_to_return.extend(urls)

            bar.update(keyword_index + 1)
        bar.finish()

        return urls_to_return

    @staticmethod
    def _process_keyword(keyword, limit, extensions, should_download_images, main_directory):
        if should_download_images:
            simple_image_download._create_keyword_directory(main_directory, keyword)

        raw_html = simple_image_download._download_google_images_page_html_by_keyword(keyword)
        urls = simple_image_download._extract_image_urls_from_html(
            keyword=keyword,
            raw_html=raw_html,
            extensions=extensions,
            limit=limit,
            should_download_images=should_download_images,
            main_directory=main_directory
        )

        return urls

    @staticmethod
    def _preprocess_output_dir(output_dir):
        if output_dir is None:
            raise ValueError(f'Provide a directory to store results')
        else:
            os.makedirs(output_dir, exist_ok=True)
            if len(os.listdir(output_dir)) != 0:
                raise ValueError(f'Directory is not empty: {output_dir}')

    @staticmethod
    def _init_bar(num_ticks):
        return progressbar.ProgressBar(
            maxval=num_ticks,
            widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()]
        )

    @staticmethod
    def _extract_image_urls_from_html(keyword, raw_html, extensions, limit, should_download_images, main_directory):
        end_object = -1
        num_images_found = 0
        image_urls = []

        while num_images_found < limit:
            while True:
                try:
                    new_line = raw_html.find('"https://', end_object + 1)
                    end_object = raw_html.find('"', new_line + 1)

                    buffer = raw_html.find('\\', new_line + 1, end_object)
                    if buffer != -1:
                        object_raw = (raw_html[new_line + 1:buffer])
                    else:
                        object_raw = (raw_html[new_line + 1:end_object])

                    if any(extension in object_raw for extension in extensions):
                        break

                except Exception:
                    break

            try:
                r = requests.get(object_raw, allow_redirects=True, timeout=1)
                if 'html' not in str(r.content):
                    mime = magic.Magic(mime=True)
                    file_type = mime.from_buffer(r.content)
                    file_extension = f'.{file_type.split("/")[1]}'
                    if file_extension not in extensions:
                        raise ValueError()

                    if should_download_images:
                        path = main_directory + keyword.replace(" ", "_")
                        file_name = str(keyword) + "_" + str(num_images_found + 1) + file_extension
                        with open(os.path.join(path, file_name), 'wb') as file:
                            file.write(r.content)

                    image_urls.append(object_raw)
                else:
                    num_images_found -= 1
            except Exception:
                num_images_found -= 1
            num_images_found += 1

        return image_urls

    @staticmethod
    def _preprocess_keywords(keywords):
        if isinstance(keywords, str):
            keywords_to_search = [str(item).strip() for item in keywords.split(',')]
        elif isinstance(keywords, Iterable):
            all_elements_are_strings = all(isinstance(item, str) for item in keywords)
            if not all_elements_are_strings:
                raise ValueError('Provided list should consist of strings')
            keywords_to_search = keywords
        else:
            raise ValueError('keywords argument should be a list of strings or string, separated by commas')

        return keywords_to_search

    @staticmethod
    def _create_keyword_directory(main_directory, name):
        name = name.replace(" ", "_")
        try:
            if not os.path.exists(main_directory):
                os.makedirs(main_directory)
                time.sleep(0.2)
                path = name
                sub_directory = os.path.join(main_directory, path)
                if not os.path.exists(sub_directory):
                    os.makedirs(sub_directory)
            else:
                path = name
                sub_directory = os.path.join(main_directory, path)
                if not os.path.exists(sub_directory):
                    os.makedirs(sub_directory)

        except OSError as e:
            if e.errno != 17:
                raise
            pass
        return

    @staticmethod
    def _download_page(url):

        try:
            headers = {
                'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
            }
            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData

        except Exception as e:
            print(e)
            exit(0)

    @staticmethod
    def _download_google_images_page_html_by_keyword(keyword):
        url = 'https://www.google.com/search?q=' + quote(
            keyword.encode(
                'utf-8')) + '&biw=1536&bih=674&tbm=isch&sxsrf=ACYBGNSXXpS6YmAKUiLKKBs6xWb4uUY5gA:1581168823770&source=lnms&sa=X&ved=0ahUKEwioj8jwiMLnAhW9AhAIHbXTBMMQ_AUI3QUoAQ'
        raw_html = simple_image_download._download_page(url)

        return raw_html
