# Chapter 1: Introduction to Machine Learning

Welcome to the first chapter of the LearningML Guide! If you haven't already installed TensorFlow from the setup guide, go there first before continuing.

So the first big question we encounter: What exactly _is_ machine learning? And how does it work?

## What is Machine Learning?
In the most basic sense, Machine Learning is a sub-category of Artificial Intelligence where computers are trained to perform a specific task or predict an outcome based on a bunch of parameters.

## How does it work?
Though Machine Learning extends beyond simply this, the core concept can be explored by looking at a basic linear equation.

Let's say we want to predict housing prices in California in the year 2005 based on their square-footage, number of bedrooms, and number of floors (Obviously housing prices are based on a _lot_ more factors, but for simplicity, let's say it's just these three). To help us with our goal, we've been given the square-footage, number of bedrooms, and number of floors for 500 houses sold in 2004.

The first step will be creating a _model_ that we think will be able to give us an accurate representation of the data. This simply means we want to create an equation where we can plug in our three parameters (square-footage, # of bedrooms, and # of floors) and it will spit out the price of our house.

The simplest model is the linear model: **y = ax + by + cz**.

Here:
* y: Price
* x: square-footage
* y: # of bedrooms
* z: # of floors

What we want to find are the right a, b, and c that will give us a good estimate for the price of our house.
