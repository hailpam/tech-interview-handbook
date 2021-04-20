# Overview
When it comes to large scale system design (an art in its own), there is not much support out there. It is then worth looking at a selection of theoretical concepts and practical design exercises to rump up skills and be prepared for the interview day.

Pillars to go through this section are:

- Basics of Systems - networking, systems, operating systems and database technologies, in particular with a focus on in-memory and on-storage design. 
- Large Scale System Design - basics of availability, reliability and scalability and design best practices to make sure that complex systems can accommodate those.

Please, refer to the theory section for a selection of refreshers on the topic.

This [video](https://www.youtube.com/watch?v=UzLMhqg3_Wc) is a nice walkthrough about all skills required to tackle successfully a system design interview.

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

Worth watching also this [video](https://www.youtube.com/watch?v=VJpfO6KdyWE) which walks through a solution.

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
- Very large objects like videos are hard to scale and keep reliably: the amount of storage may be prohibitive, and it might be worth looking at alternatives to pure replication
- Streaming very large amount of data poses challenges in terms of scalability of the front-end services which might be able to load balance according to the less busy service

## Designing Facebook Messenger
Worth watching also this [video](https://www.youtube.com/watch?v=zKPNUMkwOJE) and this [other] one which walk through a solution.

A few takeaways:
- Thinking about mobile devices is tricky: it is required to track the health and the sessions.
- A few helper tables are required to make the communication happen.
- The platform should work as a store and forward solution which allows to deal with users which are offline but are addressed by messages.
- Implementing security might become straighforward using helper tables and leveraging pre-known encryption keys: devices themselves encrypt, the data will be stored encrypted on the storage.

## Designing Dropbox
A viable solution can be found [here](https://docs.google.com/drawings/d/1qU8GLYwZ7sYXDvI1bztujJU_G1FDZjdHE6H6qVI6F0I/edit?usp=sharing).

A few takeaways:
- Scaling an object storage might be difficult meanwhile ensuring reliability: partitioning/sharding needs to be carefully thought
- Full-text search impact on the overall storage canno be neglected, in particular search volumes may impact on the bandwidth relevantly
- It is always important to keep reads and writes separated, to avoid scalability issues: patterns and so curves of scalability are tendentially different

## Designing Typeahead Suggestion
Worth watching also this [video](https://www.youtube.com/watch?v=fMZMm_0ZhK4) which walks through a solution.

A few takeaways:
- Distributed Tries are very handy to implement prefix-based search.
- Ranking may be stored directly in the Trie, requiring then some special attention in terms of scalability.
- Ingestion and data collection for ranking is a challenging task in its own: prefixes need to be ranked in order to provide a relevant and precise user experience.

## Designing TikTok
Worth watching also this [video](https://www.youtube.com/watch?v=Z-0g_aJL5Fw&t=36s) which walks through a solution.

A few takewaways:
- Like for the YouTube case, the video size might be an issue and the caching is very important
- Two important levels of caching: internal caching and external caching. Internal caching might be just a simple Redis/Memcached, instead external caching might be a CDN.
- Separation of endpoints and specific design for each it is very important: make sure that there is consistency.
- The choice between SQL Vs NoSQL is subtle. In case of metadata, if the volumes are not outrageously big, SQL might work just fine as it is very optimized for write and read.

## Designing Facebook's Newsfeed
TBD. Maybe, a good exercise! :)

## Designing Yelp!
TBD. Maybe, a good exercise! :)

## Designing Uber
TBD. Maybe, a good exercise! :)



# References

- [Grokking the System Design Interview](https://www.educative.io/courses/grokking-the-system-design-interview)
- [System Design Interview with ex-Googler](https://www.youtube.com/watch?v=q0KGYwNbf-0)
- [Non-Abstact Design](https://sre.google/workbook/non-abstract-design/)
- [What to Think During NALSD Interview](https://habr.com/en/company/google/blog/436186/)
- [Designing Distributed Systems Using NALSD Flashcards](https://cloud.google.com/blog/products/management-tools/sre-principles-and-flashcards-to-design-nalsd)
- [My Path to Site Reliability Manager](https://danrl.com/writing/path-to-srm/)
- [System Design Interview](https://github.com/checkcheckzz/system-design-interview)
- [System Design Interview Channel](https://www.youtube.com/channel/UC9vLsnF6QPYuH51njmIooCQ)
- [Exponent Interview Channel]()