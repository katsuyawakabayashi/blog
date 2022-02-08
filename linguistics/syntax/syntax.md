What is Syntax?

As a system of grammar : the part of language that allows speakers to create
and understand phrases and sentences.

As a linguistic discipline: the subfield of linguistics that studies the rules and
properties of phrases and sentences of human languages.

<ins>Universal Grammar (UG)</ins>

- The innate building blocks of language.
- The learning algorithm that turns them into the grammar of a particular
language.

<ins>Grammaticality</ins>

- A sentence that is part of a language is called grammatical, a sentence that is
not is called ungrammatical. Whether the sentence is easy to understand is unrelated to the grammaticality.

<ins>Distributional Definition</ins>

- Parts of speech are classified by their distribution.
- Morphological distribution: Affixes appear only on certain kinds of words.
- Syntactic distribution: Position relative to other words.

<ins>Morpheme</ins>

- Meaningful morphological unit of a language

<ins>Atomic</ins>

- A word consists of only one morpheme

<ins>Derivational morpheme</ins>

- Plays lexical (meaningful) role (e.g., -able, -tion)
- Can change part of speech/category.
- Never required by grammatical rules.
- Typically indicate semantic relations
within the word.
- Typically indicate relations between
different words in a sentence.
- Typically occur before inflectional
morphology.

<ins>Inflectional morpheme</ins>

- Plays only a grammatical role (e.g., -s).
- Never changes base’s category.
- Usually required by grammatical rules.
- Typically indicate relations between
different words in a sentence.
- Occur at the end.

<ins>Derivational suffixes</ins>

**Nouns**

- -ment (basement)
- -ness (emptiness)
- -ity (sincerity)...

**Verbs**

- -ify (solidify)
- -ize (regularize)

**Adjectives**

- able (readable)
- -ing (the dancing cat)
- -al (national)

**Adverbs**

- ly (efficiently)

Inflectional suffixes

**Nouns**

- Plurals (s (cats), -es (glasses), -a (addenda))

**Verbs**

- -s (Peter loves cakes)
- ing (Mary was running),
- -en (This was written by Mary)

**Adjectives**

- comparative -er (bigger )
- superlative -est (biggest)

**Adverbs**

- They generally don’t take inflectional morphology.

<ins>Lexeme</ins>

- A unit of lexical meaning that underlies a set of words that are related through inflection
- i.e., play, plays, played, playing are the forms of the same lexeme, ‘play’

<ins>Morpheme</ins>

- the smallest meaningful lexical entry

<ins>Compound</ins>

- A lexeme that consists of more than one stem

<ins>Constituent</ins>

- A group of words that function together as a unit.
- String that speakers can manipulate as a single chunk.

<ins>Lexical entry</ins>

- A single word, a part of a word, or a chain of words that forms the basic elements of a lexicon

Example: ‘remagnetize’

<ins>Lexical entry</ins>

| magnet | free (N) |  |  |
| --- | --- | --- | --- |
| -ize | bound | V | c-selects N |
| re- | bound | Adv | combines with V |

*c in c-selects stands for ‘category’

- ‘unzippable’ has two different interpretation (Morphological ambiguity)

<ins>Lexicon</ins>

- Collection of lexical entries
- * this is NOT part of word

<ins>Constituent</ins>

- A group of words that function together as a unit (Carnie: 76)
- String that speakers can manipulate as a single chunk (Sportiche et al. (2014)

<ins>Constituency test</ins>

- A test to identify a constituent
- It passes the test iff:
    - grammatical
    - consistent in meaning
- Failing the test is inconclusive

### Constituency tests

Constituency tests (stand alone, substitution, topicalization, clefting, pseudoclefting
and coordination).

<ins>Stand Alone Test</ins>

- A sting is a constituent if it can be an answer for a question.
    - John went to Paris last year
        - Q. Where did John go? → A. Paris
    

<ins>Substitution Test</ins>

- A string is a constituent if it can be replaced with a monomorphic word (word with no internal structures) and remains well formed.
- Passing the test implies:
    - The string and the monomorphic have the same distributional property (i.e., same category)
    - The string is a subtree of the entire tree
    
- Monomorphic words and categories

| Monomorphic word | Category |
| --- | --- |
| one(s) | NP |
| pronouns | DP |
| there/then | PP |
| do so | VP (do = V, so = PP) |

Coordination Test

- A string is a constituent if it can conjoin with another similar string.

<ins>Movement tests</ins>

<ins>Topicalization</ins>

- A string is a constituent if it can be moved to the front of the sentence and the sentence remains well formed.
    - i.e. John gave his apple to Mary.
        - His apple, John gave to Mary.
        - To Mary, John gave his apple to.

<ins>Clefting</ins>

- A string is a constituent if the sentence can be rewritten in the form of ‘It is(was) X that ...’ where X is the string.
    - i.e. John gave his apple to Mary.
        - It was John that gave his apple to Mary.
        - It was Mary that John gave his apple to.
- VPs can be topicalized but cannot be clefted

<ins>Pseudoclefting</ins>

- A string is a constituent if the sentence can be rewritten in in the form of ‘What X is(was) ...’. where X is the string.
    - i.e. John gave his apple to Mary
        - What John gave to
- PPs cannot be pseudoclefted
- Note that this test may not work for single stings.

# Tree

Branch: A line connecting two parts of a tree.

Node: Each point that is labeled with a word or a category is called a node. It is the end of
a branch.

Label**:** The name given to a node.

Leaf: The nodes along the bottom of the tree are called leaves. Terminal node.

Mother**:** Node A is a mother of B if and only if A is higher up in the tree than B and they are
separated by a single branch (no intervening nodes).

Sister**:** Two nodes are sisters if they share the same mother

<ins>Dominance</ins>

- A node α dominates a node β iff there exists a chain of two or more nodes α, γi, ..., γj , β such that each node is the mother of the next one. (Roughly, α is an ancestor of β.)

<ins>Root</ins>

- The node that dominates all other nodes in a tree, and is itself dominated by none.

<ins>Immediate dominance</ins>

- A node α immediately dominates a node β iff (i) α dominates β, and (ii) there is no node γ != α such that γ dominates β. (i.e., α is β’s mother)

<ins>Mother</ins>

- A is the mother of B if A immediately dominates B.

<ins>Daughter</ins>

- B is the daughter of A if B is immediately dominated by A.

<ins>Sisters</ins>

- Two nodes that share the same mother

<ins>Sister Precedence</ins>

- Node A sister-precedes node B iff both are immediately dominated by the same node, and A appears to the left of B.

<ins>Precedence</ins>

- Node A precedes node B iff
    - (i) neither A dominates B nor B dominates A
    - (ii) A (or some node dominating A) sister precedes B (or some node dominating B)
- i.e., Node A is to the left of B

<ins>C(onstituent)-Command</ins>

- Node A c-commands node B if
    - (i) every node immediately dominating A also dominate B
    - (ii) A does not itself dominate B
- i.e., Node B is a sister of A then A c-commands B and all of B’s children

<ins>Asymmetric C-Command</ins>

- A asymmetrically c-commands B if A c-commands B but B does not c-command A.

<ins>Exhaustive dominance</ins>

- A node α exhaustively dominates a set of terminal nodes N iff (i) α dominates every node in N (so that there is no member of the set N that is not dominated by α), and (ii) α does not dominate any terminal node not in N.

<ins>X-bar Theory (in English)</ins>

- XP: mother of the tree
- Specifier: daughter of XP
- X’: daughter of XP, sister preceded by Specifier
    - XP → (Specifier) X’
- X: daughter of X’
- Complement: daughter of X’, sister-preceded by X
    - X’ → X (Complement)

<ins>Head-initial language</ins>

- A language in which X sister-precedes Complement (i.g., English)

<ins>Tense</ins>

- free
    - [-fin]: ‘to’
    - [+fin]: ‘modals
- bound
    - [+pres]: -, -s
    - [-pres]: -ed, -d

<ins>Selection</ins>

- Type of phrases that the head requires in its specifier position

<ins>C(omplement)-selection</ins>

- What kind of sister a particular head is selecting for.

<ins>Determiner</ins>

- free
    - ‘the/this’ c-selects NP e.g., the/this dog
- bound
    - ‘s selects DP e.g., Mary’s
    
