import numpy as np
import pandas as pd

books = pd.read_csv('../data/BX-Books.csv', on_bad_lines='skip', sep=';', dtype={3: str}, encoding="latin-1")
books.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher', 'imageUrlS', 'imageUrlM',
                 'imageUrlL']


def year_of_publication():
    global books
    # 检查 yearOfPublication 发布时间属性的唯一值
    print(
        books.yearOfPublication.unique())  # 发布商名称 'DK Publishing Inc' 和 'Gallimard' 在数据集中被错误地加载为 yearOfPublication
    # 此外，某些值是字符串，并且在某些地方已将相同年份作为数字输入，我们将对这些行进行必要的更正，并将 yearOfPublication 的数据类型设置为 int
    print(books.loc[books.yearOfPublication == 'DK Publishing Inc', :])  # bookAuthor 错误地装载了 bookTitle，因此需要进行修正
    # ISBN '0789466953'
    books.loc[books.ISBN == '0789466953', 'yearOfPublication'] = 2000
    books.loc[books.ISBN == '0789466953', 'bookAuthor'] = "James Buckley"
    books.loc[books.ISBN == '0789466953', 'publisher'] = "DK Publishing Inc"
    books.loc[
        books.ISBN == '0789466953', 'bookTitle'] = (
        "DK Readers: Creating the X-Men, How Comic Books Come to Life (Level "
        "4: Proficient Readers)")
    # ISBN '078946697X'
    books.loc[books.ISBN == '078946697X', 'yearOfPublication'] = 2000
    books.loc[books.ISBN == '078946697X', 'bookAuthor'] = "Michael Teitelbaum"
    books.loc[books.ISBN == '078946697X', 'publisher'] = "DK Publishing Inc"
    books.loc[
        books.ISBN == '078946697X', 'bookTitle'] = (
        "DK Readers: Creating the X-Men, How It All Began (Level 4: Proficient "
        "Readers)")
    print(books.loc[(books.ISBN == '0789466953') | (books.ISBN == '078946697X'), :])
    books.yearOfPublication = pd.to_numeric(books.yearOfPublication, errors='coerce')
    print(sorted(books['yearOfPublication'].unique()))  # 由于该数据集建于 2004 年，我假设 2006 年之后的所有年份都无效，保留两年的，以防数据集可能已更新
    books.loc[(books.yearOfPublication > 2006) | (books.yearOfPublication == 0), 'yearOfPublication'] = np.nan
    books.yearOfPublication = books.yearOfPublication.fillna(round(books.yearOfPublication.mean()))
    books.yearOfPublication.isnull().sum()
    books.yearOfPublication = books.yearOfPublication.astype(np.int32)


year_of_publication()
