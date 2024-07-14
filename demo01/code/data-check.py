import pandas as pd

# 加载数据集并检查书籍、用户和评分数据集的形状
books = pd.read_csv('../data/BX-Books.csv', on_bad_lines='skip', sep=';', dtype={3: str}, encoding="latin-1")
books.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher', 'imageUrlS', 'imageUrlM',
                 'imageUrlL']
users = pd.read_csv('../data/BX-Users.csv', on_bad_lines='skip', sep=';', encoding="latin-1")
users.columns = ['userID', 'Location', 'Age']
ratings = pd.read_csv('../data/BX-Book-Ratings.csv', on_bad_lines='skip', sep=';', encoding="latin-1")
ratings.columns = ['userID', 'ISBN', 'bookRating']

print(books.shape)
print(users.shape)
print(ratings.shape)

print(
    books.columns)  # ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher','imageUrlS', 'imageUrlM',
# 'imageUrlL'],dtype='object'  其中 'imageUrlS', 'imageUrlM', 'imageUrlL' 我们可以不用进行分析，此处我们进行删除

books.drop(['imageUrlS', 'imageUrlM', 'imageUrlL'], axis=1, inplace=True)
print(books.columns)  # 输出删除后的 columns
print(books.dtypes)  # 检查每个列的数据类型并更正缺失和不一致的条目
