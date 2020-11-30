
Intro: 
- Formulated by Edsger W. Dijkstran, this search algorithm aims to find the most optimal path in a given network. A cost is attributed to reaching a node from any other given node. In this algorithm, the cost is simply time based on distance, although it could be made more complex to simulate real world scenarios. 

Explanation: 
- Source node has no cost, and since we do not know if there are other possible paths to reach the other nodes, a cost of infinity (in reality, just a very large number) is attributed to the other nodes. We only modify the cost of reaching a node if it is lower than the existing node. 

Applications: 
- Optimal routing for drivers to ensure that drivers reach destination in least possible time.

Cons: 
- According to an article on eng.uber.com, this search algorithm would be far too slow in a production environment where the graph (network) is unprocessed. 


- Algorithm doesn't work well when cost is negative. E.g. If the distance from one point to another is of a desireably short distance (a positive) but the bad conditions of the road would inflict great damage to the card (a negative), the net value of taking this particular route may be of a negative integer. 