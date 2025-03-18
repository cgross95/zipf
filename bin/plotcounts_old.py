"""
Plot the counts of words in a csv against their inverse ranks.
"""

import pandas as pd
import argparse


def plot_frequencies(df, xlim, xvar='word_frequency', yvar='inverse_rank'):
    """Plot a data frame of word_frequencies against inverse ranks."""
    scatplot = df.plot.scatter(x=xvar,
                               y=yvar,
                               figsize=[12,6],
                               grid=True,
                               xlim=xlim)
    fig = scatplot.get_figure()
    return fig


def compute_rank(df, rank_var="word_frequency"):
    """Compute the rank and inverse_rank  of frequencies in a data frame."""
    df['rank'] = df[rank_var].rank(ascending=False,
                                   method='max')
    df['inverse_rank'] = 1 / df['rank']
    return df


def main(args):
    """Run the program."""
    df = pd.read_csv(args.infile, header=None,
                     names=('word', 'word_frequency'))
    df = compute_rank(df)
    fig = plot_frequencies(df, xlim=args.xlim)
    fig.savefig(args.outfile)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Input CSV file')
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
