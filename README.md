# Inference Time Calculator

A web application that calculates the minimum number of copies of an AI model to run so that at least one copy fixes a bug, given a single-copy success rate and a target confidence level.

## Live App
https://inference-time-calculator-nuv7xmp5pjaegku8qzaohp.streamlit.app/

## The Math
This project uses the complement rule and independence to calculate the probability that at least one copy succeeds:

P(at least one success) = 1 - (1 - p)^n

To find the minimum number of copies (n) needed to reach a target confidence (T):

n = ceil( ln(1 - T) / ln(1 - p) )

The calculator rounds up because you cannot run a fraction of a copy.

## How to Run Locally
1. Install the requirements:
   pip install -r requirements.txt

2. Run the application:
   python -m streamlit run app.py

## Tech Stack
-Python
-Streamlit
-Pandas
