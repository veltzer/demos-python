"""
Extract links from a ppt file

References:
- https://www.syncfusion.com/kb/8672/how-to-extract-text-from-a-powerpoint-presentation
- https://python-pptx.readthedocs.io/en/latest/#user-guide
"""
import sys
from itertools import islice

from pptx import Presentation


input_filename = sys.argv[1]

presentation = Presentation(input_filename)
slides = presentation.slides
refs = set()
for slide_number, slide in enumerate(islice(slides, None)):
    for v in slide.part.rels.values():
        target: str = v.target_ref
        if target.startswith(".."):
            continue
        refs.add(target)
refs_l = sorted(list(refs))
for ref in refs_l:
    print(ref)
