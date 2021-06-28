from setuptools import setup

setup(
    name = "filtered_lru_cache",
    description = "a version of the @lru_cache decorator that allows specifying which results can be cached",
    version = "0.1.0",
    author = "Ferdinand Bachmann",
    author_email = "theferdi265@gmail.com",
    packages = ["filtered_lru_cache"],
    entry_points = {},
    python_requires = ">=3.5"
)
