# Overview
When it comes to large scale system design (an art in its own), there is not much support out there. It is then worth looking at a selection of theoretical concepts and practical design exercises to rump up skills and be prepared for the interview day.

Pillars to go through this section are:

- Basics of Systems - networking, systems, operating systems and database technologies, in particular with a focus on in-memory and on-storage design. 
- Large Scale System Design - basics of availability, reliability and scalability and design best practices to make sure that complex systems can accommodate those.

Please, refer to the theory section for a selection of refreshers on the topic.

# Problems
Hereafter, the links to a few representative problems solved in all its parts. Solutions adopt the guidelines and framework shared in the theory section. 

## Designing TinyURL
Referring to the [educative.io solution](https://www.educative.io/courses/grokking-the-system-design-interview/m2ygV4E81AR) which is well structured.

Worth watching also this [video](https://www.youtube.com/watch?v=fMZMm_0ZhK4) which walks through a solution.

A few takeaways:
- Generation of identifiers at scale might be a challenge in itself.
- Caching is extremely important to scale the read throughput. 
- Sharing can be tricky, in particular when it comes to identify the partitioning logic and related identifiers.

## Designing Instagram
Referring to the [educative.io solution](https://www.educative.io/courses/grokking-the-system-design-interview/m2yDVZnQ8lG) which is well structured.

A few takeways:
- For massive amount of data, it is challenging to design an object storage able to scale.
- Metadata can be still on a relational database, pointing to an object in the object storage.
- Streaming large amount of data might impact the write throughput, so it is savvy to separate the two.
- Building a timeline is a challenge in its own.

## Designing Twitter
A viable solution can be found [here](https://docs.google.com/drawings/d/17iFpnFFX7q6RXnDlrepxSBtKWEe0OLNfKBhlyqujifw/edit?usp=sharing).

A few takeaways:
- Timeline generation is compute and memory intensive task that requires massive batch capacity
- Separating the Tweet data path from the User management one
- To accommodate the scale, the generation of unique identifiers is required to re-concile the information

## Designing YouTube
A viable solution can be found [here](https://docs.google.com/drawings/d/1uJpAFO8lpkdXaAnc8PyCGdY7bNepzUUWPaHWtKSItrg/edit?usp=sharing).

A few takeaways:
- TBD

## Designing Facebook Messenger
Worth watching also this [video](https://www.youtube.com/watch?v=zKPNUMkwOJE) which walks through a solution.

## Designing Dropbox
A viable solution can be found [here](https://docs.google.com/drawings/d/1qU8GLYwZ7sYXDvI1bztujJU_G1FDZjdHE6H6qVI6F0I/edit?usp=sharing).

A few takeaways:
- Scaling an object storage might be difficult meanwhile ensuring reliability: partitioning/sharding needs to be carefully thought
- Full-text search impact on the overall storage canno be neglected, in particular search volumes may impact on the bandwidth relevantly
- It is always important to keep reads and writes separated, to avoid scalability issues: patterns and so curves of scalability are tendentially different

## Designing Typeahead Suggestion

Worth watching also this [video](https://www.youtube.com/watch?v=fMZMm_0ZhK4) which walks through a solution.

## Designing Facebook's Newsfeed

## Designing Yelp!

## Designing Uber

# References

- [Grokking the System Design Interview](https://www.educative.io/courses/grokking-the-system-design-interview)
- [System Design Interview with ex-Googler](https://www.youtube.com/watch?v=q0KGYwNbf-0)
- [Non-Abstact Design](https://sre.google/workbook/non-abstract-design/)
- [What to Think During NALSD Interview](https://habr.com/en/company/google/blog/436186/)
- [Designing Distributed Systems Using NALSD Flashcards](https://cloud.google.com/blog/products/management-tools/sre-principles-and-flashcards-to-design-nalsd)
- [My Path to Site Reliability Manager](https://danrl.com/writing/path-to-srm/)
- [System Design Interview](https://github.com/checkcheckzz/system-design-interview)