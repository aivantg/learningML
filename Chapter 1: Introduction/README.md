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

The first and simplest model we're going to learn about is the linear model: **y = ax + by + cz**.

Here:
* y: Price
* x: Square Footage
* y: # of Bedrooms
* z: # of Floors

What we want to find are the right a, b, and c that will give us a good estimate for the price of our house. The a, b, and c are called our _weights_ (or otherwise known as coefficients). We call them weights because they decide how much each parameter should factor in to the total housing price.

## Step 1: Initializing The Weights and Creating a Loss Function

The first thing we're going to do is **guess**. We're going to let the computer come up with three random numbers for a, b, and c, show it the 500 data points we have for the housing prices in 2004 and see what prices it comes up with. As you might expect, they'll probably be _very_ off, but it's a place to start. The best way to learn is to get your hands dirty so we're about to jump into some real TensorFlow code! But before we can do that, we need to talk about one more concept: the **_Loss Function_**.

A loss function is simply a way for us to know how _off_ our model was. Let's say for the first house in our dataset, the price our model calculates is $4,000 and the actual price is $400,000. Clearly our model is currently pretty bad, but that's not important. We just want a good way to tell _how_ bad it was. It's simpler than you think: _$400,000 - $4,000 = $396,000_ We were off by $396,000.

This seems like a perfectly good loss function! The only problem is that sometimes, our model might overestimate the housing price. It might think that the house was worth $1,000,000. So to avoid having to deal with negative numbers, we'll square the difference between the actual price and the predicted price.

In Sum: Loss Function: **(Actual Price - Predicted Price)^2**

Great! Now we have a model we're going to try and use to predict housing prices and a way to know how off our model is when we give it random weights. Let's get to the code!

**Stop here and check out weights_and_loss.py. Follow the tutorial and come back here and keep reading when you finish!**
