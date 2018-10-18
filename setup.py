import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = "web-share",
    version = '0.10',
    author = 'Ove Bepari',
    author_email = 'ovebepari@gmail.com',
    description = "A Flask App to Share Files Within the Same Network",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/ovebepari/webshare",
    packages = setuptools.find_packages(),
    include_package_data=True,
    python_requires='>=3',
    classifiers = [
        "Programming Language :: Python :: 3",
    ],
    install_requires=[
        'flask',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'web-share=cli:main',
        ],
    },
)