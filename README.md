[![GitHub followers](https://img.shields.io/github/followers/imegeek.svg?style=social)](https://github.com/imegeek)
[![GitHub stars](https://img.shields.io/github/stars/imegeek/base64.svg?style=social)](https://github.com/imegeek)
[![GitHub forks](https://img.shields.io/github/forks/imegeek/base64.svg?style=social)](https://github.com/imegeek)

![base64](https://user-images.githubusercontent.com/63346676/84689658-eb701800-af5e-11ea-8cdd-aeb7e9825cca.jpg)

## **📑 INDEX**

* [**⚙️ Installation**](#installation)
* [**❓ How to use?**](#how-to-use)

<a name="installation"></a>

## ⚙️ Installation

**1. Install Python & Git:**

  * For Windows:

    ```
    winget install Python.Python.3.12
    winget install Git.Git
    ```

  * For Linux:

    ```
    sudo apt-get update
    sudo apt-get install -y git python3
    ```

  * For macOS:

    ```
    brew install python git
    ```

  * For Termux:

    ```
    apt update
    apt install git python -y
    ```

**2. Download repository:**

```

  git clone https://github.com/imegeek/base64

```

**3. Change Directory:**

```
  cd base64
```

<a name="how-to-use"></a>

## ❓ How to use?

- ##### Linux/macOS/Termux:

```
python3 main.py
```

- ##### Windows:
```
python main.py
```

##### Command Line Help:

```
usage: main.py [-h] [--encode text / file | --decode text / file] [--output file_path]

Use this command-line arguments to encode/decode very fast.

options:
  -h, --help            show this help message and exit
  --encode text / file, -e text / file
                        Encode string to base64
  --decode text / file, -d text / file
                        Decode base64 to string
  --output file_path, -o file_path
                        Save output to a file.

Note: Use '\' to ignore existing file path.
e.g: main.py -e \file.txt
```

##### Command Line Usage:
- Encode string to base64:
```
python main.py -e "sometext"
```
- Decode base64 to string:
```
python main.py -d "c29tZXRleHQ="
```

- Encode/Decode from a file:
```
python main.py -e somefile.txt
python main.py -d somefile.txt
```

- Ignore existing file path while encode/decode:
```
python main.py -e \somefile.txt
python main.py -d \somefile.txt
```

- Include '\\' while encode:
```
python main.py -e "\\sometext"
```

- Save encode/decode to a file:
```
python main.py -e "sometext" -o encoded.txt
python main.py -d "c29tZXRleHQ=" -o decoded.txt
```