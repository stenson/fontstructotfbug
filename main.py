from pathlib import Path
from fontTools.pens.recordingPen import RecordingPen

import uharfbuzz as hb


def test(file:Path):
    blob = hb.Blob.from_file_path(file)
    face = hb.Face(blob)
    font = hb.Font(face)
    pen = RecordingPen()

    font.draw_glyph_with_pen(66, pen)

    return len(pen.value)


assert test(Path("fonts/good-future.ttf")) == 28
#assert test(Path("fonts/good-future.otf")) == 20 # with uharfbuzz 0.39.1
assert test(Path("fonts/good-future.otf")) == 0 # with uharfbuzz 0.39.3