# campus-helper 🎓

A tiny, begginer-friendly Python tool that helps students with everyday campus tasks:
greeting a student, calculating attendance, and converting marks to grades.
It also includes a small static web page.

## Features

- Greet a student by name
- Calculate attendance percentage
- Convert marks to a letter grade
- Show the first N students from a sample list
- A simple `index.html` landing page

## How to run

You need Python 3.8 or newer.

```bash
python main.py greet Asha
python main.py attendance 45 60
python main.py grade 83
python main.py top 3
```

To view the web page, just open `index.html` in your browser.

To run the tests:

```bash
pip install pytest
python -m pytest
```

Some tests fail right now. That is on purpose, so you can recieve points for fixing them!

## How to contribute

We love first-time contributors! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for the
step-by-step guide. Browse the open **Issues** tab, pick one, and send a Pull Request.

Please also follow our [Code of Conduct](CODE_OF_CONDCUT.md).
