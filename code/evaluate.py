import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve,auc

def plot_loss(history):
    history_frame = pd.DataFrame(history.history)
    history_frame.loc[:, ['loss', 'val_loss']].plot()
    plt.title('Training and validation loss')

def plot_accurancy(history):
    history_frame = pd.DataFrame(history.history)
    history_frame.loc[:, ['accuracy', 'val_accuracy']].plot()
    plt.title('Training and validation accurancy')

def test_accuracy(model,test_data, test_labels):
    test_loss, test_accuracy = model.evaluate(test_data, test_labels)
    print(f'Test Accuracy: {test_accuracy * 100:.2f}%')


def plot_roc_curve(model,test_data, test_labels):
    y_pred = model.predict(test_data)
    fpr, tpr, _ = roc_curve(test_labels, y_pred)
    roc_auc = auc(fpr, tpr)

    print(f'Test AUC-ROC: {roc_auc}')

    # Plot ROC curve
    plt.figure(figsize=(8, 8))
    plt.plot(fpr, tpr, lw=2, label='ROC curve (area = {:.2f})'.format(roc_auc))
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend(loc='lower right')
    plt.show()