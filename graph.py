import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
# Change CSV file names here
FILE_KR = BASE_DIR / 'KR.csv'
FILE_TW = BASE_DIR / 'TW.csv'

# Change column names to match your CSV
COL_YEAR = 'AD'
COL_RATIO = 'Percentage of Population Aged 65+ (%)'

def load_csv(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, encoding='utf-8-sig')
    df[COL_YEAR] = df[COL_YEAR].astype(int)
    df[COL_RATIO] = df[COL_RATIO].astype(float)
    return df

def main():
    df_kr = load_csv(FILE_KR)
    df_tw = load_csv(FILE_TW)

    # You can customize chart appearance here!
    plt.figure(figsize=(10, 6))  # Change chart size
    plt.plot(df_kr[COL_YEAR], df_kr[COL_RATIO], marker='o', label='South Korea')  # Change marker and label
    plt.plot(df_tw[COL_YEAR], df_tw[COL_RATIO], marker='s', label='Taiwan')      # Change marker and label
    plt.title('Change in Percentage of Population Aged 65+ (South Korea vs Taiwan)')  # Change title
    plt.xlabel('Year (AD)')           # Change X-axis label
    plt.ylabel('Percentage of Population Aged 65+ (%)')  # Change Y-axis label
    plt.grid(alpha=0.3)
    plt.legend()
    plt.xticks(sorted(set(df_kr[COL_YEAR]).union(df_tw[COL_YEAR])), rotation=45)
    plt.tight_layout()
    output_file = BASE_DIR / 'graph.png'  # Change output filename
    plt.savefig(output_file, dpi=150)     # Change image quality (dpi)
    plt.show()

if __name__ == '__main__':
    main()
