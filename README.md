# solving-polynomials

---

This my submission repository for Polynomial.ai internship task.

---

## Introduction of the problem

 The provided dataset is of Amazon customer reviews of Mobile phones and related products. The problem statement involves making a model to clasify each review as positive negative or neutral.
 
## Approach used
The given dataset has nearly 1 million records and cannot be loaded into memory directly. I have used the chunksize options in pandas.read_json to read 50000 records each time and use it for training the model. As of now I am using the bernoulli naive bayes model from sklearn which supports increamental learning. The reason for not using a neural network based model from the onset is the large amount of time required to train an LSTM or RNN. 

I have used the follwoing convention
- 
## Model Metrics

|                      | precision | recall | f1-score | support |
|----------------------|-----------|--------|----------|---------|
| positive             | 0.64      | 0.68   | 0.66     | 11530   |
| neutral              | 0.22      | 0.23   | 0.22     | 4954    |
| negative             | 0.86      | 0.84   | 0.85     | 33509   |

Accuracy: 0.74
