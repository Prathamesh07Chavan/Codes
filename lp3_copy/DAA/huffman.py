import heapq #gives us a min-heap.A min-heap always gives us the element with the smallest value first.

# Node of Huffman Tree
class Node:
    def __init__(self, char, freq):  #create new node ex Node("a",2)sochar-a,freq   -2
        self.char = char          # Store character
        self.freq = freq          # Store frequency
        self.left = None          # Left child
        self.right = None         # Right child

    # Compare nodes by frequency
    def __lt__(self, other):
        return self.freq < other.freq


# Build Huffman Tree
def build_tree(freq):
    # Create a node for each character
    heap = [Node(ch, f) for ch, f in freq.items()]

    # Convert list into min heap acc to freq
    heapq.heapify(heap)

    # Build tree until only one node remains as final remaining node becomes the root of the Huffman Tree.
    while len(heap) > 1:

        # Take two smallest frequency nodes
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Combine both nodes
        new_node = Node(None, left.freq + right.freq) #None is used because this is not a character node. It is an internal node.

        # Set left and right children
        new_node.left = left
        new_node.right = right

        # Put new node back into heap
        heapq.heappush(heap, new_node)

    # Return root of Huffman Tree
    return heap[0]


# Generate Huffman Codes
def generate_codes(root, code="", codes=None):

    # Create empty dictionary
    if codes is None:
        codes = {}

    # Stop if tree is empty
    if root is None:
        return codes

    # If it is a character node, store its code
    if root.char is not None:
        codes[root.char] = code

    # Go left and add 0
    generate_codes(root.left, code + "0", codes)

    # Go right and add 1
    generate_codes(root.right, code + "1", codes)

    return codes


# Main program
text = input("Enter text to encode: ")


# Step 1: Count frequency of each character
freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1


# Step 2: Build Huffman Tree
root = build_tree(freq)


# Step 3: Generate Huffman Codes
codes = generate_codes(root)


# Step 4: Encode the text
encoded_text = ""

for ch in text:
    encoded_text += codes[ch]


# Step 5: Display character, frequency and code
print("\nCharacter | Frequency | Huffman Code")
print("------------------------------------")

for ch in freq:
    print(f"    {ch!r}     |     {freq[ch]}      |    {codes[ch]}")


# Display encoded text
print("\nEncoded Text:", encoded_text)

'''
time complex - O(nlogn)
space complex - O(n)
adv --
-Lossless compression.  
Reduces data size.  
Simple greedy approach.  
Frequently occurring characters get shorter codes.
dis--
A Huffman Tree must be stored/transmitted.  
Not equally effective for every type of data.  
Building the tree adds some processing overhead.
use--
It is used in data compression, such as ZIP, GZIP and other compression systems.
'''
