from script import load_dataset
from sklearn.datasets import load_iris()

data = load_iris()

def test_columns():
    df = load_dataset(data)
    column_names = list(df.columns)
    assert column_names == ["setosa","versicolor","virginica"]