class TrieNode {
    public children: Map<string, TrieNode>;
    public isEndOfWord: boolean;

    constructor() {
        this.children = new Map();
        this.isEndOfWord = false;
    }
}

export default class Trie {
    private root: TrieNode;

    constructor() {
        this.root = new TrieNode();
    }

    // Insert a word into the trie
    insert(item: string): void {
        let currentNode = this.root;

        for (const char of item) {
            if (!currentNode.children.has(char)) {
                currentNode.children.set(char, new TrieNode());
            }
            currentNode = currentNode.children.get(char)!;
        }

        currentNode.isEndOfWord = true;
    }

    // Delete a word from the trie
    delete(item: string): void {
        this.deleteHelper(this.root, item, 0);
    }

    private deleteHelper(node: TrieNode, item: string, index: number): boolean {
        if (index === item.length) {
            // We've reached the end of the word
            if (!node.isEndOfWord) {
                return false; // Word not found
            }
            node.isEndOfWord = false;
            return node.children.size === 0; // If true, delete this node
        }

        const char = item[index];
        const childNode = node.children.get(char);

        if (!childNode) {
            return false; // Word not found
        }

        const shouldDeleteChild = this.deleteHelper(childNode, item, index + 1);

        if (shouldDeleteChild) {
            node.children.delete(char);
            return node.children.size === 0 && !node.isEndOfWord;
        }

        return false;
    }

    // Find all words that start with the given prefix
    find(partial: string): string[] {
        const result: string[] = [];
        let currentNode = this.root;

        // Traverse to the end of the prefix
        for (const char of partial) {
            if (!currentNode.children.has(char)) {
                return result; // Prefix not found
            }
            currentNode = currentNode.children.get(char)!;
        }

        // Recursively find all words starting from this node
        this.findAllWordsFromNode(currentNode, partial, result);
        return result;
    }

    private findAllWordsFromNode(
        node: TrieNode,
        prefix: string,
        result: string[],
    ): void {
        if (node.isEndOfWord) {
            result.push(prefix);
        }

        for (const [char, childNode] of node.children) {
            this.findAllWordsFromNode(childNode, prefix + char, result);
        }
    }
}
