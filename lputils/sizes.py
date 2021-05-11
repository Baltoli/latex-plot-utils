from typing import NewType, Tuple

Points = NewType('Points', float)
PPI = NewType('PPI', float)
Inches = NewType('Inches', float)
ColFrac = NewType('ColFrac', float)
TextFrac = NewType('ColFrac', float)

def default_column_width() -> Points:
    """
    The default width of a document column (in LaTeX points)
    """
    return Points(240.94499)

def default_text_width() -> Points:
    """
    The default width of a document (in LaTeX points)
    """
    return Points(505.89)

def thesis_text_width_in() -> Inches:
    """
    The width of a text block in the Edinburgh thesis style, in inches.
    """
    return Inches(5.70978)

def default_ppi() -> PPI:
    """
    The number of LaTeX points contained in one inch of paper space
    """
    return PPI(72.26999)

def col_fig_size(w: ColFrac, h: ColFrac) -> Tuple[Inches, Inches]:
    """
    Get the size (in inches) of a figure that is specified in the document to
    occupy the stated fraction of the column width.
    """
    colwidth_in = Inches(default_column_width() / default_ppi())
    return (
        Inches(w * colwidth_in),
        Inches(h * colwidth_in)
    )

def text_fig_size(w: TextFrac, h: TextFrac) -> Tuple[Inches, Inches]:
    """
    Get the size (in inches) of a figure that is specified in the document to
    occupy the stated fraction of the text width.
    """
    textwidth_in = Inches(default_text_width() / default_ppi())
    return (
        Inches(w * textwidth_in),
        Inches(h * textwidth_in)
    )

def thesis_fig_size(w: TextFrac, h: TextFrac) -> Tuple[Inches, Inches]:
    """
    Get the size (in inches) of a figure specified in a thesis document to
    occupy the stated fraction of the text width.
    """
    return (
        Inches(w * thesis_text_width_in()),
        Inches(h * thesis_text_width_in())
    )
