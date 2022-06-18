# Phonology

# Stress

- Only syllables can be stressed
- Syllabification algorithm creates unstressed syllables
- Stresses can be added according to stress rules afterward

## Stress rules

### Penultimate Stress

$\sigma \rightarrow [+stress] \space / \space \_\_ \space \sigma \space]_{word}$

- Stress second last syllable

### A**ntepenult Stress**

$\sigma \rightarrow [+stress] \space / \space \_\_ \space \sigma \space \sigma\space]_{word}$

- Stress third last syllable

## Application of Parenthesis Stress Rules

- Stress rules are tried from the longest(”Longest first”) to shorter(”Completeness”) and once it’s applied terminates(”Blockage”).

**Example**

$\sigma \space \rightarrow \space [+stress] \space / \space \_\_ \space ((\sigma)\space \sigma) \space ]_{word}$

1. Remove all the parentheses (”Longest first”)

$\sigma \space \rightarrow \space [+stress] \space / \space \_\_ \space \sigma\space \sigma \space ]_{word}$

- Stress is applied to the third last syllable

1. If it fails, then the inner parenthesis is added and eliminates the $\sigma$ (”Completeness”)

$\sigma \space \rightarrow \space [+stress] \space / \space \_\_ \space (\sigma)\space \sigma \space ]_{word}$

$\sigma \space \rightarrow \space [+stress] \space / \space \_\_ \space \space \sigma \space ]_{word}$

- Stressed is applied to second last syllable

1. If it fails, then recurse

$\sigma \space \rightarrow \space [+stress] \space / \space \_\_ \space  (\sigma) \space ]_{word}$

$\sigma \space \rightarrow \space [+stress] \space / \space \_\_ \space ]_{word}$

- Stress is applied to the last syllable

## Alternating Stress

$\sigma \space \rightarrow \space \begin{bmatrix}+main \\+stress \end{bmatrix} \space / \space \_\_  \space]_{word}$

### Iterative rules

$\sigma \space \rightarrow \space [+stress] \space / \space \_\_  \space \begin{bmatrix}
\sigma \\
+stress
\end{bmatrix}]_{word}$

- This applies *iteratively* since its preceding syllable feeds the rule (**self-feeding**)

## Syllable Weight

### Heavy syllable

- Ends with a consonant (**Closed syllable**)
- Includes a long vowel or diphthong (**Open syllable**)
- Tends to attract stress
- Macron ****/-/

### Light syllable

- Ends with a short vowel
- Breve / ̆/

Example: Classical Arabic Stress

$\sigma \space \rightarrow \space [+stress] \space / \_\_ \space ((\space \breve{} \space) \space \sigma )]_{word}$

TL;DR: Stress heavy penult and if not stress antepenult or shorter

1. Remove all the parentheses

$\sigma \space \rightarrow \space [+stress] \space / \_\_ \space \space \breve{} \space \space \sigma ]_{word}$

- Stress *antepenult* if *penult* is light

1. Add an inner parentheses and eliminate

$\sigma \space \rightarrow \space [+stress] \space / \_\_ \space \space (\space \breve{} \space) \space \space \sigma ]_{word}$

$\sigma \space \rightarrow \space [+stress] \space / \_\_ \space \space  \space \space \sigma ]_{word}$

- Stress *penult*

1. Recurse

$\sigma \space \rightarrow \space [+stress] \space / \_\_ \space ]_{word}$

**Fricative:** /f/,/v/, /s/,/z/,/θ/,/ð/, /ʒ/ and  /∫/ are examples of fricatives.

**Affricate:** /ʧ/ and /ʤ/ are the only affricate consonants in the English language.

# Natural Class

### Voice

- DORSAL: tongue body

### Place

- **LABIAL**:
    - labiodental
        - + (f v)
    - round
        - + (with “w”)
        - -
- CORONAL:
    - **anterior:**
        - + (Alveolar and front)
        - -
    - **distributed**:
        - + (dental and affricate)
        - -
    - **strident:**
        - + (sibilants)
        - -

### Manner

- vowel = [+syllabic]
- glide = [-syllabic, -consonantal]
- liquid = [+consonantal, +approximant]
- nasal = [-approximant, +sonorant]

- obstruent = [-sonorant]
    - stops = [-continuant, -delayed release]
    - affricate = [-continuant, +delayed release]
    - fricative = [+continuant, +delayed release]

- aspiration = [+spread glottis]
- ejectives = [+constricted glottis]
- implosives = [+implosives]

## Feeding / Bleeding

### Feeding

- A rule creates a context in which another rule can apply

### Bleeding

- A rule destroys a context in which another rule can apply

### Counter feeding

- Feeding causes incorrect prediction

### Counter bleeding

- Bleeding causes incorrect prediction