# weed_species_classification
Classify Weed Species into 8 class. 

Dataset can be found here - 

For preprocessing ( for my easyness ) - I concatinated the two csv files ( train and test ) and later as separated train, 
test and validiation set.

Data can be loaded as  pytorch tensor using Datasetloader Class.

## MODEL 
Used resnet18 - by changing and training the last layer training the last layer.

1. CrossEntropyLoss

2. SGD ( with learning rate of 0.001 and Momentum of 0.9 )

3. Decaying learning rate by 0.1 every 7 epochs.

4. 10 epochs.

fortunately got 91% accuracy ( on test set )



You can find the saved model here - [Saved Model](https://drive.google.com/open?id=1JQY4GkKsEJwxX7nDyiqXrxnEK9NQGaA1)

For training in CPU it might take a while so better use colab GPU, 
just turn on the GPU instance and run this notebook[Colab Link](https://colab.research.google.com/drive/1pvh4ey8d96voFT7ROD0HQDqcjGtTcZqf?usp=sharing) ( make you you upload the datset in google drive and mount in colab notebook)

## For testing 

The instructions are in the notebook itself.

Either you can train or jsut load the saved Model.

For checking with your image, do consider reading from PIL and using the transform as provided and feed into the trained model( I will add this fucntion soon ).
