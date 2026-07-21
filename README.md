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
```

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

```
 Top recommendations:

1. Sunrise City — Neon Echo (87% Match)
 Reasoning:  Genre: pop, Mood: happy, Instrumental match, Energy match, Valence match, Duration match

2. Super Shy — NewJeans (56% Match)
 Reasoning:  Mood: happy, Instrumental match, Energy match, Valence match, Duration match

3. Rooftop Lights — Indigo Parade (56% Match)
 Reasoning:  Mood: happy, Instrumental match, Energy match, Valence match

4. Dynamite — BTS (55% Match)
 Reasoning:  Mood: happy, Instrumental match, Energy match, Valence match

5. Gym Hero — Max Pulse (55% Match)
 Reasoning:  Genre: pop, Instrumental match, Energy match, Valence match, Duration match


Top recommendations:

1. Midnight Coding — LoRoom (99% Match)
 Reasoning:  Genre: lofi, Mood: chill, Artist: LoRoom, Instrumental match, Energy match, Valence match, Tempo match, Duration match

2. Library Rain — Paper Lanterns (89% Match)
 Reasoning:  Genre: lofi, Mood: chill, Instrumental match, Energy match, Valence match, Tempo match, Duration match

3. One Summer's Day — Joe Hisaishi (86% Match)
 Reasoning:  Genre: orchestral, Mood: peaceful, Instrumental match, Energy match, Valence match, Tempo match, Duration match

4. Spacewalk Thoughts — Orbit Bloom (84% Match)
 Reasoning:  Genre: ambient, Mood: chill, Instrumental match, Energy match, Valence match, Tempo match

5. Sweden — C418 (84% Match)
 Reasoning:  Genre: ambient, Mood: peaceful, Instrumental match, Energy match, Valence match, Tempo match


Top recommendations:

1. Kick Back — Kenshi Yonezu (84% Match)
 Reasoning:  Genre: j-rock, Mood: energetic, Energy match, Valence match

2. Dynamite — BTS (65% Match)
 Reasoning:  Mood: happy, Artist: BTS, Energy match, Valence match, Tempo match

3. Super Shy — NewJeans (56% Match)
 Reasoning:  Mood: happy, Energy match, Valence match, Tempo match, Duration match

4. Tank! — The Seatbelts (56% Match)
 Reasoning:  Mood: energetic, Energy match, Valence match, Duration match

5. Sunrise City — Neon Echo (56% Match)
 Reasoning:  Mood: happy, Energy match, Valence match, Tempo match


Top recommendations:

1. Storm Runner — Voltline (97% Match)
 Reasoning:  Genre: rock, Mood: intense, Artist: Voltline, Instrumental match, Energy match, Valence match, Tempo match, Duration match

2. Gurenge — LiSA (85% Match)
 Reasoning:  Genre: j-rock, Mood: intense, Instrumental match, Energy match, Valence match, Tempo match

3. Kick Back — Kenshi Yonezu (56% Match)
 Reasoning:  Genre: j-rock, Instrumental match, Energy match, Tempo match, Duration match

4. Gym Hero — Max Pulse (55% Match)
 Reasoning:  Mood: intense, Instrumental match, Energy match, Tempo match, Duration match

5. Megalovania — Toby Fox (54% Match)
 Reasoning:  Mood: intense, Energy match, Valence match, Tempo match, Duration match


Top recommendations:

1. Super Shy — NewJeans (99% Match)
 Reasoning:  Genre: k-pop, Energy match, Valence match

2. Dynamite — BTS (98% Match)
 Reasoning:  Genre: k-pop, Energy match, Valence match

3. Sunrise City — Neon Echo (97% Match)
 Reasoning:  Genre: pop, Energy match, Valence match

4. Gym Hero — Max Pulse (97% Match)
 Reasoning:  Genre: pop, Energy match, Valence match

5. Tank! — The Seatbelts (96% Match)
 Reasoning:  Genre: jazz, Energy match, Valence match
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

One experiment I ran was that I decreased the importance of genre and increased the importance of energy. Surprisingly, the results of the recommendation did not change drastically. Some of the songs in the top 5 shifted slightly, but overall did not change much. I suspect this is due to the fact that I have so many other song features in consideration (tempo, valence, instrumental, duration, etc) that decreases the important of genre and energy (despite those being relatively higher).

---

## Limitations and Risks

My recommender is limited by the songs represented in its database as well as its over-prioritization of genre and mood. Since the artist and song selection is limited, choosing genre/mood as a strong weight means that some genres go unseen by the recommender because those features are under a different category, but could be a good match musically. For example, those who only put "rock" as their favorite genre may not get recommended "j-rock" songs, despite those genres being close musically. Additionally, users are allowed to skip multiple fields, so those who are indifferent to genre/mood/energy will not get any interesting recommendations. Similarly, users who enjoy multiple genres with contrasting moods/energies may not get strong recommendations because my system doesn't account for users who enjoy a breadth of genres. 

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



