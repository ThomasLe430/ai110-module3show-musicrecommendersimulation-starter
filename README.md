# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Real recommendation systems work by quantifying items as vectors and using computational/mathematical algorithms to compute items that match user's preferences. Each item (song or YT video) is turned into feature vectors and a neural network is trained to learn these numerical representations. The scoring function often uses cosine similarity or L2 distance (I am researching these in my lab!). Context based information such as whats trending and what others users enjoy is also taken into consideration - and a hybrid approach (content + collaborative) is the norm for many systems. 

My design compares song features with users preferences to calculate a recommendation score. The song features I am using include general vibes (artist, genre, mood) and audio characteristics (energy, tempo, valence, instrumental, duration). The UserProfile dataclass stores the user's favorite artist and favorite genres/moods. Additionally, the class stores target energy, tempo, valence, duration, and instrumental preference. 

My recommender computes a score for each song based on the feature type, where categorical features are checked for equality and numerical features are used to compute a distance metric. Each feature also has a weighting, where favorite vibes (artist, genre, mood) will be weighted more than numerical features. In order choose which songs to recommend, the system will choose the ones with the highest score. This may cause a bias towards genre, where the system might ignore good recommendations that match the user's preferred energy and valence levels because of a genre mismatch.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



