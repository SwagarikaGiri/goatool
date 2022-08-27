#!/Users/sgiri/Desktop/Projects/Kihara-TextSummarization/goatools/goatool/bin/python3.9
"""Create/edit sections files and view GO grouping results."""

__copyright__ = "Copyright (C) 2016-2018, DV Klopfenstein, H Tang. All rights reserved."
__author__ = "DV Klopfenstein"

from goatools.cli.wr_sections import WrSectionsCli


def run():
    """Create/edit sections files and view GO grouping results."""
    WrSectionsCli().cli()


if __name__ == '__main__':
    run()

# Copyright (C) 2016-2018, DV Klopfenstein, H Tang. All rights reserved.
