# jupyter-config

This is my modification of jupyter-config. Except few minor settings, it features git-commit-on-save functionality. That is, when you hit _Save_ button, `git add` and `git commit` are run in order (but not with autosave!).

## Autosave

By default, autosave is set to 2 minutes. This may be somewhat disturbing and create lot of noise in the repo. You can change it or turn off entirely on two different ways:
1. Per notebook, inside notebook: enter value in seconds, where 0 means disabled
```       
## save every 30min
%autosave 1800 
```
2. Globally, [using `custom.js`](http://stackoverflow.com/questions/25631344/turn-off-autosave-in-ipython-notebook)

## changing default config dir

By default, config dir is located in `$HOME/.jupyter`. This can be changed by exporting `JUPYTER_CONFIG_DIR` environment variable

```
export JUPYTER_CONFIG_DIR=~/.jupyter_profile2
jupyter notebook --generate-config
```

## TODO

1. ~~Fix for situation when a file is not in git repo~~
2. ~~Option to filter out output results~~ (needs to be enabled in config)
3. Add option for automatic push
4. Add popups to notebook about progress/errors (if possible)
5. Add button for push/pull
6. Create GitContentsManager

## Resources

* [Official docs: File save hooks](http://jupyter-notebook.readthedocs.org/en/latest/extending/savehooks.html)
* [Official docs: Embracing web standards](http://jupyter-notebook.readthedocs.org/en/latest/examples/Notebook/rstversions/JavaScript%20Notebook%20Extensions.html)
* for future:
    * [Notebook extensions](https://carreau.gitbooks.io/jupyter-book/content/notebook-extensions.html) from [Jupyter Community Docs Book](https://www.gitbook.com/book/carreau/jupyter-book/details)
    * [Four Ways to Extend Jupyter Notebook](https://mindtrove.info/4-ways-to-extend-jupyter-notebook/)
    * [(StackOverflow) IPython Notebook: programmatically trigger a cell from JavaScript](http://stackoverflow.com/questions/21470546/ipython-notebook-programmatically-trigger-a-cell-from-javascript)
    * [IPython Notebook: Javascript/Python Bi-directional Communication](http://jakevdp.github.io/blog/2013/06/01/ipython-notebook-javascript-python-communication/)

## License

See LICENSE file in the repo.
