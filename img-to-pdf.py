import argparse
from pathlib import Path

from fpdf import FPDF
from PIL import Image


def make_pdf(img_dir_path, output_filename=None):
    path = Path(img_dir_path)
    images = [i for i in path.rglob("*.jpg")]

    if output_filename is None:
        output_filename = Path(path, str(path.name) + ".pdf")

    cover = Image.open(images[0])
    width, height = cover.size

    pdf = FPDF(unit="pt", format=[width, height])

    for i in images:
        pdf.add_page()
        pdf.image(str(i), 0, 0)

    pdf.output(Path(output_filename))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description="A CLI tool to convert a folder of images into a pdf doc."
    )

    ap.add_argument(
        "-d", "--dir", required=True, help="Path to search for filenames.",
    )
    ap.add_argument(
        "-o", "--output", required=False, help="Path of output pdf.",
    )
    args = vars(ap.parse_args())
    make_pdf(args["dir"], output_filename=args["output"])
