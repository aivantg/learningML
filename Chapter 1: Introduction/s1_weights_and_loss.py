# Hello and welcome to the first coding guide in learningML!
# This might be a little hard to follow if you have zero programming
# experience and little math background, so if you find yourself
# having trouble, feel free to check out the main repository page
# for links to good places to start!

# This file is going to walk you through the basics of Tensorflow,
# initalizing weights, and creating a loss function. By the way, any
# line preceded by a "#" is a comment, and the computer ignores those.
# It's recommended to leave yourself notes on why and how code works
# using these!

# These next two lines simply tell the computer to quiet any warnings
# that aren't critical. This way, when we run the code, we'll only see
# what we want to see.
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# This line imports the TensorFlow library and tells the computer to nickname it "tf".
# When the computer reads this line, it knows to prepare the TensorFlow
# library, which will help us do a lot of the tasks we'll have coming up.
import tensorflow as tf

# First off, we want to design the model that you read about earlier.
# This part of the program is going to be reading through the housing prices
# we know, so we can split it up into the parts of the model we know and the
# parts we don't know.

# These three programming variables are "placeholders" for all the housing data
# parameters. We're calling it a placeholder because we're telling the computer
# we'll give it the actual data later, for now, we just want to teach it what to
# do with it.
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
z = tf.placeholder(tf.float32)

# A note about the "tf.float32, that's just us telling the computer what kind
# of number it will be holding. In this case, it's a 32-bit float, or in
# normal language: it's a decimal.

# Next we want to create the weights and bias variable. This is stuff we want
# the computer to figure out, and hence we don't know it.

a = tf.Variable([0.1], tf.float32)
b = tf.Variable([0.2], tf.float32)
c = tf.Variable([0.3], tf.float32)
d = tf.Variable([-0.4], tf.float32)

# You'll notice that this time, between the parentheses, we wrote two different
# things separated by a comma. The first one is a one-dimensional vector, with
# our initial value and the second is again the type of number it's holding.

# I randomly chose those values, but in bigger programs we'd ask the computer
# to do that randomization for us.

# Now, let's make our model! This model is going to take the data it reads
# and predict housing prices with it. It is our "Predicted Price"

linear_model = a*x + b*y + c*z + d

# Now we just need our "Actual Price" which is one of the things we know, so we can
# feed it in as a placeholder.

P = tf.placeholder(tf.float32)

# Now we just need our loss function! Which is going to look exactly like we
# talked about earlier

loss = tf.square(P - linear_model)

# Last thing we need to do is sum up the loss, because we'll be finding a
# different loss for each sample house we look at.

sum_loss = tf.reduce_sum(loss)

# Great! We now have a loss function that will tell us how off we were for a
# set of houses!

# Now let's create our dataset and run Tensorflow! For now we'll just feed
# it things ourselves. For each parameter (# of floors, # of bedrooms, and
# square footage) we'll create an array of 5 numbers. And then we'll create
# one for the corresponding price. We call them "train" because they belong
# to the data we plan to train our algorithm on.

x_train = [200000, 150000, 234949, 112000, 79000] # Square Footage
y_train = [4, 3, 5, 3, 2] # of bedrooms
z_train = [3, 2, 3, 2, 1] # of floors
P_train = [500000, 452000, 700000, 300000, 250000] # Price


# This next stuff just initializes tensor flow and tells it to initialize those
# variables we set earlier to their random values
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# Finally, we "run" our "sum_loss" node. This goes back through the chain,
# and does all the math we set up earlier. If you remember, we created four
# placeholders to hold the "real data", so in this line, we pass in the dummy
# data we made up there and then print the result!
print("Loss: %g"%sess.run(sum_loss, {x: x_train, y: y_train, z: z_train, P: P_train} ))
