# Docusign Api Client Python PyPackage

Docusign Api Client is a Python library to access services quickly.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install DocusignRestClient
```

## Environment Variables

```bash
DOCUSIGN_ENV: 'dev|prod'
DOCUSIGN_ENCODED_KEYS: 'Encoded keys'
DOCUSIGN_CODE_FROM_URL: 'Code from callback url'
```

### Note

If you don't want to set this variables from global environment you can pass them to class.
You can see usage below

## Usage

```python
from docusign import DocusignService


# Initialize client with
docusign_service = DocusignService()
# or Docusign_service = DocusignService(**kwargs)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
