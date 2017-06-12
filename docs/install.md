### Accessing a bash shell

You want to be able to manipuate files and data on your computer without having to use your mouse and cursor, but with your keyboard.
This enable you to manipulate many files at once, and also allows you to automate such processes.
We do this through shell programming.
A common shell language is bash, which we will use in this course.
If your computer runs a Linux or Unix operating system, you should be all set to easily access a bash shell.
If, however, you run Windows, there will be a little bit of work to do in order to access a bash shell.

If you run Windows 10 or higher, this has been made easier for you.
Follow [this guide](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/)
to get started.

If you run an older version of Windows, you will have to resort to using applications like Cygwin to run Linux software on Windows.
See [here](https://www.howtogeek.com/howto/41382/how-to-use-linux-commands-in-windows-with-cygwin/) for how to get started.

On a Mac computer, all you need to do is find the Terminal application located in your Applications/Utilities/ folder.
This is also called a "command line."
You can make sure your shell is running bash by typing
```bash
echo $SHELL
```
If the output is something like "/bin/bash" then you are running bash! If not, you can probably access a bash shell just by typing "bash" into your command line.


### Installing Python

There are a number of ways to install Python and the various packages we will use during the course.
For machines running Linux and Unix, you will likely already have an installation of Python present.
One thing that will be helpful over the course of our exploration of various Python modules is a package-manager.
One powerful and convenient (and free!) package manager is the [Anaconda installation](https://www.continuum.io/Anaconda-Overview). 

While I`d prefer that you use Anaconda for the course, if you already have a Python installation that you really like and works for you, that is fine.
The only requirement is that you use Python 3.0 or higher.

You can get started downloading and installing Anaconda [here](https://www.continuum.io/downloads)


















