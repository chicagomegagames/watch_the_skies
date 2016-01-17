# Watch the Skies

This is "The App" created for the Chicago MegaGame Society's playing of Watch
the Skies.

## Setup for development

1. Create a virtualenv with python 3, the path in the `.gitignore` file is
`./venv`.
2. Install the requirements

```bash
virtualenv -p `which python3` venv
pip install -r requirements.txt
```

### Tests

To run tests, just run `nosetests` from the project root.
