
Example of packaging a python app as a .deb using dh-virtualenv
====================================================

 

Setup for ubuntu
-----------------------
- Install the python development packages

```bash
sudo apt-get install python3-setuptools 
sudo apt install python3-venv python3-pip
```

- Create a [virtualenv](https://virtualenv.pypa.io/en/latest/) (so that the latest pip and setuptools  and activate

```bash
pip3 install --upgrade pip
pip3 install --upgrade virtualenv
virtualenv -p python3 venv
or
python3 -m venv venv
source venv/bin/activate
pip install -U pip
pip install -U setuptools
```

- Install the latest dh-virtualenv from source as discussed in step 1 of the 
[dh-virtualenv instructions](http://dh-virtualenv.readthedocs.org/en/0.9/tutorial.html#step-1-install-dh-virtualenv)

- Install pyside in your virtualenv (Requires Qt4)

- Test that the script works before packaging it as a deb
```bash
python main.py
```

Build the example debian package of the GUI
-------------------------------------------
In the folder containing the source

```bash
dpkg-buildpackage -us -uc -b
```

This should build a debian outside the folder

For a full discussion on the setup and files, see the corresponding [blog post](http://blog.birving.com/2015/10/creating-debian-application-from-python.html).


To uninstall the test app

```bash
sudo apt-get remove dtux
```
