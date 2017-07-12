# Chapter 1: Introduction to Machine Learning

Welcome to the first chapter of the LearningML Guide! If you haven't already installed TensorFlow from the setup guide, go there first before continuing.

So the first big question we encounter: What exactly _is_ machine learning? And how does it work?

## What is Machine Learning?
In the most basic sense, Machine Learning is a sub-category of Artificial Intelligence where computers are trained to perform a specific task or predict an outcome based on a bunch of parameters.

## How does it work?
Though Machine Learning extends beyond simply this, the core concept can be explored by looking at a basic linear equation.

Let's say we want to predict housing prices in California in the year 2005 based on their square-footage, number of bedrooms, and number of floors (Obviously housing prices are based on a _lot_ more factors, but for simplicity, let's say it's just these three). To help us with our goal, we've been given the square footage, number of bedrooms, and number of floors for 500 houses sold in 2004.

In this case, square footage, number of bedrooms, and number of floors are our _parameters_. These are the things we are given in order to try to predict an outcome, in this case: the price of the house.

The first step will be creating a _model_ that we think will be able to give us an accurate representation of the data. This simply means we want to create an equation where we can plug in our three parameters (square footage, # of bedrooms, and # of floors) and it will spit out the price of our house.

The first and simplest model we're going to learn about is the linear model: **P = ax + by + cz + d**.

Here:
* P: Price
* x: Square Footage
* y: # of Bedrooms
* z: # of Floors

What we want to find are the right a, b, c, and d that will give us a good estimate for the price of our house. If you remember anything from math class, this might involve looking at a large plot of the data and seeing which four values for a, b, c, and d make the graph line up perfectly. In Machine Learning, we let the computer figure out those values so we don't have to do the work!

 The variables a, b, and c are called our _weights_ (otherwise known as coefficients). We call them weights because they decide how much each parameter should factor in to the total housing price. The variable d is our bias term that helps the model factor in things that don't depend on our parameters (like the fact that all houses will probably start at some base cost).

 Now we're going to get our hands dirty with some of the code! Open up StepOne.md to get started.
