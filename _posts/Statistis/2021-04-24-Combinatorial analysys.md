
---
permalink: /Combinatory analysis/
tags:
  - Statistics
layout: single
classes: wide
categories:
  - Statistics
---

<script type="text/javascript" async
src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js? 
config=TeX-MML-AM_CHTML"
</script>


# Combinatorial analysis


## Probability Theory: An Introduction

"What are the chances..." is an expression you probably use very often. Determining the chances of an event occurring is called "probability".

This type of probability is different from the mathematical way of looking at probability, which you can find in probability theory, a branch of mathematics. And in mathematics, you have two broad categories of interpretations on "probability" is - the "physical" and "evidential" probabilities.

The former are also called objective or frequency probabilities and are associated with random physical systems such as flipping coins, roulette wheels, or rolling dice. In such systems, a given type of event tends to occur at a persistent rate, or "relative frequency", in a long run of trials.

The latter is also called Bayesian probability, which can be assigned to any statement whatsoever, even when no random process is involved, as a way to represent its subjective plausibility, or the degree to which the statement is supported by the available evidence. On most accounts, evidential probabilities are considered to be degrees of belief, defined in terms of dispositions to gamble at certain odds.

From that perspective, the fundamental ingredient of probability theory is an *experiment* that can be repeated, at least hypothetically, under essentially identical conditions. This experiment may lead to different outcomes on different *trials* or single performances of an experiment. The set of all possible *outcomes* or results of an experiment is then called a "*sample space*". An *event* is a well-defined subset of the sample space.

Now that you have an idea of the key concepts that you'll be using throughout this tutorial, it's time to also consider some probability symbols that you will also encounter:

| Symbol | Meaning |
| :----: | ------- |
|   ∩    | And     |
|   ∪    | Or      |
|   \|   | Given   |

This means that you have to consider first how many possible ways there are for the coin to land on tails, and the number of possible outcomes. The former is 1, as you have only one possible way to get tails. The latter is 2, as you will either get heads or tails when you flip the coin.

To summarize, the calculation of the probability of an event A will look something like this:

$$
P(A)=\frac{Event\ outcomes\ favorable}{Sample\ space}
$$

In the case of the coin flipping, the probability of the coin landing on tails is  0.5.

There are 52 cards In a standard deck of cards and of those 52 cards, 4 are Aces. If you follow the example of the coin flipping from above to know the probability of drawing an Ace, you'll divide the number of possible event outcomes (4), by the sample space (52):
$$
P(A)=4/52=0.08
$$

```python
# Create function that returns probability percent rounded to one decimal place

def event_probability(event_outcomes, sample_space):
    probability = (event_outcomes / sample_space) * 100
    return round(probability, 1)

# Sample Space
cards = 52

# Determine the probability of drawing a heart
hearts = 13
heart_probability = event_probability(hearts, cards)

# Determine the probability of drawing the queen of hearts
queen_of_hearts = 1
queen_of_hearts_probability = event_probability(queen_of_hearts, cards)

# Print each probability
print(str(heart_probability) + '%')
print(str(queen_of_hearts_probability) + '%')

25.0%
1.9%
```

## Probability with Combinations and Permutations

You have seen in the previous section that determining the size of your sample space is key to calculating probabilities. However, this can sometimes prove to be a challenge!

Fortunately, there are ways to make the counting task easier. Two of these ways are permutations and combinations. In this section, you'll see what both of these concepts exactly mean and how you can use them to calculate the size of your sample space!

### Permutations

Permutations are the number of ways a subset of a specified size can be arranged from a given set, generally without replacement. An example of this would be a 4 digit PIN with no repeated digits. 

As a matter of fact, a permutation is an ordered combination. There are basically two types of permutations, with repetition (or replacement) and without repetition (without replacement).

#### Permutations with repetition

(In other words, there are **n** possibilities for the first choice, THEN there are **n** possibilities for the second choice, and so on, multiplying each time.)

Which is easier to write down using an [exponent](https://www.mathsisfun.com/exponent.html) of **r**:
$$
n^r
$$

#### Permutations without repetition

The probability of having no repeated digits can be calculated by executing the following calculation:

10×9×8×710×9×8×7

You have 10 numbers to choose from, but as you're working without replacement, one option always falls away as you pick a number for the 4-digit pin. This means that in picking the first number for your pin, you'll have 10 numbers to choose from (0 to 9), but for the second number of your pin, you'll only have 9 options to choose from, etc.

$$
nPk=\frac{n!}{(n-r)!}
$$

$$
10P4=10!/(10−4)!
$$

Where n is the number of things to choose from,and we choose r of them, no repetitions, order matters.

```python
# Permutations Code
n = 4
k = 2

# Determine permutations and print result
Permutations = math.factorial(n) / math.factorial(n-k)
print(Permutations)

12.0

# OR

import math
math.perm(4,2)
```

### Combinations

You have seen that when you're working with permutations, the order matters. With combinations, however, this isn't the case: the order doesn't matter. Combinations refers to the number of ways a subset of a specified size can be drawn from a given set, (remember the order does **not** matter now):

#### Combinations without repetition/replacement

The formula, for the number of combinations without repetition/replacement, would be very similar to working out the number of permutations without repetition/replacement; it is simply the same formula but decreased by the number of size r permutations without replacement/repetition:

$$
nCk=\frac{n!}{r!(n-r)!}
$$

And is also known as the [Binomial Coefficient](https://www.mathsisfun.com/data/binomial-distribution.html).

An example here is the following situation where you have your deck of cards, which consists of 52 cards. Three cards are going to be taken out of the deck. How many different ways can you choose these three cards?

This means that your calculation of the combinations will look like this:

$$
52C3=\frac{52!}{3!(52-3)!}
$$ 

Where you clearly see that the numerator is exactly the same formula as the permutations formula that you have just seen, while the denominator is the factorial of the number of cards that you will actually choose.

#### Combinations with repetition/replacement

$$
nCk=\frac{(r+n-1)!}{r!(n-1)!}
$$

There are six combinations of pocket Aces. To find the number of combinations, you first must find the number of permutations.

To determine the number of combinations, simply divide the number of permutations by the factorial of the size of the subset. Try finding the number of starting hand combinations that can be dealt in Texas Hold’em.

###### Python

```python
# Combinations Code
n = 52
k = 2

# Determine Permutations
Permutations = math.factorial(n) / math.factorial(n - k)

# Determine Combinations without replacement
Combinations = Permutations / math.factorial(k)
print(Combinations)

1326.0
```

###### R

```R
# calculate the number of combinations without replacement/repetition
choose(n=24,k=4)
10626

# calculate the number of combinations with replacement/repetition

comb_with_replacement <- function(n, r){
  return(factorial(n + r – 1) / (factorial(r) * factorial(n – 1)))
}

#have 3 elements, choosing 3
comb_with_replacement(52,2)

1378
```

## Independent versus Dependent Events

You have read in the introduction that an event is a well-defined subset of the sample space. Events can be classified into two categories: dependent or independent.

Independent events are events that don't impact the probability of the other event(s). Two events A and B are independent if knowing whether event A occurred gives no information about whether event B occurred.

Dependent events, then, are events that have an impact on the probability of the other event(s).

For example, you draw a card from the deck and then draw a second card from the deck without replacing the first card. In this case, the probability of drawing an Ace the fist draw is not the same as the probability of drawing an Ace on the second draw. After the first card is drawn, the sample space has reduced by 1, from 52 to 51. Depending on what the card was on the first draw, the number of event outcomes may have also changed. If the card was an Ace, there are now only 3 Aces remaining for the second draw.

Let's consider these definitions in formal terms now. Events A and B (which have nonzero probability) are independent if and only if one of the following equivalent statements holds:

$$
P(A∩B)=P(A)P(B)\\

P(A|B)=P(A)\\

P(B|A)=P(B)
$$

Let's consider the following example, where you already know the probability of drawing an Ace on the first draw. Now you need to determine the probability of drawing an Ace on the second draw, if the first card drawn was either a King or an Ace:

###### Python

```python
# Sample Space
cards = 52
cards_drawn = 1 
cards = cards - cards_drawn 

# Determine the probability of drawing an Ace after drawing a King on the first draw
aces = 4
ace_probability1 = event_probability(aces, cards)

# Determine the probability of drawing an Ace after drawing an Ace on the first draw
aces_drawn = 1
aces = aces - aces_drawn
ace_probability2 = event_probability(aces, cards)

# Print each probability
print(ace_probability1)
print(ace_probability2)


7.8
5.9
```

There are a few situations common to poker which are relevant to the concept of dependent events.

## Multiple Events

$$
P(EventA∩EventB)=P(EventA)×P(EventA)
$$

For your deck of playing cards, you could ask yourself the question "What is the probability of getting three Hearts when choosing without replacement?". When you sample or choose without replacement, it means that you choose a card but do not put it back, so that your final selection cannot include that same card. In this case, your probability calculation will be the following: 13/52 x 12/51 x 11/50.

### Mutually Exclusive Events

When you're working with multiple events, you might also have events that are mutually exclusive or disjoint: they cannot both occur. In such cases, you might want to calculate the probability (or the union) of any of multiple mutually exclusive events occurring. In such cases, you don't multiply probabilities, but you simply add together the probability of each event occurring:

$$
P(EventA∪EventB)=P(EventA)+P(EventB)
$$

It's key here to understand that the "OR" component is very important: drawing a heart OR drawing a club are two mutually exclusive events. A heart is a heart and a club is a club. To determine the probability of drawing a heart or drawing a club, add the probability of drawing a heart to the probability of drawing a club.

1. Drawing a heart or drawing a club;

2. Drawing an ace, a king or a queen.

###### Python

```python
# Sample Space
cards = 52

# Calculate the probability of drawing a heart or a club
hearts = 13
clubs = 13
heart_or_club = event_probability(hearts, cards) + event_probability(clubs, cards)

# Calculate the probability of drawing an ace, king, or a queen
aces = 4
kings = 4
queens = 4
ace_king_or_queen = event_probability(aces, cards) + event_probability(kings, cards) + event_probability(queens, cards)

print(heart_or_club)
print(ace_king_or_queen)

50.0
23.1
```

### Non-Mutually Exclusive Events

You can imagine that not all events are mutually exclusive: Drawing a heart or drawing an ace are two non-mutually exclusive events. The ace of hearts is both an ace and a heart. When events are not mutually exclusive, you must correct for the overlap.
$$
P(EventA∪EventB)=P(EventA)+P(EventB)−P(EventA∪EventB)
$$
To calculate the probability of drawing a heart or an ace, add the probability of drawing a heart to the probability of drawing an ace and then subtract the probability of drawing the ace of hearts.

Calculate the probability of the following non mutually exclusive events;

1. Drawing a heart or an ace;
2. Drawing a red card or drawing a face card.

```python
# Sample Space
cards = 52

# Calculate the probability of drawing a heart or an ace
hearts = 13
aces = 4
ace_of_hearts = 1

heart_or_ace = event_probability(hearts, cards) + event_probability(aces, cards) - event_probability(ace_of_hearts, cards)

# Calculate the probability of drawing a red card or a face card
red_cards = 26
face_cards = 12
red_face_cards = 6

red_or_face_cards = event_probability(red_cards, cards) + event_probability(face_cards, cards) - event_probability(red_face_cards, cards)

print(round(heart_or_ace, 1))
print(round(red_or_face_cards, 1))

30.8
61.6
```

### Intersection of Independent Events

The probability of the intersection of two independent events is determined by multiplying the probabilities of each event occurring.

$$
P(EventA∩EventB)=P(EventA)×P(EventB)
$$

If you want to know the probability of drawing an Ace from a deck of cards, replacing it, reshuffling the deck, and drawing another Ace, you multiply the probability of drawing and Ace times the probability of drawing an Ace.

```python
# Sample Space
cards = 52

# Outcomes
aces = 4

# Probability of one ace
ace_probability = aces / cards

# Probability of two consecutive independant aces 
two_aces_probability = ace_probability * ace_probability

# Two Ace Probability Percent Code
two_ace_probability_percent = two_aces_probability * 100
print(round(two_ace_probability_percent, 1))

0.6
```

The probability of drawing two Aces in a row, independently, is 0.592%. What if the second event is dependent?

### Intersection of Dependent Events

The probability of the intersection of two non independent events (Event A & Event B given A) is determined by multiplying the probability of Event A occurring times the probability of Event B given A.

$$
P(EventA∩EventB|A)=P(EventA)×P(EventB|A)
$$

The best starting hand you can have in Texas Hold’em is pocket Aces. What is the probability of being dealt two Aces?

```python
# Sample Space first draw
cards = 52
# Outcomes first draw
aces = 4

# Probability of ace on first draw
first_ace_probability = aces / cards
# Sample Space second draw
cards = cards - 1
# Outcomes second draw
aces = aces - 1

# Probability of ace on second draw after ace on first
second_ace_probability = aces / cards
# Probability of two consecutive aces (dependent)
both_aces_probability = first_ace_probability * second_ace_probability * 100
print(both_aces_probability)

0.45
```

The probability of drawing two dependent Aces in a row is 0.452%. Let's take a look at a couple situations where this comes into play at the poker table.

## Expected Value

When playing a game such as poker, you're fairly concerned with questions such as "how much do I gain - or lose - on average, if I repeatedly play this game?". You can imagine that this is no different for poker, especially when you're a professional poker player!

Now, if the possible outcomes of the game and their associated probabilities can be described by a random variable, then you can answer the above question by computing its **expected value**, which is equal to a weighted average of the outcomes where each outcome is weighted by its probability.

Or, in other words, you simply multiply the Total Value times the probability of winning to get your Expected Value:
$$
ExpectedValue=TotalValue×Probability
$$
What is the expected value if there is $100 (Total Value) in the pot, and your probability of winning the pot is 0.75?

```python
# Initialize `pot` and `probability` variables
pot = 100
probability = 0.75

# Determine expected value
expected_value = pot * probability
print(expected_value)

75.0
```

You're expected value is $75. Expected value is an important concept in poker. Let’s go back to the first flush example to see how to use expected values to your advantage.

#### Examples of probability

1. We seek the probability of no repetition in our sample:

$$
p=\frac{(n)_r}{n^r}
$$

for example, the probability that five consecutive random digits are all different is:

```python
n=10
k=5
c = math.comb(10,5)

p = c*(n**-k)
print(p)

0.00252
```

2. If _n balls are randomly placed into n cells, the probability that each cell will be occupied equals:

$$
n!/n^n
$$

Which is surprisingly small:  for n=7 is only 0.00612.

3. An elevator with r =7 passengers and 10 floors, the probability _p_ that no two passengers leave at the same floor, we assume all passengers have the same probability, then.
    
    ```python
    floors=10
    pas=7
    c = math.comb(10,7)
    
    p = c*(floors**-pas)
    print(p)
    
    1.2e-05
    ```
    
    ##### Subpopulations and partitions
    
    1. **Theorem 1**. Of one or two colors. _r_ flags can be shown in _n_ poles, where N total of poles. For example, numbering flags of the same color can be displayed in _N/r!_ ways. Now suppose that p are the number of  flags with red color (p<r) and blue (q=r-p) flags, it can be still displayed: N/(p! q!).
    
        Finally _p and q can be arranged in exactly_.
        $$
        \frac{(p+q)!}{p!q!}=\binom{p+q}{p}=\binom{p+q}{q}
        $$
        **Theorem 2**. Let be a list of integers _r1+r2+.....+rk = n_, where b can be divided into k parts, and it is not important the order of groups.
        $$
        \frac{n!}{r_1!r_2!...r_k!}
        $$
        For example the probability of an ace to each player in a Bridge table:
    
        52 total cards, 4 players, the number of different situations is equal to:
    
        ```python
        math.factorial(52)/math.factorial(13)**4
        
        5.36e+28
        
        
        (math.factorial(4)*math.factorial(48)*13**4)/math.factorial(52)
        
        0.105
        ```
    
        _Dices_: A throw of ten dice can result as 6^10 different outcomes with equal probabilities, the event of each face can appear three times in as many ways is equal to:
    
        ```python
        math.factorial(10)/(3**6*6**10)
        
        0.000082
        
        math.factorial(10)/(2**6*6**10)
        
        0.00094
        ```
    
### The Hypergeometric distribution

Many combinatorial problems can be reduced to the following form of a population of _n_ elements, where n<sub>2</sub> = n -  n<sub>1</sub>. Where we see the probability of red elements (_k_) and blacks ones (_r - k_).

The hypergeometric distribution can be generalized where the total population _n_ contains several classes of elements, for example it contains three subclasses (n1, n2, and n - n1 -n2) respectively.

If we take a sub sample of size _r_, the probability that contains _k1_ of the first, _k2_ of the second, and _r-k1-k2_ of the last one, can be defined by the analogy:

$$
\binom{n_1}{k_1}\binom{n_2}{k_2}\binom{n-n_1-n_2}{r-k_1-k_2}/\binom{n}{r}
$$
The probability defined by the _hypergeometric distribution_:
$$
q_k= \frac{\binom{r}{k}\binom{n-r}{n_1-k}}{\binom{n}{n_1}}
$$

#### Examples

a.	*Quality inspection*: Sampling inspection of _n_ elements, with red defecting items (n<sub>1</sub>), their number is unknown. Considering a sampling of _r_ with _k_ defecting elements.

```python
n = 25000
n1 = 5000
r = 200
k = 18

qk = (math.comb(r,k)*math.comb(n-r,r-k))/math.comb(n,r)
qk

1.060e-05
```

b.	In case we have to estimate an approximation of total population we could use
$$
n \approx \frac{n_1*r}{k}
$$
Let's see we have a first catch of fishes of 1,000 all had red spots, after releasing them  we did a second catch of 1,000, and in this last one we had 100 fishes with red spots, we don't have the total population, and we would like to have the probability of red spots fishes in the pond.

```python
n1 = 1000
r = 1000
k = 100

n = int(n1*r/k)
n
10000

qk = (math.comb(r,k)*math.comb(n-r,n1-k))/math.comb(n,n1)
qk
0.0442
```

c.	In a bridge game, the probability that a hand of thirteen cards consists of five spades, four hearths, three diamonds and one club is:
$$
\binom{13}{5}\binom{13}{4}\binom{13}{3}\binom{13}{1}/\binom{52}{13} = 0.0053
$$

```python
n=52
n1=13

pk = (math.comb(n1,5)*math.comb(n1,4)*math.comb(n1,3)*math.comb(n1,1))/math.comb(n,n1)
pk

0.0053
```

