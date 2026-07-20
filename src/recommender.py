import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    is_instrumental: bool
    duration: int

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_artist: str
    favorite_genres: List[str]
    favorite_moods: List[str]
    target_energy: float
    target_valence: float
    target_bpm: Optional[float] = None
    likes_instrumental: Optional[bool] = None
    target_duration: Optional[int] = None
    

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file
    Required by src/main.py
    """
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            songs.append({
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "isInstrumental": row["isInstrumental"].strip().lower() == "true",
                "duration": int(row["duration"]),
            })
    return songs

# Weight given to each preference when scoring a song. Genre and mood are
# weighted highest since "vibe" match matters most for a simple recommender;
# weights sum to 1.0 so a song matching every preference scores exactly 1.0.
SCORE_WEIGHTS = {
    "genre": 0.30,
    "mood": 0.30,
    "artist": 0.10,
    "energy": 0.10,
    "valence": 0.08,
    "tempo_bpm": 0.05,
    "instrumental": 0.02,
    "duration": 0.05,
}

# Spans used to normalize numerical distances onto a 0-1 scale before the
# inverse-distance calculation (energy/valence are already 0-1).
NUMERICAL_RANGES = {
    "energy": 1.0,
    "valence": 1.0,
    "tempo_bpm": 115.0, # Hard coded as the max(bpm) - min(bpm) in songs.csv
    "duration": 153.0, # Hard coded as the max(duration) - min(duration) in songs.csv
}

# If numerical features are scored above 0.7 --> Feature added
# to explanation list 
NUMERICAL_PREF_THRESHOLD = 0.7

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py

    Preferences the user didn't specify (missing from user_prefs, or
    missing from the song's data) are excluded from scoring entirely
    rather than counted as unsatisfied: the raw score is renormalized by
    the total weight of only the preferences actually evaluated, so a
    user who skips a preference can still reach a max score of 1.0.
    """
    score = 0.0
    specified_weight = 0.0
    reasons: List[str] = []

    # --- Categorical features: equality/existence checks ---
    for key, label in (("genre", "genre"), ("mood", "mood"), ("artist", "artist")):
        pref = user_prefs.get(key)
        value = song.get(key)
        if not pref or value is None:
            continue
        specified_weight += SCORE_WEIGHTS[key]
        wanted = pref if isinstance(pref, (list, tuple, set)) else [pref]
        wanted = {str(w).strip().lower() for w in wanted}
        if str(value).strip().lower() in wanted:
            score += SCORE_WEIGHTS[key]
            reasons.append(f"matches your favorite {label} ({value})")

    # Check instrumental preferences
    instrumental_pref = user_prefs.get("instrumental")
    song_instrumental = song.get("isInstrumental", song.get("is_instrumental"))
    if instrumental_pref is not None and song_instrumental is not None:
        specified_weight += SCORE_WEIGHTS["instrumental"]
        if bool(song_instrumental) == bool(instrumental_pref):
            score += SCORE_WEIGHTS["instrumental"]
            reasons.append("matches your instrumental preference")

    # --- Numerical features: inverse distance from target ---
    for key in ("energy", "valence", "tempo_bpm", "duration"):
        target = user_prefs.get(key)
        value = song.get(key)
        if target is None or value is None:
            continue
        specified_weight += SCORE_WEIGHTS[key]
        closeness = max(0.0, 1.0 - abs(float(value) - float(target)) / NUMERICAL_RANGES[key])
        score += SCORE_WEIGHTS[key] * closeness
        if closeness >= NUMERICAL_PREF_THRESHOLD:
            reasons.append(f"close match on {key} ({value} vs your preference of {target})")

    # Ensure no divide by zero
    if specified_weight == 0:
        return 0.0, reasons

    return round(min(score / specified_weight, 1.0), 4), reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    return []
