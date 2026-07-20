"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, score_song, recommend_songs


def main() -> None:
    # Returns a list of dictionaries representing each song
    songs = load_songs("data/songs.csv") 
    # Starter example profile (updated from original)
    user_prefs = {"artist":"Taylor Swift",
                   "genre": "pop",
                   "mood": "happy",
                   "energy": 0.8,
                   "valence":0.8,
                   "instrumental": False,
                    "tempo_bpm": None,
                    "duration": 150,
                   }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{rank}. {song['title']} — {song['artist']} ({score:.0%} Match)")
        print(" Reasoning:", f" {explanation}")
        print()


if __name__ == "__main__":
    main()
