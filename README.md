# Oregon-Pathfinder

How to compile/run your program
Dependencies and setup instructions
Example commands showing how to use each algorithm
At least 3 example runs with different algorithm/route combinations

Welcome! You should be able to run my program as long as you have both of the .txt files within the same folder under the correct name and variable declaration. Everything is pretty self explanatory, as my program will walk you through each step of running it. Some example runs and test cases:

Test Cases:

Welcome to Oregon Pathfinder!

Enter your starting city: Portland
Enter your destination city: Salem
Choose an algorithm (A* (a), Dijkstra: (d), Greedy Best-First Search: (g)): a
Calculating route from PORTLAND to SALEM using A* Search algorithm...
 
Path found: PORTLAND -> SALEM
Cities explored: 2
Total distance: 47 miles
Vertices explored: 2
Time taken: 0.0004 seconds

Would you like to try another route? (yes/no): y
Enter your starting city: Portland
Enter your destination city: Salem
Choose an algorithm (A* (a), Dijkstra: (d), Greedy Best-First Search: (g)): d
Calculating route from PORTLAND to SALEM using Dijkstra's algorithm...
 
Path found: PORTLAND -> SALEM
Cities explored: 2
Total distance: 47 miles
Vertices explored: 2
Time taken: 0.0002 seconds

Would you like to try another route? (yes/no): y
Enter your starting city: Portland
Enter your destination city: Salem
Choose an algorithm (A* (a), Dijkstra: (d), Greedy Best-First Search: (g)): g
Calculating route from PORTLAND to SALEM using Greedy Best-First Search algorithm...

Path found: PORTLAND -> SALEM
Cities explored: 2
Total distance: 47 miles
Vertices explored: 5
Time taken: 0.0003 seconds

Would you like to try another route? (yes/no): y
Enter your starting city: Portland
Enter your destination city: Eugene
Choose an algorithm (A* (a), Dijkstra: (d), Greedy Best-First Search: (g)): a
Calculating route from PORTLAND to EUGENE using A* Search algorithm...
 
Path found: PORTLAND -> SALEM -> EUGENE
Cities explored: 3
Total distance: 111 miles
Vertices explored: 3
Time taken: 0.0004 seconds

Would you like to try another route? (yes/no): y
Enter your starting city: Portland
Enter your destination city: Eugene
Choose an algorithm (A* (a), Dijkstra: (d), Greedy Best-First Search: (g)): d
Calculating route from PORTLAND to EUGENE using Dijkstra's algorithm...
 
Path found: PORTLAND -> SALEM -> EUGENE
Cities explored: 3
Total distance: 111 miles
Vertices explored: 7
Time taken: 0.0004 seconds

Would you like to try another route? (yes/no): y
Enter your starting city: Portland
Enter your destination city: Eugene
Choose an algorithm (A* (a), Dijkstra: (d), Greedy Best-First Search: (g)): g
Calculating route from PORTLAND to EUGENE using Greedy Best-First Search algorithm...

Path found: PORTLAND -> SALEM -> EUGENE
Cities explored: 3
Total distance: 111 miles
Vertices explored: 7
Time taken: 0.0003 seconds

Would you like to try another route? (yes/no): y
Enter your starting city: Portland
Enter your destination city: Ashland
Choose an algorithm (A* (a), Dijkstra: (d), Greedy Best-First Search: (g)): a
Calculating route from PORTLAND to ASHLAND using A* Search algorithm...
 
Path found: PORTLAND -> SALEM -> EUGENE -> ROSEBURG -> MEDFORD -> ASHLAND
Cities explored: 6
Total distance: 283 miles
Vertices explored: 8
Time taken: 0.0011 seconds

Would you like to try another route? (yes/no): y
Enter your starting city: Portland
Enter your destination city: Ashland
Choose an algorithm (A* (a), Dijkstra: (d), Greedy Best-First Search: (g)): d
Calculating route from PORTLAND to ASHLAND using Dijkstra's algorithm...
 
Path found: PORTLAND -> SALEM -> EUGENE -> ROSEBURG -> MEDFORD -> ASHLAND
Cities explored: 6
Total distance: 283 miles
Vertices explored: 20
Time taken: 0.0003 seconds

Would you like to try another route? (yes/no): y
Enter your starting city: Portland
Enter your destination city: Ashland
Choose an algorithm (A* (a), Dijkstra: (d), Greedy Best-First Search: (g)): g
Calculating route from PORTLAND to ASHLAND using Greedy Best-First Search algorithm...

Path found: PORTLAND -> NEWPORT -> FLORENCE -> COOS_BAY -> ROSEBURG -> MEDFORD -> ASHLAND
Cities explored: 7
Total distance: 412 miles
Vertices explored: 14
Time taken: 0.0007 seconds

Would you like to try another route? (yes/no): y
Enter your starting city: Portland
Enter your destination city: Burns
Choose an algorithm (A* (a), Dijkstra: (d), Greedy Best-First Search: (g)): a
Calculating route from PORTLAND to BURNS using A* Search algorithm...
 
Path found: PORTLAND -> HOOD_RIVER -> THE_DALLES -> MADRAS -> REDMOND -> BEND -> BURNS
Cities explored: 7
Total distance: 351 miles
Vertices explored: 10
Time taken: 0.0006 seconds

Would you like to try another route? (yes/no): y
Enter your starting city: Portland
Enter your destination city: Burns
Choose an algorithm (A* (a), Dijkstra: (d), Greedy Best-First Search: (g)): d
Calculating route from PORTLAND to BURNS using Dijkstra's algorithm...
 
Path found: PORTLAND -> HOOD_RIVER -> THE_DALLES -> MADRAS -> REDMOND -> BEND -> BURNS
Cities explored: 7
Total distance: 351 miles
Vertices explored: 22
Time taken: 0.0005 seconds

Would you like to try another route? (yes/no): y
Enter your starting city: Portland 
Enter your destination city: Burns
Choose an algorithm (A* (a), Dijkstra: (d), Greedy Best-First Search: (g)): g
Calculating route from PORTLAND to BURNS using Greedy Best-First Search algorithm...

Path found: PORTLAND -> HOOD_RIVER -> THE_DALLES -> MADRAS -> REDMOND -> BEND -> BURNS
Cities explored: 7
Total distance: 351 miles
Vertices explored: 12
Time taken: 0.0006 seconds

Would you like to try another route? (yes/no): y
Enter your starting city: Portland
Enter your destination city: Medford
Choose an algorithm (A* (a), Dijkstra: (d), Greedy Best-First Search: (g)): a
Calculating route from PORTLAND to MEDFORD using A* Search algorithm...
 
Path found: PORTLAND -> SALEM -> EUGENE -> ROSEBURG -> MEDFORD
Cities explored: 5
Total distance: 268 miles
Vertices explored: 6
Time taken: 0.0008 seconds

Would you like to try another route? (yes/no): y
Enter your starting city: Portland
Enter your destination city: Medford
Choose an algorithm (A* (a), Dijkstra: (d), Greedy Best-First Search: (g)): d
Calculating route from PORTLAND to MEDFORD using Dijkstra's algorithm...
 
Path found: PORTLAND -> SALEM -> EUGENE -> ROSEBURG -> MEDFORD
Cities explored: 5
Total distance: 268 miles
Vertices explored: 19
Time taken: 0.0005 seconds

Would you like to try another route? (yes/no): y
Enter your starting city: Portland
Enter your destination city: Medford
Choose an algorithm (A* (a), Dijkstra: (d), Greedy Best-First Search: (g)): g
Calculating route from PORTLAND to MEDFORD using Greedy Best-First Search algorithm...

Path found: PORTLAND -> NEWPORT -> FLORENCE -> COOS_BAY -> ROSEBURG -> MEDFORD
Cities explored: 6
Total distance: 397 miles
Vertices explored: 12
Time taken: 0.0004 seconds

Would you like to try another route? (yes/no): n
Thank you for using Oregon Pathfinder! Safe travels!

Reflection Essay:
	I found the pathfinding exercise incredibly helpful and interesting. Before I started I had a pretty decent understanding of the steps that each algorithm takes due to the worksheet that we did this past week, but I think actually coding them and seeing them in a context that makes sense to me (like my home state geography) really helped cement them in my mind. 
	For the individual test cases, I found that for 3 of the 5 cases, all 3 algorithms gave me the same optimized path. For Portland to Ashland and Portland to Medford, Greedy Best First Search gave me significantly slower routes that took me through the coast both times instead of south through I5, the quicker way. Greedy Best-First and A* both explored fewer vertices than Dijkstra’s and often had quicker run times like in Portland to Burns where they explored 10 and 12 vertices respectively, with run times of .0006 for both. Unfortunately, neither is guaranteed to always find the quickest path. Dijkstra’s and A* always found the fastest route, where Greedy Best First went 3 for 5.
	Dijkstra’s performs best on complicated, long routes with lots of options. Although it takes slightly longer than the other two, it’s ability to consistently find the best path makes it optimal in these complex scenarios. I would use this algorithm for long road trips or other complicated routes where run time isn’t really an issue. Greedy Best First Search tends to find suboptimal routes in longer, more complicated routes where the heuristic values by city are very different. An example case I found was going from Burns to Astoria, where Greedy Best First Search found a route that took me through 2 fewer cities but added on an extra 20 miles. I would use Greedy Best First Search for short distances where run time is important, maybe if I’m in a rush to get to work. A* shows it’s greatest advantage in medium distance complicated routes, due to its faster runtime than Dijkstra’s and better accuracy in finding the fastest route than Greedy Best First. I would use A* for medium to long distance where run time does matter, maybe if I’m going to be driving for a couple hours and need to leave quickly.
	The time complexity of each of these is O((n + m) log n) where n is the amount of vertices and m is the amount of edges. Both Dijkstra's and A* have a space complexity of O(m + n), whereas Greedy Best First has a storage complexity of O(n). The Oregon map size limits how effectively we can compare these algorithms, since the runtimes are so small, the benefits of using Greedy Best First aren’t as noticeable, whereas if we were using the entire US highway system, it would be noticeably faster than the other two, and take up less space on your device. This would also highlight Dijkstra’s Algorithm as the best, since its ability to always find the fastest route will be much bigger differences time-wise on such a large scale.
	The Haversine distance is good enough for A* because it doesn’t overestimate the amount of time it takes to travel. Since it travels in a line “as the crow flies”, it is guaranteed that anything in the way will cause it to take longer, as that is the theoretical minimum distance it can take. This gives us a relatively accurate estimate of the actual distance it takes between two places. When the heuristic value underestimates the actual distance between two points, Greedy Best-First Search gets thrown off and will take whatever route it deems the shortest. In an underestimation, this may cause vertices that are further apart to seem closer together, potentially impacting the direction that Greedy Best First Search goes into, then ends up taking a much longer route than necessary.	
Trying to design a better heuristic value for this would not be easy, as the “as the crow flies” distance is about as accurate as we can get. You could use the actual driving distance between two cities as an example from our assignment to be more accurate, but that kinda defeats the point of having the heuristic value in the first place.
	

