import os
from setuptools import setup

from virtualmethod import __version__

def main():
    cwd = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(cwd, 'README.txt')
    readme = open(path, 'rb').read()

    setup(
        name = 'virtualmethod',
        version = __version__,
        description = 'Decorator to prevent base class methods from being called directly.',
        license = 'Apache 2.0',
        author = 'Brad Greenlee',
        author_email = 'brad@footle.org',
        keywords = ['decorator', 'virtual method'],
        url = 'http://github.com/bgreenlee/virtualmethod',
        packages = ['virtualmethod'],
        classifiers = [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: POSIX :: Linux",
            "Operating System :: Unix",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: 2.7",
            "Topic :: Software Development :: Libraries :: Python Modules",
            ],
        long_description = readme
        )


if __name__ == '__main__':
    main()