import pandas as pd # type: ignore
import sqlalchemy as sa # type: ignore
from sqlalchemy import text # type: ignore
from pathlib import Path

from IPython.display import display # type: ignore
import matplotlib.pyplot as plt # type: ignore

from google.colab import drive # type: ignore
import datetime


# ============================================================
# 🚀 Google Drive + Project Initialization
# ============================================================

def init_project(base_dir: str = "/content/drive/MyDrive/colab_projects/sql_analytics"):
    """
    Mount Google Drive and create the full project directory structure.
    Returns a dictionary of all important paths.
    """

    # Mount Drive (idempotent)
    drive.mount('/content/drive', force_remount=False)

    BASE_DIR = Path(base_dir)

    # Data directories
    DATA_DIR       = BASE_DIR / 'data'
    RAW_DIR        = DATA_DIR / 'raw'
    PROCESSED_DIR  = DATA_DIR / 'processed'

    # Report directories
    REPORTS_DIR    = BASE_DIR / 'reports'
    RESULTS_DIR    = REPORTS_DIR / 'results'
    PLOTS_DIR      = REPORTS_DIR / 'plots'

    # Sub‑directories for clients
    NIKE_DIR            = RESULTS_DIR / 'nike'
    BRITISH_AIRWAYS_DIR = RESULTS_DIR / 'ba'
    META_REVENUE_DIR    = RESULTS_DIR / 'meta'
    CHINOOK_DIR         = RESULTS_DIR / 'chinook'

    # Plot directories
    NIKE_PLOTS_DIR            = PLOTS_DIR / 'nike'
    BRITISH_AIRWAYS_PLOTS_DIR = PLOTS_DIR / 'ba'
    META_PLOTS_DIR            = PLOTS_DIR / 'meta'
    CHINOOK_PLOTS_DIR         = PLOTS_DIR / 'chinook'

    # Source directories
    NOTEBOOKS_DIR = BASE_DIR / 'notebooks'
    SRC_DIR       = BASE_DIR / 'src'

    # Create all directories
    ALL_DIRS = [
        DATA_DIR, RAW_DIR, PROCESSED_DIR,
        REPORTS_DIR, RESULTS_DIR, PLOTS_DIR,
        NIKE_DIR, BRITISH_AIRWAYS_DIR, META_REVENUE_DIR, CHINOOK_DIR,
        NIKE_PLOTS_DIR, BRITISH_AIRWAYS_PLOTS_DIR, META_PLOTS_DIR, CHINOOK_PLOTS_DIR,
        NOTEBOOKS_DIR, SRC_DIR
    ]

    for d in ALL_DIRS:
        d.mkdir(parents=True, exist_ok=True)

    print("📁 Project structure successfully created:")
    print(f"BASE_DIR:          {BASE_DIR}")
    print(f"DATA_DIR:          {DATA_DIR}")
    print(f"RAW_DIR:           {RAW_DIR}")
    print(f"PROCESSED_DIR:     {PROCESSED_DIR}")
    print(f"REPORTS_DIR:       {REPORTS_DIR}")
    print(f"RESULTS_DIR:       {RESULTS_DIR}")
    print(f"PLOTS_DIR:         {PLOTS_DIR}")
    print(f"NOTEBOOKS_DIR:     {NOTEBOOKS_DIR}")
    print(f"SRC_DIR:           {SRC_DIR}")

    return {
        "BASE_DIR": BASE_DIR,
        "DATA_DIR": DATA_DIR,
        "RAW_DIR": RAW_DIR,
        "PROCESSED_DIR": PROCESSED_DIR,
        "REPORTS_DIR": REPORTS_DIR,
        "RESULTS_DIR": RESULTS_DIR,
        "PLOTS_DIR": PLOTS_DIR,
        "NIKE_DIR": NIKE_DIR,
        "BRITISH_AIRWAYS_DIR": BRITISH_AIRWAYS_DIR,
        "META_REVENUE_DIR": META_REVENUE_DIR,
        "CHINOOK_DIR": CHINOOK_DIR,
        "NIKE_PLOTS_DIR": NIKE_PLOTS_DIR,
        "BRITISH_AIRWAYS_PLOTS_DIR": BRITISH_AIRWAYS_PLOTS_DIR,
        "META_PLOTS_DIR": META_PLOTS_DIR,
        "CHINOOK_PLOTS_DIR": CHINOOK_PLOTS_DIR,
        "NOTEBOOKS_DIR": NOTEBOOKS_DIR,
        "SRC_DIR": SRC_DIR
    }


# ============================================================
# 🗄️ SQL Client Wrapper
# ============================================================

# ============================================================
# 🗄️ SQL Client Wrapper (Documented, Clean, Production‑Ready)
# ============================================================

class SQLClient:
    """
    Lightweight SQL execution wrapper for analytics workflows.

    Provides:
    - Persistent SQLAlchemy engine + connection
    - Safe, clean execution of SQL queries
    - Pretty DataFrame display for notebooks
    - AUTOCOMMIT mode for convenience in analytics environments

    Parameters
    ----------
    db_url : str
        Full SQLAlchemy‑compatible database URL.
    """

    def __init__(self, db_url: str):
        """
        Initialize the SQL client and establish a database connection.

        Creates:
        - SQLAlchemy engine
        - AUTOCOMMIT connection (ideal for analytics)
        """
        self.engine = sa.create_engine(db_url)
        self.conn   = self.engine.connect().execution_options(isolation_level="AUTOCOMMIT")

        ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"✅ Connected successfully at {ts}")

    def run(self, sql: str) -> pd.DataFrame:
        """
        Execute a SQL query and return the result as a DataFrame.

        Parameters
        ----------
        sql : str
            Raw SQL query string.

        Returns
        -------
        pd.DataFrame
            Query results.
        """
        return pd.read_sql(text(sql), self.conn)

    def show(self, df: pd.DataFrame, title: str = "", top: int = 20):
        """
        Display the first rows of a DataFrame with a formatted title.

        Parameters
        ----------
        df : pd.DataFrame
            DataFrame to display.
        title : str, optional
            Optional section title printed above the table.
        top : int, optional
            Number of rows to preview (default: 20).
        """
        if title:
            print(f"\n{'═'*60}\n  {title}\n{'═'*60}")

        display(df.head(top))  # type: ignore
        print(f"↳ {len(df):,} rows")



# ============================================================
# 💾 Save Utility
# ============================================================

def save_to_drive(df: pd.DataFrame, filename: str, db_name: str = "nike", base_paths: dict = None):
    """
    Save a DataFrame to the correct client-specific results directory.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to save.
    filename : str
        File name (e.g., 'customers.csv').
    db_name : str
        One of: 'nike', 'ba', 'meta', 'chinook'.
    base_paths : dict
        The dictionary returned by init_project().
    """

    if base_paths is None:
        raise ValueError("❌ 'base_paths' is required. Pass the dictionary returned by init_project().")

    db_name = db_name.lower()

    # Map database name → correct results directory
    results_map = {
        "nike":     base_paths["NIKE_DIR"],
        "ba":       base_paths["BRITISH_AIRWAYS_DIR"],
        "meta":     base_paths["META_REVENUE_DIR"],
        "chinook":  base_paths["CHINOOK_DIR"]
    }

    if db_name not in results_map:
        raise ValueError(f"❌ Unknown db_name '{db_name}'. Expected one of: {list(results_map.keys())}")

    save_dir = results_map[db_name]
    save_dir.mkdir(parents=True, exist_ok=True)

    save_path = save_dir / filename

    df.to_csv(save_path, index=False)
    print(f"💾 Saved → {save_path} ({len(df):,} rows)")



# ============================================================
# 📊 Figure Saving Utility
# ============================================================



def save_fig(filename: str, db_name: str = "nike", base_paths: dict = None):
    """
    Save a Matplotlib figure to the correct client-specific plot directory.

    Parameters
    ----------
    filename : str
        Name of the file to save (e.g., 'revenue_trend.png').
    db_name : str
        One of: 'nike', 'ba', 'meta', 'chinook'.
    base_paths : dict
        The dictionary returned by init_project(), containing plot directories.
    """

    if base_paths is None:
        raise ValueError("❌ 'base_paths' is required. Pass the dictionary returned by init_project().")

    db_name = db_name.lower()

    # Map database name → correct plot directory
    plot_map = {
        "nike":     base_paths["NIKE_PLOTS_DIR"],
        "ba":       base_paths["BRITISH_AIRWAYS_PLOTS_DIR"],
        "meta":     base_paths["META_PLOTS_DIR"],
        "chinook":  base_paths["CHINOOK_PLOTS_DIR"]
    }

    if db_name not in plot_map:
        raise ValueError(f"❌ Unknown db_name '{db_name}'. Expected one of: {list(plot_map.keys())}")

    save_dir = plot_map[db_name]
    save_dir.mkdir(parents=True, exist_ok=True)

    save_path = save_dir / filename

    plt.savefig(
        save_path,
        dpi=130,
        bbox_inches="tight",
        facecolor="#F8F9FA"
    )

    print(f"📊 Figure saved → {save_path}")
