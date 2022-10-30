# Prime-Explo

## Introduction

The feature of this program is to build a database with as much prime numbers as possible with some of their properties (eg. is it a Fermat number ?). The main goal is to reach the million of calculated prime numbers.

## Specifications of the computer in charge of calculations

| Host | Swift SF314-42 V1.10 |
|------|-------------------------------------------------------|
| OS | Fedora Linux 36 (Workstation Edition) |
| CPU | AMD Ryzen 5 4500U with Radeon Graphics (6) @ 2.375GHz |

## Installation

First download the source code.

```
cd Wherever/You/Want
git clone https://github.com/Constantin-Hentgen/Prime-Explo.git
```

Then download the necessary Python libraries.

```
pip install numpy
pip install multiprocessing
pip install mysql-connector-python
pip install pathos
pip install matplotlib
```

## Use

First go to `~/src/Main.py` and change the variables according to your needs. Then run the following commands to launch the program.

```
cd ~/src
python3 Main.py
```

## License

Free of use and modification on condition of quoting the original author and inheriting this license.
