# xerox-python

[//]: # (Add an asciicast)

`xerox-python` is a project template that spins up a new python project in about a minute.

> [!WARNING]
> This template is _extremely_ opinionated. It creates a Python project just the way I like.
> It might not be _immediately_ useful for anyone else unless they adapt it to their needs.


## Usage

There branches available that each build a different project type:

- `main`: [Default] Builds a basic python project
- `fastapi`: Builds a basic FastAPI python project
- `flask`: Builds a basic Flask python project
- `typer`: Builds a basic [Typer](https://typer.tiangolo.com/) CLI project
- `typerdrive`: Builds a basic [typerdrive](https://github.com/dusktreader/typerdrive) CLI project


## Local

Clone this repo:

```
git clone git@github.com:dusktreader/xerox-python
```

If you want to use a template besides main, checkout the branch you wish to use.

Then just run `make`:

```bash
make
```


## One line

You can use the following one-line commands to build a project from the selected branch


### `main` branch

```bash
uvx copier copy --trust gh:dusktreader/xerox-python .
```


### `fastapi` branch:

```bash
uvx copier copy --trust gh:dusktreader/xerox-python --vcs-ref=fastapi .
```


### `flask` branch:

```bash
uvx copier copy --trust gh:dusktreader/xerox-python --vcs-ref=flask .
```


### `typer` branch:

```bash
uvx copier copy --trust gh:dusktreader/xerox-python --vcs-ref=typer .
```


### `typerdrive` branch:

```bash
uvx copier copy --trust gh:dusktreader/xerox-python --vcs-ref=typerdrive .
```
