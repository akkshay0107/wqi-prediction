import camelot
import pandas as pd


def extract_pdf(path, outpath, pages):
    tables = camelot.read_pdf(path, pages=f'1-{pages}')
    all_frames = []
    for i in range(len(tables)):
        subtable = tables[i].df
        subtable.drop([0, 1], inplace=True)
        all_frames.append(subtable)
    df = pd.concat(all_frames, ignore_index=False)
    df.to_csv(outpath, index=False)


if __name__ == "__main__":
    extract_pdf("./data/pdf/2022_lake_data.pdf", "./data/csv/2022_lake_data.csv", 55)
