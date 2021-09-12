<h1 align="center"> pyDM </h1>
<p align="center">
<img src="https://img.shields.io/github/repo-size/magnusjwatson2786/pyDM">
<img src="https://img.shields.io/github/last-commit/magnusjwatson2786/pyDM">
<img src="https://img.shields.io/github/license/magnusjwatson2786/pyDM">
</p>
I got tired of the conventional download managers where finding one with good features, nice UI and being free of cost is impossible.

So this is my attempt at a free multithreaded modern download manager. (Its not that bad)

Made using Python and PySide6 

## Features
- Multithreading
- Modern GUI
- Dark-Themed
- Logging
- Scheduled downloads (to be added)
- Adding Batch/multiple downloads supported (to be added)

## Screenshots
![Alt text](screenshots/img1.png?raw=true "pyDM")
![Alt text](screenshots/img2.png?raw=true "pyDM")

## Dependencies
- [Python]
- [PySide6]
- [Requests]
- [cx-freeze] (for build)

## Run
To run this program, clone it to your local machine using: 
```sh
git clone https://github.com/magnusjwatson2786/pyDM.git
```
then cd to the repo directory and hit:.
```sh
python -m pip install -r requirements.txt --user
python xt.py
```
Or just double-click on the start.bat file to run.

Note:  Mac OS X / Linux users may need to run the following before executing the script.
```sh
chmod +x start.sh
```

## Build
To build this script as an executable, cd to the repo dir on your terminal and hit:

```sh
python setup.py build
```

## Usage

1. Click on the Add(+) button in the side bar.

2. Paste the URL where specified.

3. Select a download folder (Optional).

4. Hit Add.

5. Watch your file get downloaded (or not).

Simple as that!

## License

MIT

**Free Software, Hell Yeah!**

*Happy Coding!*

[//]: # (links)
    
   [Python]: <https://www.python.org/>
   [PySide6]: <https://pypi.org/project/PySide6/>
   [Requests]: <https://pypi.org/project/requests/>
   [cx-freeze]: <https://pypi.org/project/cx-Freeze/>
   [Material Theme UI]: <https://www.material-theme.com/>
