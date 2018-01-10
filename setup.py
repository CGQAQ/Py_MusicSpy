from distutils.core import setup
setup(
    name = 'musicspy',
    packages = ['musicspy'],
    version = '1.0',
    description = 'music crawler',
    author = 'CG',
    author_email = 'm.jason.liu@outlook.com',
    url = 'https://github.com/CGQAQ/Py_MusicSpy',
    download_url = 'https://github.com/CGQAQ/Py_MusicSpy/releases/download/v1.0/musicspy-1.0.tar.gz',
    keywords = ['CG', 'Music', 'Crawler'],
    classifiers = [
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=['requests']
)