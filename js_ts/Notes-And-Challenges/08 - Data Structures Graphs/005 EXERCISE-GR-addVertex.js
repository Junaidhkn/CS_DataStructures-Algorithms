/*

> Single item in graph is refered to as a Vertex(also often called as Node).
> And the connection between these Vertex is called Edge(also often called as connection)
> These is no limitations to how many vertices a particular vertex can connect to.
> There are couple of ways we can store a graph 
        - Adjacency Matrix
        - Adjacency List
> Space Complexity of 
        - Adjacency Matrix => O(|V|^2), where V is vertices
        - Adjacency List => O(|V| + |E|), where V is vertices and edges
> Time Complexity of 
        - Adjacency Matrix => O(|V|^2)
        - Adjacency List   => O(1)

*/

class Graph {
    constructor() {
        this.adjacencyList = {};
    }

    printGraph () {
        if ( Object.keys( this.adjacencyList ).length !== 0 ) {
            console.log( "{" );
            for ( const [key, value] of Object.entries( this.adjacencyList ) ) {
                console.log( " ", `${key}: ${value}` );
            }
            console.log( "}" );
        } else {
            console.log( "{}" );
        }
    }

    /// WRITE ADDVERTEX METHOD HERE ///

    addVertex ( vertex ) {
        if ( !this.adjacencyList[vertex] ) {
            this.adjacencyList[vertex] = []
            console.log( this.adjacencyList )
            // console.log( this.adjacencyList[vertex] )
            return true
        }
        return false
    }

    ///////////////////////////////////

}



function test () {
    let myGraph = new Graph();
    myGraph.addVertex( 'aa' )
    myGraph.printGraph();
}


test();


/*
    EXPECTED OUTPUT:
    ----------------
    {}

*/