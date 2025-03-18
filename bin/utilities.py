"""Collection of commonly used functions."""

import sys
import csv
import pandas as pd
import matplotlib.pyplot as plt

def plot_frequencies(df, xlim):
    """Plot a data frame of word_frequencies against inverse ranks."""
    fig, ax = plt.subplots(figsize=[12,6])
    groups = df.groupby('fname')
    for name, group in groups:
        ax.scatter(group.word_frequency, group.inverse_rank,
                   label=name)
    ax.grid(True)
    ax.set_xlim(xlim)
    ax.legend()
    return fig


def compute_rank_df(fname):
    """Compute the rank and inverse_rank  of frequencies in a data frame."""
    df = pd.read_csv(fname, header=None,
                     names=('word', 'word_frequency'))
    df['rank'] = df['word_frequency'].rank(ascending=False,
                                           method='max')
    df['inverse_rank'] = 1 / df['rank']
    print(fname)
    df['fname'] = fname
    return df


def collection_to_csv(collection, num=None):
    """
    Write collection of items and counts in csv format.

    Parameters
    ----------
    collection : collections.Counter
        Collection of items and counts
    num : int
        Limit output to N most frequent items
    """
    collection = collection.most_common()
    if num is None:
        num = len(collection)
    writer = csv.writer(sys.stdout)
    writer.writerows(collection[0:num])
