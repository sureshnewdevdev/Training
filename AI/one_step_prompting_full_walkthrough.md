# One-Step (Zero-Shot) Prompting — Full Technical Walkthrough

**Input Prompt:** `Explain AI in One Sentence`

This document follows every branch in your mind map (“One-Step Prompting Technical Lifecycle”) and demonstrates an **encode → process → decode** run with **toy-but-consistent numbers**. Real models use larger dimensions and learned weights; numbers here are illustrative.

---

## A) Text Processing

### 1) Text normalization
**Goal:** Canonicalize input for predictable downstream behavior.  
**Ops:** Unicode NFC/NFKC, whitespace cleanup, quote standardization, trimming.  
**Example:**  
Raw: `Explain AI in One Sentence` → Normalized: `Explain AI in One Sentence` (no change)

### 2) Handling spacing around punctuation
No punctuation here. (If present, many tokenizers use a leading-space marker `▁` to encode boundaries.)

---

## B) Tokenization

Tokenizers split text into **subword pieces**. We mimic a BPE/Unigram-style tokenizer that uses a **leading-space marker** `▁` for word boundaries.

### 3) Convert text → tokens (subwords)
Segmentation (spaces shown as `▁`):
```
Explain  ▁AI  ▁in  ▁One  ▁Sentence
```

### 4) Algorithms like BPE / WordPiece
- Build subwords by merging frequent character/byte pairs.
- Allows open-vocab coverage with a compact vocabulary.

### 5) Special tokens
We wrap the sequence with special tokens:
```
<bos>  Explain  ▁AI  ▁in  ▁One  ▁Sentence  [target to be generated ...]  <eos>
```

---

## C) Vocabulary Mapping

### 6) Vocabulary
Learned at tokenizer training time; contains entries for words, subwords, punctuation, and specials.

### 7) Tokens → IDs
**Illustrative IDs (toy):**

| Piece        | ID    |
|--------------|-------|
| `<bos>`      | 0     |
| `Explain`    | 11987 |
| `▁AI`        | 314   |
| `▁in`        | 69    |
| `▁One`       | 1207  |
| `▁Sentence`  | 8905  |

**Encoded input IDs:**
```
[ 0, 11987, 314, 69, 1207, 8905 ]
```

### 8) Lookup tables
Two maps exist: `piece → id` and `id → piece` used for encode/decode.

---

## D) Neural Network Processing (Decoder-Only Transformer)

We simulate a **GPT-style** decoder (used for generation).

- Hidden size `d_model = 8` (toy; real ≈ 2–8k)
- One attention head with `d_k = d_v = 4` (toy)
- No padding; short prompt

### 9) Token embeddings (IDs → vectors)

| Token        | ID    | Embedding `e` (size 8)                                     |
|--------------|-------|-------------------------------------------------------------|
| `<bos>`      | 0     | `[ 0.00,  0.03, -0.01,  0.02,  0.00,  0.01,  0.00, -0.02]` |
| `Explain`    | 11987 | `[ 0.11, -0.23,  0.05,  0.40, -0.12,  0.07,  0.18, -0.03]` |
| `▁AI`        | 314   | `[-0.05,  0.08,  0.10, -0.02,  0.03, -0.01,  0.06,  0.00]` |
| `▁in`        | 69    | `[ 0.02,  0.01, -0.03,  0.05, -0.04,  0.02,  0.00,  0.01]` |
| `▁One`       | 1207  | `[-0.06,  0.02,  0.04,  0.03,  0.01,  0.05, -0.02,  0.00]` |
| `▁Sentence`  | 8905  | `[ 0.07,  0.06,  0.03,  0.01, -0.03,  0.04,  0.02, -0.01]` |

### 10) Vector size
Equal to `d_model` (=8 here). All layer transforms preserve this size.

### 11–12) Positional encodings (add position info)

**Learned** positional vectors (toy):

| Position | `p_pos`                                      |
|----------|-----------------------------------------------|
| 0        | `[ 0.00,  0.01,  0.00,  0.01,  0.00,  0.01,  0.00,  0.01]` |
| 1        | `[ 0.02,  0.01,  0.00,  0.03,  0.01, -0.02,  0.00,  0.02]` |
| 2        | `[ 0.01,  0.02,  0.01,  0.00, -0.01,  0.01,  0.01,  0.00]` |
| 3        | `[ 0.03,  0.01, -0.01,  0.01,  0.00,  0.02,  0.01, -0.02]` |
| 4        | `[ 0.02,  0.00,  0.01,  0.01,  0.01,  0.00, -0.01,  0.01]` |
| 5        | `[ 0.01,  0.03,  0.02, -0.01,  0.01,  0.01,  0.00,  0.02]` |

**Input states** `x_t = e_token + p_t`:

- `x0 = [ 0.00, 0.04, -0.01, 0.03, 0.00, 0.02, 0.00, -0.01 ]`  
- `x1 = [ 0.13,-0.22, 0.05, 0.43,-0.11, 0.05, 0.18, -0.01 ]`  
- `x2 = [ -0.04, 0.10, 0.11, -0.02, 0.02, 0.00, 0.07,  0.00 ]`  
- `x3 = [ 0.05, 0.02, -0.04, 0.06,-0.04, 0.04, 0.01, -0.01 ]`  
- `x4 = [ -0.04, 0.02, 0.05, 0.04, 0.02, 0.05, -0.03, 0.01 ]`  
- `x5 = [ 0.08, 0.09, 0.05, 0.00,-0.02, 0.05, 0.02, 0.01 ]`  

---

### 13–15) Transformer: masked self‑attention → context

One head with `d_k = d_v = 4`. (Weights are learned; we show the **results** of Q, K, V.)

**Queries (t=5 only), Keys & Values (t=0..5):**

| t | Q₅ / Kᵗ / Vᵗ (size 4)                                   |
|---|---------------------------------------------------------|
| 0 | K₀=`[ 0.10,-0.02, 0.03, 0.04]`  V₀=`[ 0.00, 0.01, 0.00, 0.02]` |
| 1 | K₁=`[ 0.05, 0.06, 0.02, 0.08]`  V₁=`[ 0.10,-0.05, 0.07, 0.01]` |
| 2 | K₂=`[ 0.07, 0.03, 0.05, 0.02]`  V₂=`[ 0.04, 0.02, 0.08,-0.01]` |
| 3 | K₃=`[ 0.03, 0.01, 0.00, 0.06]`  V₃=`[ 0.02, 0.00, 0.01, 0.03]` |
| 4 | K₄=`[ 0.06, 0.04, 0.02, 0.03]`  V₄=`[ 0.01, 0.03, 0.01, 0.02]` |
| 5 | Q₅=`[ 0.08, 0.05, 0.06, 0.07]`  K₅=`[ 0.09, 0.05, 0.04, 0.05]`  V₅=`[ 0.06, 0.02, 0.09, 0.01]` |

**Scaled dot-products** `score₅→t = (Q₅·K_t)/√d_k`, with `√d_k = 2`:
- `score₅→0 = 0.006`
- `score₅→1 = 0.007`
- `score₅→2 = 0.006`
- `score₅→3 = 0.004`
- `score₅→4 = 0.005`
- `score₅→5 = 0.0078`

**Causal mask:** only `t ≤ 5` visible (no future).

**Softmax → attention weights** (toy normalization):
```
α₅,0=0.163, α₅,1=0.165, α₅,2=0.163, α₅,3=0.159, α₅,4=0.162, α₅,5=0.188
```

**Context vector** `ctx₅ = Σ α₅,t · V_t` (size 4):
```
ctx₅ ≈ [ 0.036, 0.006, 0.041, 0.017 ]
```

**FFN + residual + norms** → **post-FFN hidden** (size 8):
```
h₅ ≈ [ 0.11, 0.07, 0.08, 0.02, -0.01, 0.06, 0.04, 0.03 ]
```

---

## E) Generation Process (progressive)

**Vocab projection** of `h₅` → **logits** (slice shown):

| Piece           | ID   | Logit |
|-----------------|------|-------|
| `▁AI`           | 314  | 2.1   |
| `▁is`           | 45   | **6.3** |
| `▁the`          | 17   | 5.1   |
| `▁science`      | 901  | 5.5   |
| `▁of`           | 23   | 5.0   |
| `▁creating`     | 1456 | 5.2   |
| `▁machines`     | 1789 | 5.4   |
| `▁that`         | 66   | 4.9   |
| `▁can`          | 88   | 4.2   |
| `▁learn`        | 3001 | 5.0   |
| `▁and`          | 21   | 4.6   |
| `▁like`         | 120  | 4.1   |
| `▁humans`       | 3302 | 5.3   |
| `.`             | 13   | 5.8   |

**16) Non-linear transforms** happen inside FFN (e.g., GELU).  
**17) Feature processing** uses LayerNorms and residuals for stability.

---

## F) Output Generation

### Probability distribution
Softmax turns logits to probabilities. With **greedy decoding**, we pick the top logit each step.

**Greedy path for one sentence:**
```
▁is(45), ▁the(17), ▁simulation(1711), ▁of(23), ▁human(1120),
▁intelligence(2044), ▁by(130), ▁machines(1789), .(13), <eos>(1)
```
**Generated IDs tail:**
```
[ 45, 17, 1711, 23, 1120, 2044, 130, 1789, 13, 1 ]
```

---

## G) Decoding (IDs → text)

**Input IDs:** `[ 0, 11987, 314, 69, 1207, 8905 ]` → `<bos> Explain ▁AI ▁in ▁One ▁Sentence`  
**Generated IDs:** `[ 45, 17, 1711, 23, 1120, 2044, 130, 1789, 13, 1 ]`  
Apply detokenization rules (drop specials; `▁` = leading space; fix punctuation).

- If we naïvely continue after the prompt, we may get:  
  `Explain AI in One Sentence is the simulation of human intelligence by machines.`

- In chat settings the model typically **does not echo** the user text; you’ll see the **answer**:
  **`AI is the simulation of human intelligence by machines.`**

---

## H) Model Types (mind map)

- **BERT (encoder-only):** Understanding tasks (classification, NER, span QA). Not generative.  
- **GPT (decoder-only):** Left-to-right **generation** (what we demonstrated).  
- **T5 (encoder–decoder):** **Text-to-text** mapping (summarization, translation, rewriting).

For `"Explain AI in One Sentence"`, a **GPT-style** decoder is the direct fit.

---

## I) Implementation Components (what you’d build)

1. **Tokenizer runtime** (text↔ids, BPE merges, specials)  
2. **Embedding tables** (token + positional)  
3. **Transformer stack** (N layers; MH-Attention + FFN + residuals + norms)  
4. **LM head** (projection to vocab logits)  
5. **Decoding loop** (greedy / top‑k / top‑p; stop conditions)  
6. **Postprocess** (detokenize, trim, punctuation spacing)  

---

## J) End-to-End Cheat Sheet

### Encode (text → ids)
```
Text:   "Explain AI in One Sentence"
Pieces: <bos> | Explain | ▁AI | ▁in | ▁One | ▁Sentence
IDs:    [0, 11987, 314, 69, 1207, 8905]
```

### Neural processing (at last input position t=5)
- `x5 = [0.08, 0.09, 0.05, 0.00, -0.02, 0.05, 0.02, 0.01]`
- Compute Q5, Kt, Vt; scores = `(Q5·Kt)/√4`
- Softmax → `α₅,t`  
- `ctx5 = Σ α₅,t Vt = [0.036, 0.006, 0.041, 0.017]`  
- FFN/residuals/norms → `h5 ≈ [0.11, 0.07, 0.08, 0.02, -0.01, 0.06, 0.04, 0.03]`  
- Vocab projection → logits → softmax → pick `▁is`

### Progressive generation
Append token; repeat until `.` and `<eos>`.

### Decode (ids → text)
Apply `▁` → space; drop `<bos>/<eos>`; fix punctuation.

---

## Extra: Byte/Unicode view
UTF‑8 bytes of `"Explain AI in One Sentence"` (hex):
```
45 78 70 6C 61 69 6E 20 41 49 20 69 6E 20 4F 6E 65 20 53 65 6E 74 65 6E 63 65
```
Byte-aware tokenizers handle arbitrary Unicode reliably before merges map bytes to subwords.

## Extra: Decoding strategies
- **Greedy:** deterministic, concise.  
- **Top‑k / top‑p:** diversity; may yield e.g., “AI is the science of building systems that learn and make decisions like humans.”  
- **Temperature τ:** scales logits before softmax; lower τ → more deterministic.

---

### TL;DR
1) Normalize → 2) Tokenize (+`<bos>`) → 3) IDs → 4) Embed+Positions → 5) Masked Self‑Attention + FFN → 6) Logits→Softmax→Pick → 7) Repeat → 8) Detokenize → **One clean sentence**.

