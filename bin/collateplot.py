"""
Plot the counts of words in multiple csvs against their inverse ranks.
"""

import pandas as pd
import argparse

import utilities as util


def update_ranks(fname, df):
    """
    Update a dataframe containing rank data with data from another
    file.
    """
    new_df = util.compute_rank_df(fname)
    df = pd.concat([df, new_df])
    return df


def main(args):
    """Run the program."""
    df = pd.DataFrame()
    for fname in args.infiles:
        df = update_ranks(fname, df)

    fig = util.plot_frequencies(df, xlim=args.xlim)
    fig.savefig(args.outfile)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infiles', type=str, nargs='*',
                        help='Input file names')
    parser.add_argument('--outfile', '-o',
                        type=str, nargs='?',
                        default='plotcounts.png',
                        help='Output image file name')
    parser.add_argument('--xlim', '-x',
                        type=float, nargs=2,
                        default=None,
                        help='x limits of plot')
    args = parser.parse_args()
    main(args)

