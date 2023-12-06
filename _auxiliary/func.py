from pathlib import Path
import urllib.request
import spiceypy as sp

__all__ = ['download_file', 'add_col2tab']


KM2AU = sp.convrt(1, "km", "au")
AU2KM = sp.convrt(1, "au", "km")
R2D = sp.dpr()
D2R = sp.rpd()
SEC2YR = sp.convrt(1, "seconds", "years")

GM_SUN = sp.bodvcd(bodyid=10, item='GM', maxn=1)[1][0]
GM_JUP = sp.bodvcd(bodyid=5, item='GM', maxn=1)[1][0]


def download_file(dl_path, dl_url):
    """ Download files from the Internet.

    Parameters
    ----------
    dl_path : str
        Download path on the local machine, relative to this function.
    dl_url : str
        Download url of the requested file.
    """

    # Make directory if it does not exist
    dl_path = Path(dl_path)
    dl_path.mkdir(parents=True, exist_ok=True)
    # Get the file name from the url
    file_name = dl_url.split('/')[-1]

    # If the file is not present in the download directory -> download it
    if not (dl_path/file_name).exists():
        # Download the file with the urllib  package
        urllib.request.urlretrieve(dl_url, dl_path/file_name)


# %%

# We define a function to add a new column in an already existing database
# table. This code snippet may be helpful in the future
def add_col2tab(con_db, cur_db, tab_name, col_name, col_type):
    """
    This function adds a new column to an already existing SQLite table.
    Setting a new or editing an existing key (primary or foreign) is not
    possible.

    Parameters
    ----------
    con_db : sqlite3.Connection
        Connection object to the SQLite database.
    cur_db : sqlite3.Cursor
        Connection corresponding cursor.
    tab_name : str
        Table name.
    col_name : str
        New column name that shall be added.
    col_type : str
        New column name corresponding SQLite column type.

    Returns
    -------
    None.

    """

    # Iterate through all existing column names of the database table using
    # the PRAGMA table_info command
    for row in cur_db.execute(f'PRAGMA table_info({tab_name})'):

        # If the column exists: exit the function
        if row[1] == col_name:
            break

    # If the column is not existing yet, add the new column
    else:
        cur_db.execute(f'ALTER TABLE {tab_name} '
                       f'ADD COLUMN {col_name} {col_type}')
        con_db.commit()
