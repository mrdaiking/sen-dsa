# Day 6: Group Anagrams - HashMap Grouping

## Key Concept
- Use HashMap to group words that are anagrams of each other
- Canonical form (sorted string or character count) as HashMap key

## When to Use
- When you need to group or classify strings by their character composition
- When order of characters doesn't matter, only frequency

## Complexity Expectation
- Time: O(N * K log K) (N = number of words, K = max word length)
- Space: O(N * K) for storing groups

## Typical Edge Cases
- Empty string
- Single word
- All words are unique
- All words are the same

## Pattern Variations
- Group by sorted string
- Group by character count tuple
- Can combine with other patterns (e.g., frequency counting)
