# Plagiarism Detection - iCog Labs

## Project Description
A Python-based plagiarism detection system that leverages advanced string algorithms including **shingling**, **rolling hash**, and **Trie-based autocomplete**.  
The project allows comparison of user input with multiple book datasets, provides **real-time autocomplete suggestions**, and generates a plagiarism score based on **hash matching** and **longest consecutive similarity**.



## Repository Structure
```bash
Plagiarism_detection_iCog-Labs/
├── main.py
├── preprocessing.py
├── shingling.py
├── rolling_hash.py
├── trie_autocomplete.py
├── plagiarism_checker.py
├── scoring.py
├── README.md
├── LICENSE
├── .gitignore
dataset/
├── Emma.txt
├── Mansfield Park.txt
├── Northanger Abbey.txt
├── Pride and Prejudice.txt
├── Sense and Sensibility.txt
├── preprocessed/
│   ├── Emma_clean.txt
│   ├── Mansfield Park_clean.txt
│   ├── Northanger Abbey_clean.txt
│   ├── Pride and Prejudice_clean.txt
│   ├── Sense and Sensibility_clean.txt
├── shingles/
│   ├── Emma_shingles.txt
│   ├── Mansfield Park_shingles.txt
│   ├── Northanger Abbey_shingles.txt
│   ├── Pride and Prejudice_shingles.txt
│   ├── Sense and Sensibility_shingles.txt
├── hashes/
│   ├── Emma_rolling_hashes.txt
│   ├── Mansfield Park_rolling_hashes.txt
│   ├── Northanger Abbey_rolling_hashes.txt
│   ├── Pride and Prejudice_rolling_hashes.txt
│   ├── Sense and Sensibility_rolling_hashes.txt
```

---

## Features

- Preprocess books and user input.
- Generate **k-word shingles** for efficient text comparison.
- Compute **rolling hashes** for fast similarity detection.
- Provide **autocomplete suggestions** based on preprocessed book data.
- Compute plagiarism scores including a **boost for longest consecutive matches**.
- **Command-line interface** for user input and results.

## Plagiarism Scoring Formula

Let:

• **M** = Number of matching shingles  
• **T** = Total user shingles  
• **L** = Longest consecutive matching sequence  

### Final Score
\[
\boxed{
\text{Score} =
\min \left(
\frac{M}{T}
\left(1 + \frac{L}{T}\right) 100,
100
\right)
}
\]

### Quick Meaning
- \(\frac{M}{T}\) → Overall similarity  
- \(\frac{L}{T}\) → Strength of consecutive copying  
- Score is capped at **100%**


---

## Dataset

- Source: [Project Gutenberg](https://www.gutenberg.org/) (free books)
- Books used:
  - Emma
  - Mansfield Park
  - Northanger Abbey
  - Pride and Prejudice
  - Sense and Sensibility
- Only the main content is used; books with over ~50,000 words (≈200 pages) are truncated for processing.

---

## Requirements

```

# Python version >= 3.9 is required

prompt_toolkit>=3.0.38

````

> `prompt_toolkit` is required only for live autocomplete in the CLI.

---

## How to Run

1. Clone the repository:

```bash
git clone <repository_url>
cd Plagiarism_detection_iCog-Labs
````

2. Install Requirments:

3. Run the project:

```bash
python main.py
```

4. Follow the command-line prompts:

   * Type your text for plagiarism checking.
   * Autocomplete suggestions appear as you type.
   * press Enter when you finish typring to see the plagiarism score.

---


## Possible Improvements

* Integrate a **web or mobile UI** for better user experience.

---

## License

MIT License


