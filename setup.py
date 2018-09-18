import setuptools

setuptools.setup(
    name="seqt",
    version="0.0.2",
    url="https://github.com/jjmurre/seqt",

    author="JJ Murre",
    author_email="jan.murre@catalyz.nl",

    description="Structured Easy Query Templates",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
