# Trojan Horse

A game guise for a nefarious second purpose, non-chalantly named "Trojan Horse".
While the **victim** plays a `2D` platformer with a Troy theme, in a second
process the user's files are encrypted and the encrypted key is sent
to a private server to be ransomed for later on. 😈

This project was made for [CSE
4471](https://cse.osu.edu/courses/information-security-4471) at [Ohio State University](https://www.osu.edu/)

## Screenshots

![Start Screen](./screenshots/start_screen.png)

## Installation

Install [Python](https://www.python.org/downloads/)

```sh
# In project directory

$ pip install pipenv --user
$ pipenv install
```

if Pip doesn't install `pygames` for whatever reason download it [here](https://www.pygame.org/downloads.shtml)

## Running

```sh
$ pipenv run python src/main.py
```

### Backend

```sh
$ pipenv run python src/server/app.py
```

## Pdf Inator

This project must be submitted with solely `pdf` files, therefore we have a
little script file to make this easier!

```sh
$ pipenv install --dev
# or
$ pip install fpdf --user

$ pipenv run python pdf_inator.py
```

Creates `pdf/` directory which has a copied `pdf` structure of `src/`
