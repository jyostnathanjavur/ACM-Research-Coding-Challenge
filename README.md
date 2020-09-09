# ACM Research Coding Challenge (Fall 2020)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using . `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Email the link of your repo to research@acmutd.co with the same email you used to submit your application. Be sure to include your name in the email.

## Question One

![Image of Cluster Plot](ClusterPlot.png)
<br/>
Given the following dataset in `ClusterPlot.csv`, determine the number of clusters by using any clustering algorithm. **You're allowed to use any Python library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file.

SOLUTION

First, I saw a couple of youtube videos on how clustering works and researched several websites to understand the differnt types of algorithms present in clustering. Since I had no prior experience with Python, I had to do some research on the python syntax, I used the source below to learn the basic syntax.I had to install the necessary libraries which gave me a better understanding of this language and k-means clustering. Since there were 150 values provided, the easiest method to group the data into clusters was Centroid Clustering(K-Means Clustering).In that, The elbow method was an easy method for implementation . The main approach of this problem was to pick random centroid points from the data and group the data values based on the similarities and relationship between them. Then find the total number of clusters based on this approach. 

Libraries used

matplotlib, pandas, numpy, scikit-learn

Sources Used

https://www.datacamp.com/community/tutorials/k-means-clustering-python

https://www.programiz.com/python-programming
