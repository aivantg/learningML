## Step 1: Initializing The Weights and Creating a Loss Function

The first thing we're going to do is **guess**. We're going to let the computer come up with three random numbers for a, b, and c, show it the 500 data points we have for the housing prices in 2004 and see what prices it comes up with. As you might expect, they'll probably be _very_ off, but it's a place to start. The best way to learn is to get your hands dirty so we're about to jump into some real TensorFlow code! But before we can do that, we need to talk about one more concept: the **_Loss Function_**.

A loss function is simply a way for us to know how _off_ our model was. Let's say for the first house in our dataset, the price our model calculates is $4,000 and the actual price is $400,000. Clearly our model is currently pretty bad, but that's not important. We just want a good way to tell _how_ bad it was. It's simpler than you think: _$400,000 - $4,000 = $396,000_ We were off by $396,000.

This seems like a perfectly good loss function! The only problem is that sometimes, our model might overestimate the housing price. It might think that the house was worth $1,000,000. So to avoid having to deal with negative numbers, we'll square the difference between the actual price and the predicted price.

In Sum, Loss Function: **(Actual Price - Predicted Price)^2**

Great! Now we have a model we're going to try and use to predict housing prices and a way to know how off our model is when we give it random weights. Let's get to the code!

If you've downloaded this entire repository onto your computer, open up s1_weights_and_loss.py on your computer in your favorite code editor and start reading there! If you haven't downloaded the repo or don't know what I'm talking about, just create a new file using your code editor, name it s1_weights_and_loss.py, and copy everything that's online into that file and follow along.  

Check out the setup folder for instructions on how to use a code editor and run python files if you're not sure how to!

**Stop here and check out s1_weights_and_loss.py. Follow the tutorial and open up StepTwo.md when you're ready to continue**
