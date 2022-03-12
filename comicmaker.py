from re import template
from jinja2 import Environment, select_autoescape, FileSystemLoader
from pathlib import Path
import mimetypes, argparse, shutil, logging
import settings

env = Environment(
    autoescape=select_autoescape(),
    loader=FileSystemLoader("templates")
)

def main():
    args = parseArgs()
    images = getAllComicImagePaths(args.source)

    # make the output dir and images dir
    out = Path(args.output)

    # Clear output dir
    shutil.rmtree(out)

    # build the image folder
    (out / "images").mkdir(parents=True, exist_ok=True)

    # copy over anything in the static directory
    shutil.copytree("./static", out / "static")

    print(f"Building comic with {len(images)} images found in {args.source}")

    # pre-calculate the first and last pages, since they're always
    # the same for each page
    first_page = settings.BASE_URL + images[0].stem + ".html"
    last_page = settings.BASE_URL

    # load our template
    template = env.get_template("main.html")

    for index in range(len(images)):
        prev_item = f"{settings.BASE_URL}{images[index - 1].stem}.html" if index > 0 else first_page
        next_item = f"{settings.BASE_URL}{images[index + 1].stem}.html" if index < len(images)-2 else last_page

        html = template.render(
            COMIC_TITLE = settings.COMIC_TITLE,
            COMIC_DESCRIPTION = settings.COMIC_DESCRIPTION,
            FIRST = first_page,
            LAST = last_page,
            PREV = prev_item,
            NEXT = next_item,
            IMG_SOURCE = "/images/" + images[index].name
        )

        outfile = Path(out / f"{images[index].stem}.html")
        outfile.write_text(html)

        shutil.copy(str(images[index]), str(out / "images"))

    # rename the last item to index.html
    Path(out / f"{images[-1].stem}.html").rename(out / "index.html")

    print(f"Wrote comic files to {out.resolve()}")


def parseArgs():
    p = argparse.ArgumentParser(description="A static site generator for comics.")
    p.add_argument("-o", "--out", dest="output", help="Output directory", default="dest")
    p.add_argument("-s", "--source", help="Directory containing comic pages.", default="comic_pages")
    return p.parse_args()


def getAllComicImagePaths(source = "./comic_pages"):
    """Collect an ordered list of comic page images."""

    p = Path(source)
    files = [x for x in p.iterdir() if x.is_file()]

    return [f for f in sorted(files) if _isImage(f)]


def _isImage(p: Path) -> bool:
    """Determine if the given path is an image, based on mime type"""
    t, e = mimetypes.guess_type(str(p))
    if t and t.startswith("image"): return True
    else: return False

if __name__ == '__main__':
    main()