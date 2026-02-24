# ipfsspec-example

A minimal example of reading files from IPFS using [ipfsspec](https://github.com/fsspec/ipfsspec) and [fsspec](https://filesystem-spec.readthedocs.io/).

## Requirements

- Python 3.14+
- [uv](https://github.com/astral-sh/uv)

## Setup

```bash
uv sync
```

## Usage

```bash
uv run main.py
```

This fetches two files from IPFS via the `https://ipfs.io` gateway and prints the number of bytes retrieved for each.