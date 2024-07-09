import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name='DocusignRestClient',
    version="0.0.11",
    author="Yaşar Özyurt",
    author_email="blueromans@gmail.com",
    description='Docusign Api Client Python package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/blueromans/Docusign-Python-Client.git',
    project_urls={
        "Bug Tracker": "https://github.com/blueromans/Docusign-Python-Client.git/issues",
    },
    install_requires=['requests', 'python-dotenv', 'docusign-esign'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['docusign', 'docusign.service','docusign.helper'],
    python_requires=">=3.6",
)
