<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Artificial Intelligence Algorithms & Agents</title>
<style>
body{
    font-family: Arial, sans-serif;
    margin:40px;
    line-height:1.6;
}
h1,h2,h3{
    color:#2c3e50;
}
code{
    background:#f4f4f4;
    padding:4px;
}
pre{
    background:#f4f4f4;
    padding:10px;
    border-radius:5px;
}
table{
    border-collapse: collapse;
    width:60%;
}
table, th, td{
    border:1px solid #ccc;
}
th,td{
    padding:8px;
    text-align:left;
}
</style>
</head>

<body>

<h1>Artificial Intelligence Algorithms & Agents</h1>

<p>
This repository contains simple implementations of <b>Artificial Intelligence search algorithms and agents</b> written in Python.
The project demonstrates how classical AI techniques such as 
<b>Breadth First Search (BFS)</b>, <b>Depth First Search (DFS)</b>, and 
<b>Iterative Deepening DFS (IDDFS)</b> can be applied to solve problems like the 
<b>Missionaries and Cannibals puzzle</b>, along with a <b>Reflex Agent example for Air Quality Index (AQI)</b> decision making.
</p>

<hr>

<h2>Project Files</h2>

<h3>1. Missionaries and Cannibals Search Problem</h3>

<p><b>File:</b> cannibals.py</p>

<p>
This program solves the classic <b>Missionaries and Cannibals problem</b> using different search algorithms.
</p>

<h3>Problem Description</h3>

<ul>
<li>The boat carries at most <b>2 people</b></li>
<li>Cannibals should never <b>outnumber missionaries</b> on either side</li>
</ul>

<h3>Algorithms Implemented</h3>

<ul>
<li>Breadth First Search (BFS)</li>
<li>Depth First Search (DFS)</li>
<li>Iterative Deepening Depth First Search (IDDFS)</li>
</ul>

<h3>State Representation</h3>

<pre>(M, C, Boat)</pre>

<p>
M = Missionaries on the left side<br>
C = Cannibals on the left side<br>
Boat = Boat position (0 = left, 1 = right)
</p>

<h3>Example States</h3>

<pre>
Start : (3,3,0)
Goal  : (0,0,1)
</pre>

<p>
The program generates valid successor states and finds a solution path using search algorithms.
</p>

<hr>

<h2>Search Algorithms Implemented</h2>

<h3>Breadth First Search (BFS)</h3>

<p>Breadth First Search explores nodes <b>level by level</b>.</p>

<b>Characteristics:</b>
<ul>
<li>Uses a <b>queue</b></li>
<li>Always finds the <b>shortest path</b></li>
<li>High memory usage</li>
</ul>

<b>Best used when:</b>
<ul>
<li>The solution is close to the root</li>
<li>The optimal path is required</li>
</ul>

<h3>Depth First Search (DFS)</h3>

<p>Depth First Search explores <b>deep into the tree first</b> before backtracking.</p>

<b>Characteristics:</b>
<ul>
<li>Uses a <b>stack</b></li>
<li>Uses less memory</li>
<li>May not always find the shortest path</li>
</ul>

<b>Best used when:</b>
<ul>
<li>The search space is very large</li>
<li>Memory usage must be minimal</li>
</ul>

<h3>Iterative Deepening DFS (IDDFS)</h3>

<p>IDDFS combines the advantages of <b>BFS and DFS</b>.</p>

<b>Characteristics:</b>
<ul>
<li>Performs DFS with increasing depth limits</li>
<li>Guarantees optimal solution like BFS</li>
<li>Uses memory similar to DFS</li>
</ul>

<b>Steps:</b>

<pre>
Depth 0 → search
Depth 1 → search
Depth 2 → search
...
until goal found
</pre>

<hr>

<h2>Algorithm Comparison</h2>

<table>
<tr>
<th>Algorithm</th>
<th>Data Structure</th>
<th>Completeness</th>
<th>Optimal</th>
<th>Memory Usage</th>
</tr>

<tr>
<td>BFS</td>
<td>Queue</td>
<td>Yes</td>
<td>Yes</td>
<td>High</td>
</tr>

<tr>
<td>DFS</td>
<td>Stack</td>
<td>No</td>
<td>No</td>
<td>Low</td>
</tr>

<tr>
<td>IDDFS</td>
<td>Stack (Depth Limited)</td>
<td>Yes</td>
<td>Yes</td>
<td>Moderate</td>
</tr>

</table>

<hr>

<h2>Reflex Agent for Air Quality Monitoring</h2>

<p><b>File:</b> aqi_reflex_agent_multi_pollutant.py</p>

<p>
This program implements a <b>Simple Reflex Agent</b> that analyzes environmental data and decides how many vehicles should be allowed on the road based on <b>Air Quality Index (AQI)</b>.
</p>

<p>The agent reads pollutant values from:</p>

<pre>environment.txt</pre>

<h3>Pollutants Considered</h3>

<ul>
<li>PM2.5</li>
<li>PM10</li>
<li>CO</li>
<li>NO₂</li>
<li>SO₂</li>
<li>O₃</li>
</ul>

<p>
Each pollutant is converted into a <b>sub-index</b>, and the overall AQI is calculated as the <b>maximum of all sub-indices</b>.
</p>

<hr>

<h2>AQI Categories</h2>

<table>

<tr>
<th>AQI Range</th>
<th>Category</th>
</tr>

<tr>
<td>0 – 50</td>
<td>Good</td>
</tr>

<tr>
<td>51 – 100</td>
<td>Satisfactory</td>
</tr>

<tr>
<td>101 – 200</td>
<td>Moderate</td>
</tr>

<tr>
<td>201 – 300</td>
<td>Poor</td>
</tr>

<tr>
<td>301 – 400</td>
<td>Very Poor</td>
</tr>

<tr>
<td>401 – 500</td>
<td>Severe</td>
</tr>

</table>

<hr>

<h2>Example Output</h2>

<pre>
Overall AQI: 200
AQI Category: Moderate
Cars Allowed on Road: 6000
</pre>

<hr>

<h2>How to Run the Programs</h2>

<h3>Run Missionaries and Cannibals Problem</h3>

<pre>python cannibals.py</pre>

<p>The output will show solutions using:</p>

<ul>
<li>BFS</li>
<li>DFS</li>
<li>IDDFS</li>
</ul>

<h3>Run AQI Reflex Agent</h3>

<p>Create a file called:</p>

<pre>environment.txt</pre>

<p>Example content:</p>

<pre>
PM2.5=120
PM10=180
CO=5
NO2=60
SO2=30
O3=80
</pre>

<p>Then run:</p>

<pre>python aqi_reflex_agent_multi_pollutant.py</pre>

<hr>

<h2>Concepts Demonstrated</h2>

<ul>
<li>State space search</li>
<li>Graph traversal algorithms</li>
<li>Problem solving using AI</li>
<li>Simple reflex agents</li>
<li>Environment based decision making</li>
</ul>

<hr>

<h2>Author</h2>

<p>
<b>AI Practice Project</b><br>
Implemented in Python for learning basic Artificial Intelligence algorithms and agent models.
</p>

</body>
</html>
