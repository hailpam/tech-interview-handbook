# Back of the Envelope Calculations

> A back-of-the-envelope calculation is a rough calculation, typically jotted down on any available scrap of paper such as an envelope. It is more than a guess but less than an accurate calculation or mathematical proof.

> In the natural sciences, back-of-the-envelope calculation is often associated with physicist Enrico Fermi, who was well known for emphasizing ways that complex scientific equations could be approximated within an order of magnitude using simple calculations.

When referred to the design of large systems, according to Jeff Dean: 

- Back-of-the-envelope calculations allow you to take a look at different variations.
- When designing your system, these are the kind of calculations you should be doing over and over in your head.
- Know the back of the envelope numbers for the building blocks of your system. It's not good enough to just know - the generic performance numbers, you have to know how your subsystems perform. You can't make decent - back-of-the-envelope calculations if you don't know what's going on.
- Monitor and measure every part of your system so you can make these sorts of projections from real data.

## Fermi Estimation

> In physics or engineering education, a Fermi problem, Fermi quiz, Fermi question, Fermi estimate, order-of-magnitude problem, order-of-magnitude estimate, or order estimation is an estimation problem designed to teach dimensional analysis or approximation of extreme scientific calculations, and such a problem is usually a back-of-the-envelope calculation.

Also known as Fermi Estimation, it allows to make educated guesses using real world data and observations. Very useful when architecting systems and decisions need to be taken for alternatives.

> Scientists often look for Fermi estimates of the answer to a problem before turning to more sophisticated methods to calculate a precise answer. This provides a useful check on the results. While the estimate is almost certainly incorrect, it is also a simple calculation that allows for easy error checking, and to find faulty assumptions if the figure produced is far beyond what we might reasonably expect. By contrast, precise calculations can be extremely complex but with the expectation that the answer they produce is correct. The far larger number of factors and operations involved can obscure a very significant error, either in mathematical process or in the assumptions the equation is based on, but the result may still be assumed to be right because it has been derived from a precise formula that is expected to yield good results. Without a reasonable frame of reference to work from it is seldom clear if a result is acceptably precise or is many degrees of magnitude (tens or hundreds of times) too big or too small. The Fermi estimation gives a quick, simple way to obtain this frame of reference for what might reasonably be expected to be the answer.

A perspective of the back-of-the-envelope calculations:

> If a nice, aesthetically pleasing analytical result were required, much of physics would not have happened. Indeed, the seduction of formal calculations can be a serious hindrance. Whenever the math gets out of hand, it is usually a good idea to relax demands and accept an approach that while imprecise, offers a prayer of moving forward.

Examples of questions that might leverage Fermi's estimation for resolution:

- If the cost of the wars in Afghanistan and Iraq were factored into the price of gasoline for a taxpayer in the United States, what would the effective war tax be per gallon? 
- On the basis of energy per person, what is more effective, solar power or wind?
- How many cracked iPhone screen repairmen are there in the United States? 

The key to master those estimates is to break a problem into appropriate and manageable sub-problems. Therefore an iterative process which incrementally makes educated assumptions or guesses for one or multiple sub-problems requiring those.

Statistically speaking, a typical Fermi estimation process can be modeled as a Random Walk, considering that for N sub-problems the aggregate variance will be N times a sigma square (variance is additive) and so the average displacement becomes square root of t.

## Pareto Law

Also known as the 80/20 rule, it is a power law which governs a number of real-world phenomenon and is actually extremely useful when it comes at driving estimates by making assumptions and educated guesses.

> The Pareto principle states that for many outcomes, roughly 80% of consequences come from 20% of the causes (the “vital few”). Other names for this principle are the 80/20 rule, the law of the vital few, or the principle of factor sparsity

## Pareto Efficiency/Optimality

Selectng alternatives, it is important to refer to the Pareto Efficiency or Optimality.

> Pareto efficiency or Pareto optimality is a situation where no individual or preference criterion can be better off without making at least one individual or preference criterion worse off or without any loss thereof. The concept is named after Vilfredo Pareto (1848–1923), Italian civil engineer and economist, who used the concept in his studies of economic efficiency and income distribution. The following three concepts are closely related:

> Given an initial situation, a Pareto improvement is a new situation where some agents will gain, and no agents will lose. A situation is called Pareto dominated if there exists a possible Pareto improvement. A situation is called Pareto optimal or Pareto efficient if no change could lead to improved satisfaction for some agent without some other agent losing or if there's no scope for further Pareto improvement.

## Order of Magnitude

Numbers that everyone's should know according to Jeff Dean:

- L1 cache reference 0.5 ns
- Branch mispredict 5 ns
- L2 cache reference 7 ns
- Mutex lock/unlock 100 ns
- Main memory reference 100 ns
- Compress 1K bytes with Zippy 10,000 ns
- Send 2K bytes over 1 Gbps network 20,000 ns
- Read 1 MB sequentially from memory 250,000 ns
- Round trip within same datacenter 500,000 ns
- Disk seek 10,000,000 ns
- Read 1 MB sequentially from network 10,000,000 ns
- Read 1 MB sequentially from disk 30,000,000 ns
- Send packet CA->Netherlands->CA 150,000,000 ns 

## Design Tips

- Notice the magnitude differences in the performance of different options.
- Datacenters are far away so it takes a long time to send anything between them.
- Memory is fast and disks are slow.
- By using a cheap compression algorithm a lot (by a factor of 2) of network bandwidth can be saved.
- Writes are 40 times more expensive than reads.
- Global shared data is expensive. This is a fundamental limitation of distributed systems. The lock contention in shared heavily written objects kills performance as transactions become serialized and slow.
- Architect for scaling writes.
- Optimize for low write contention.
- Optimize wide. Make writes as parallel as you can.

# References
- [Jeff Dean's Back of the Envelope Calculations](http://highscalability.com/blog/2011/1/26/google-pro-tip-use-back-of-the-envelope-calculations-to-choo.html)
- [Femi's Estimate](https://brilliant.org/wiki/fermi-estimate/)
- [Pareto's Principle](https://en.wikipedia.org/wiki/Pareto_principle)