from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='simple_image_download',
    version='0.4',
    description='Downloads raw page from google images and searches for images that can be downloaded',
    long_description=README,
	long_description_content_type='text/markdown',
    license='MIT',
    packages=find_packages(),
    author='Jakub Dobies',
    author_email='kuba.dobies@onet.pl',
    keywords=['google images', 'image downloader'],
    url='https://github.com/RiddlerQ/simple_image_download',
    download_url='https://pypi.org/project/simple_image_download/'
)

install_requires = ['requests','python-magic-bin==0.4.14','progressbar']

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)