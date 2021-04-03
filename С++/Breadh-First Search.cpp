#include <deque>
#include <map>
#include <vector>
#include <iostream>


bool BreadthFirst(std::map<std::string, std::deque<std::string>> graph, std::string begin, std::string end);
void printQueue(std::deque<std::string> d);	
void printGraph(std::map<std::string, std::deque<std::string>> graph);

int main()
{
	std::map<std::string, std::deque<std::string>> graph;

	graph["A"] = {"B", "C", "D"};
	graph["B"] = {"E", "F"};
	graph["C"] = {"H"};
	graph["D"] = {"I", "J"};
	graph["E"] = {"K"};
	graph["F"] = {};
	graph["G"] = {};
	graph["H"] = {"G"};
	graph["I"] = {};
	graph["J"] = {"L"};
	graph["K"] = {""};
	graph["L"] = {};

	if (BreadthFirst(graph, "C", "P"))
		printf("Found");
	else
		printf("Not found");

	return 0;
}

// push_front - add to the begin
// push_back - add to the end

// front - return begin
// back - return end

void printQueue(std::deque<std::string> d)
{
		for (size_t i = 0; i < d.size(); i++)
			std::cout << d[i] << " ";
		printf("\n\n");
}

void printGraph(std::map<std::string, std::deque<std::string>> graph)
{
	for (size_t i = 0; i < graph.size(); i++)
	{
		
	}
}

bool BreadthFirst(std::map<std::string, std::deque<std::string>> graph, std::string begin, std::string end)
{
	std::deque<std::string> queueForSearch;

	for (size_t i = 0; i < graph[begin].size(); i++)
		queueForSearch.push_back(graph[begin][i]);

	while (queueForSearch.size())
	{
		if (queueForSearch.front() == end)
		{
			return true;
		}

		std::string front = queueForSearch.front();

		queueForSearch.pop_front();

		for (size_t i = 0; i < graph[front].size(); i++)
		{
			queueForSearch.push_back(graph[front][i]);
			printQueue(queueForSearch);
		}
		
	}

	return false;

}