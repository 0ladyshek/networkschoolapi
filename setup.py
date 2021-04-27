from setuptools import setup


with open("README.md") as readme:
    long_description = readme.read()


setup(
    name="networkschool",
    version="1.0.0",
    author="0ladyshek",
    author_email="digital@oladyshek.ml",
    description="api для Электронной школы",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/0ladyshek/networkschoolapi",
    packages=["networkschool"],
    license="MIT",
    install_requires=["httpx"],
    python_requires=">=3.7",
)
