## Getting started

### Using Pipenv

`pip install pipenv`

`pipenv install`

### Running commands

#### Inside the Pipenv shell

`pipenv shell`

`python -m msb`

#### Outside the Pipenv shell

`pipenv run python -m msb`

## Notes

### Security

MacOS has security measures to prevent scripts from having control over the system. You must open **Security & Privacy** under **System Preferences**, and grant Accessibility access to Terminal (or whichever application you will be running the script from).

## Roadmap

1. It seems that high resolution displays cause an issue, due to the sheer amount of pixels between an origin and destination coordinate. The time between points does not work past 0.01, perhaps there is an issue with the level of accuracy, or something else going on.
