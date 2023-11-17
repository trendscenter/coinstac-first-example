# COINSTAC: Simple Averaging

This is a COINSTAC computation which calculates the average of vectors held at different clients.

Suppose there are $S$ sites. Each site has a $d$-dimensional vector $\mathbf{x}_s$ stored as a $d \times 1$ array. The goal of the consortium is to compute the average of the vectors:

$$\bar{x} = \frac{1}{S} \sum_{s=1}^{S} \mathbf{x}_s$$

## Local and aggregator computations

### Local script

The local script at site $s$ does the following:

1. Reads the array $\mathbf{x}_s$ from disk.
2. Sends the array to the aggregator.
3. Waits for the aggregator to send back the the average $\bar{x}$.
4. Stores the average $\bar{x}$ to the output directory as a CSV file.

### Aggregator script

The aggregator does the following:

1. Receives $\{ \mathbf{x}_s : s =1, 2, \ldots, S\}$ from the $S$ sites.
2. Computes the average $\bar{x} = \frac{1}{S} \sum_{s=1}^{S} \mathbf{x}_s$.
3. Sends the average $\bar{x}$ to each site.
4. Deletes the data $\{ \mathbf{x}_s : s =1, 2, \ldots, S\}$.

## Communication and storage specification

**What data must sites provide?**

* the sites need to provide access to the vector $\mathbf{x}_s$

**What is communicated from the sites to the aggregator?**

* the site ID
* the vector $\mathbf{x}_s$

**What intermediate resultes are stored locally at the sites?**

* the sites do not receive any intermediate results

**What intermediate results are stored at the aggregator?**

* the aggregator deletes the messages from the sites after computing the average

**what is the output from the computation?**

This computation produces a single output file:

* *format*: CSV
* *content*: 
  * $d$-dimensional vector $\mathbf{x}_s$
  * ...



