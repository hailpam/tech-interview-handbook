# Traversals
> In computer science, tree traversal (also known as tree search and walking the tree) is a form of graph traversal and refers to the process of visiting (checking and/or updating) each node in a tree data structure, exactly once. Such traversals are classified by the order in which the nodes are visited. The following algorithms are described for a binary tree, but they may be generalized to other trees as well.

> There are three common ways to traverse them in depth-first order: in-order, pre-order and post-order.


![Depth-first Traversals](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Sorted_binary_tree_RGB.svg/2880px-Sorted_binary_tree_RGB.svg.png)

> These searches are referred to as depth-first search (DFS), since the search tree is deepened as much as possible on each child before going to the next sibling. For a binary tree, they are defined as access operations at each node, starting with the current node, whose algorithm is as follows:

```
The general recursive pattern for traversing a binary tree is this:

   Go down one level to the recursive argument N. If N exists (is non-empty) execute the following three operations in a certain order:
       L: Recursively traverse N's left subtree.
       R: Recursively traverse N's right subtree.
       N: Access (visit) the current node N itself.

    Return by going up one level and arriving at the parent node of N.
```

## Pre-order Traversal
> The pre-order traversal is a topologically sorted one, because a parent node is processed before any of its child nodes is done.

The traversal is implemented as follows:

```
1. Access the data part of the current node (in the figure: position red).
2. Traverse the left subtree by recursively calling the pre-order function.
3. Traverse the right subtree by recursively calling the pre-order function.
```

## In-order Traversal
> In a binary search tree ordered such that in each node the key is greater than all keys in its left subtree and less than all keys in its right subtree, in-order traversal retrieves the keys in ascending sorted order

The traversal is implemented as follows:

```
1. Traverse the left subtree by recursively calling the in-order function.
2. Access the data part of the current node (in the figure: position green).
3. Traverse the right subtree by recursively calling the in-order function.
```

## Post-order Traversal
> The trace of a traversal is called a sequentialisation of the tree. The traversal trace is a list of each visited node. No one sequentialisation according to pre-, in- or post-order describes the underlying tree uniquely. Given a tree with distinct elements, either pre-order or post-order paired with in-order is sufficient to describe the tree uniquely. However, pre-order with post-order leaves some ambiguity in the tree structure.

The traversal is implemented as follows:

```
1. Traverse the left subtree by recursively calling the post-order function.
2. Traverse the right subtree by recursively calling the post-order function.
3. Access the data part of the current node (in the figure: position blue).
```
