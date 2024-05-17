from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="jupyter-prolog",
    version="0.0.1",
    author="Emmanuel Kieffer",
    author_email="emmanuel.kieffer@lxp.lu",
    description="Prolog IPython magic extension",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/ekieffer/jupyter-prolog",
    packages=find_packages(),
    install_requires=[
        "ipython"
    ],
    classifiers=[
        "Framework :: IPython",
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.1'
)
