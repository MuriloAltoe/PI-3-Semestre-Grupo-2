import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def converte_string(pergunta):
    if str(pergunta).lower() == 'sim':
        pergunta = 1
    elif str(pergunta).lower() == 'não':
        pergunta = 0

    return pergunta

if os.path.exists('files/dados_formatados.csv'):
    print('Arquivo já existente, seguindo!!!')
else:
    df = pd.read_csv('files/dados.csv')

    pergunta1 = 'Você se interessaria mais em comprar este alimento se fizéssemos a entrega em sua residência?'
    pergunta2 = 'Você tem interesse em comida 100% orgânica'
    pergunta3 = 'Há feiras de alimento 100% orgânico onde você mora?'
    pergunta4 = 'Até quanto você estaria disposto a pagar em uma cesta pronta de produtos desta categoria?'

    df[pergunta1] = df[pergunta1].apply(converte_string)
    df[pergunta2] = df[pergunta2].apply(converte_string)
    df[pergunta3] = df[pergunta3].apply(converte_string)
    df[pergunta4] = df[pergunta4].apply(lambda x: float(x.split('R$')[1].strip().replace(',', '.')) if not 'não pagaria' in str(x).lower() else 0.0)

    colunas_remover = ['Carimbo de data/hora',
                    'Quais são os principais motivos que o levam/levariam a comprar produtos orgânicos?',
                    'O quão distante você se deslocaria de onde mora para comprar este tipo de alimento?',
                    'Qual é o seu principal desafio ao comprar produtos orgânicos?']

    df = df.drop(columns=colunas_remover)

    df.to_csv('files/dados_formatados.csv', index=False)

df2 = pd.read_csv('files/dados_formatados.csv')

X = df2.drop('Você tem interesse em comida 100% orgânica', axis=1)
y = df2['Você tem interesse em comida 100% orgânica']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
confusion_mat = confusion_matrix(y_test, y_pred)

print("Acurácia:", accuracy)
print("Precisão:", precision)
print("Revocação(recall):", recall)
print("F1-SCORE:", f1)
print("Matriz de Confusão:\n", confusion_mat)