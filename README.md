# ComicMaker - A Webcomic Site Generator

This is a simple static site generator (SSG) to build a webcomic website, with as little
input as possible. All you need is an ordered set of images, and you're good to
go!

## Installing Python and Setting Up Jinja

*Note: Windows users will likely need to install python (it's preinstalled on
Macs and in most Linux installations - you can download releases from
[python.org](https://www.python.org/downloads/). If unsure which version to use
Python 3.8 is a good choice. Also, when installing, be sure to check to check
the box 'Add Python to PATH' in the installer.*

Once python is installed, you'll need to install the templating library used by
this tool (jinja). Thankfully, python can do this for us.

Open a Terminal (or Powershell for Windows) in the folder where you downloaded this tool.

*Note: If you're new to using a command line, you might want to grab
[Visual Studio Code](https://code.visualstudio.com/). It's a great editor (which
will help when you want to customize things later), and it has a built in
terminal. If you decide to go that route, open the folder containing this tool
with VS Code, and then hit `Terminal > New Terminal`. It will open one in the
correct place.*

Once you have a terminal open, we need to setup a python environment.
  * First we need to setup our virtual environment in the folder `./venv`:
    * Mac/Linux: `python3 -m venv ./venv`
    * Windows: `python -m venv ./venv`
  * We then need to activate it: 
    * Mac/Linux: `. ./venv/bin/activate` (note the leading dot + space)
    * Windows: `./venv/Scripts/activate`
  * Finally we can install the necessary libraries `pip install -r requirements.txt`

We're now ready. Note that in the future we don't need to run `pip` or create a
new venv, but you will need to re-activate the environment whenever you create a
new terminal Window (by running either `. ./venv/bin/activate` for Mac/Linux
users, or `./venv/Scripts/activate` for Windows users).

## Basic Usage

To use, copy your comic images into `comic_pages`, and update `settings.py`
so the title and description are correct. 

You can then run the tool with `python comicmaker.py` 

This will build your webcomic in the `dest/` folder by default. 

You can view the website by running `cd dest` (to move into the output
directory) and `python -m http.server` to start a test server. You can then
navigate to `http://localhost:8000` to see your webcomic on the local machine.

*Hint: If you're running a more recent version of python (3.7+), you can skip the 
`cd dest` command and just run `python -m http.server -d dest/`.*

If you make changes to any of the files (including adding new images), you'll need to rerun
the tool (and rerun the test server command) to see changes.

## Customizing Your Site

You'll likely want to update `templates/header.html` and `templates/footer.html`
to change the content above and below the comic pages itself. 

You can also change `static/style.css` to adjust things like spacing, font, color scheme, 
and more. 

However, it's worth noting that this tool is designed to be a scaffold! Look at the templates
(there are only three, and they're all short)! Feel free to experiment and build your own
thing!

## FAQs

*Can I add text to go with a specific comic?*

Not right now. I may add the ability to add markdown-based posts above/below a comic
in the future if there's demand.

*Can I set alt text?*

Not yet. If we add markdown (see the last question), this will be included too!

*How can I add custom art for headers/footers/etc?*

Any file you add to the `static` folder will be available to the website under `/static`. So,
if you want to add a banner on your site, you could copy it to `static/banner.jpg` and add
an image tag to load from `/static/banner.jpg`. 

*What can I do with the website?*

The output from this tool is portable, basic HTML. You can host it on any provider that
offers static HTML hosting. I would recommend checking out Netlify, Vercel, Surge, and GitHub Pages. All offer generous free tiers.

*I found a bug!*

Please file an issue!