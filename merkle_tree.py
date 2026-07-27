import hashlib #built-in cryptographic library for hashing (sha256/hashlib.sha256)
from typing import List, Optional #built-in type hinting module (specifying what type of data is expected) purpose is to catch bug early
    #:List - tells python that variable expects a list of strings (List[str])


class MerkleTree: #blueprint for Merkle Tree object

  def __init__(self, data_blocks: List[str]): #constructor method to initialize, self = instance of the class himself and data_blocks = represents as list of raw text strings
    self.data_blocks: List[str] = data_blocks #store the original raw strings inside the object
    self.leaves: List[str] = [ #: - type annotations, self.leaves - variable name, : List[str] - type hint (hey python, this variable is expected to be a list  of strings)
        self._hash(block) for block in data_blocks #self._hash(block) - convert each raw string into SHA-256 hash and for block in data_block - loops over every raw string (log entry 1) passed into data_blocks
    ] if data_blocks else [] #safety check = ternary operator, if data_blocks is not empty = create a list of hashes, else = sets self.leaves to empty list ([])
    self.root: Optional[str] = self._build_tree(self.leaves) # self.leaves - takes new hashed leaves, self._build_tree(self.leaves) - automatically call the "self._build tree" right after the object is created, self.root - calculate top level merkle root hash string to self.root, :Optional[str] - type hint, telling either will hold a string hash or None (if self.leaves is empty)

  @staticmethod #telling python that this method doesnt depend to self (class data)/standalone utility function inside class
  def _hash(val: str) -> str: #it accept a string parameter (val) and promise to return string, the "_" indicates its an internal helper method 
    """Helper method to return SHA-256 hash of a string."""
    return hashlib.sha256(val.encode("utf-8")).hexdigest() #val.encode("utf-8") - convert string into raw bytes because cryptographic functions require byte streams, hashlib.sha256(...) - passes those bytes into the SHA-256 algorithm to create a hash object, .hexdigest() - converts the raw binary hash into standard 64-hexadecimal string

  def _build_tree(self, nodes: List[str]) -> Optional[str]: #function with self (class instance), nodes that expects a list of string and type hinting that return value is either string or None
    """Recursively pair and hash nodes until a single Merkle Root remains."""
    if not nodes: #if nodes is empty, return None
      return None
    if len(nodes) == 1: #if nodes has only one left node, the algorithm has reached the top of the tree and return that single node as the Merkle Root
      return nodes[0]

    # Handle odd number of elements by duplicating the last node
    if len(nodes) % 2 != 0: #if the number of nodes is odd, duplicate the last node (nodes[-1]) and append it to the end of the list to make it even
      nodes.append(nodes[-1])

    next_level: List[str] = [] #next_level - empty list that expects to hold the combined hashes of the current level, :List[str] - type hint that expects a list of strings
    for i in range(0, len(nodes), 2): #loop that iterates even
      combined_hash = self._hash(nodes[i] + nodes[i + 1]) #concatenate the two hashes (nodes[i] + nodes[i+1]) and pass it to one variable
      next_level.append(combined_hash) #the combined hash append to the next_level list

    return self._build_tree(next_level) #recursively call the _build_tree(self) until only one hash remains, which will be the Merkle Root
  

# --- Quick Test Execution ---
if __name__ == "__main__": #seperate execution when it run directly 
  sample_logs = [ #sample log entries 
      "2026-07-26 05:00:01 - User clocked in",
      "2026-07-26 05:05:00 - Cryptography study complete",
      "2026-07-26 06:45:00 - Rest period completed",
      "2026-07-26 07:15:00 - Deep Coding block initiated",
  ]

  tree = MerkleTree(sample_logs) #create an instance inside with sample_logs as input

  print(f"Total Log Entries: {len(sample_logs)}")
  print(f"Merkle Root: {tree.root}")