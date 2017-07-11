# Chapter 1: Introduction to Machine Learning

Welcome to the first chapter of the LearningML Guide! If you haven't already installed TensorFlow from the setup guide, go there first before continuing.

So the first big question we encounter: What exactly _is_ machine learning? And how does it work?

## What is Machine Learning?
In the most basic sense, Machine Learning is a sub-category of Artificial Intelligence where computers are trained to perform a specific task or predict an outcome based on a bunch of parameters.

## How does it work?
Though Machine Learning extends beyond simply this, the core concept can be explored by looking at a basic linear equation.

Let's say we want to predict housing prices in California in the year 2005 based on their square-footage, number of bedrooms, and number of floors (Obviously housing prices are based on a _lot_ more factors, but for simplicity, let's say it's just these three). To help us with our goal, we've been given the square-footage, number of bedrooms, and number of floors for 500 houses sold in 2004.

In this case, square-footage, number of bedrooms, and number of floors are our _parameters_. These are the things we are given in order to try to predict an outcome, in this case: the price of the house.

The first step will be creating a _model_ that we think will be able to give us an accurate representation of the data. This simply means we want to create an equation where we can plug in our three parameters (square-footage, # of bedrooms, and # of floors) and it will spit out the price of our house.

The first and simplest model we're going to learn about is the linear model: **y = ax + by + cz**.

Here:
* y: Price
* x: square-footage
* y: # of bedrooms
* z: # of floors

What we want to find are the right a, b, and c that will give us a good estimate for the price of our house. The a, b, and c are called our _weights_ (or otherwise known as coefficients). We call them weights because they decide how much each parameter should factor in to the total housing price.

## Step 1: Initializing The Weights

The first thing we're going to do is **guess**. We're going to let the computer come up with three random numbers for a, b, and c, show it the 500 data points we have for the housing prices in 2004 and see what prices it comes up with. As you might expect, they'll probably be _very_ off, but it's a place to start. Now enough reading, let's get our hands dirty with the code!
