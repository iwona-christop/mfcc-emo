from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from json import dumps
from datasets import load_dataset


CRITERION = 'log_loss'
MAX_FEATURES = 'log2'


MODELS = [
    GaussianNB(),
    DecisionTreeClassifier(criterion=CRITERION, max_features=MAX_FEATURES),
    KNeighborsClassifier(n_neighbors=5),
    RandomForestClassifier(criterion=CRITERION, max_features=MAX_FEATURES),
    GradientBoostingClassifier(max_features=MAX_FEATURES),
    MLPClassifier(activation='relu', solver='adam', alpha=0.1)
]


if __name__ == '__main__':
    dataset = load_dataset('json', data_files={
        'train' : 'train.json',
        'test' : 'test.json'
    })

    X_train = dataset['train']['sample']
    y_train = dataset['train']['label']

    X_test = dataset['test']['sample']
    y_test = dataset['test']['label']

    results = {}

    for model in MODELS:
        y_predicted = model.fit(X_train, y_train).predict(X_test)
        results[str(model)] = {'accuracy' : accuracy_score(y_test, y_predicted),
            'precision' : precision_score(y_test, y_predicted, average='macro'),
            'recall' : recall_score(y_test, y_predicted, average='macro'),
            'f1' : f1_score(y_test, y_predicted, average='macro')}

    with open('results.json', 'w') as r_file:
        r_file.write(dumps(results))