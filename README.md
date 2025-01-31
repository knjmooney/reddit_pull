# reddit_pull

## Dependencies
The python script uses the requests module which you can download with pip

``` shell
pip install requests --user
```

## Conky Script
To use the conky script, you will need reddit_pull in your PATH
`reddit_pull` in your `PATH`. if `$HOME/bin` is in your `PATH`, then
the simplest way is

``` shell
mkdir ~/bin
ln -s /path/to/reddit_pull.py ~/bin/reddit_pull
```

You can then start conky with

``` shell
conky -c /path/to/reddit_pull/default.conky
```

## Contributing
This is designed for conky v1.10+. The conky config is now written in
Lua. The Sourceforge page seems to be out of date (conky v1.8). Use
the [github wiki](https://github.com/brndnmtthws/conky/wiki/) to read
up on the current syntax. Also see `man conky` in your shell.
