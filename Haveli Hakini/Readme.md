### Haveli Hakini Theorem
 To find whether a graph exist given the degree of the vertices present in the graph.
 It is a Recursive Algorithm which takes the vertex with higher degree (di) at first and reduces the other di vertices degree value by 1.
 Then the list of degrees is sorted at every step.

```python
Input : 8 8 7 6 6 5 5 2 2 2 1 1 1

* 8 7 6 6 5 5 2 2 2 1 1 1
* 7 6 5 5 4 4 1 1 2 1 1 1
* * 6 5 5 4 4 2 1 1 1 1 1
* * 5 4 4 3 3 1 0 1 1 1 1
* * * 4 4 3 3 1 1 1 1 1 0
* * * 3 3 2 2 0 1 1 1 1 0
* * * * 3 2 2 1 1 1 1 0 0
* * * * 2 1 1 1 1 1 1 0 0
* * * * * 1 1 1 1 1 1 0 0
* * * * * 0 0 1 1 1 1 0 0
* * * * * * 1 1 1 0 0 0 0
* * * * * * 0 1 1 0 0 0 0
* * * * * * * 1 0 0 0 0 0
* * * * * * * 0 0 0 0 0 0
Graph is possible !
```
