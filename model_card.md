# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**SongSeeker 1.0**
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

The recommender takes in user song preferences spanning favorite artist, genre, mood, and various musical qualities (valence, energy, instrumental, etc) and gives the user song recommendations based on how similar the songs are to the users preference. The recommender assumes the user has a strong preference for certain genres and moods and recommends accordingly. The model is intended for classroom exploration and has a limited scope in songs it can recommend, but may be expanded later for personal use.

---

## 3. How the Model Works  

The features of the songs that are used include artist, genre, mood, energy, valence, tempo, duration, and if the song is instrumental. The user can indicate their preference for any of these features, where they can choose their favorite artist and list out multiple genres/moods they enjoy. The remaining features are numerical. The model turns these preferences into scores by comparing the song's categorical features (artist, genre, mood) to the song's features. In contrast, the numerical features use a distance metric to calculate a similarity score. 

---

## 4. Data  
 
There are 20 songs in the catalog and the genres represented include pop, rock, lofi, jazz, ambient, electronic, classical, k-pop, j-rock, synthwave, indie pop, and world. The moods represented include happy, chill, intense, energetic, melancholic, peaceful, and relaxed. The songs added mainly reflect the author's personal taste (k-pop, j-rock, and video game songs). Some notable genres and moods not in the dataset include: hip hop, rap, R&B, ballad, country, and sad songs. 

---

## 5. Strengths  

The system works well when the user specifies a small list of favorite genres and moods. Since the recommender prioritizes these features the most, the recommendation provided will be strong. The scoring captures how genre and mood can better capture musical vibes over specific qualities like tempo or duation. For instance, if a user specifies they enjoy rock songs, the system will most likely recommend a few rock songs to the user, as well as good mood/energy matches. 

---

## 6. Limitations and Bias 

The system biases towards genre and mood over other musical qualities, overfitting to generic music genres such as pop and rock. This causes adjacent genres to be missed despite having similar musical qualities (ex: rock vs j-rock or lofi vs ambient). Additionally, the system breaks down if a user specifies multiple genres or moods they enjoy. If a user's musical preferences spans all genres present in the dataset, then the recommendation system has a harder time finding stronger matches. 

---

## 7. Evaluation  

I evaluated the system by creating multiple user profiles spanning different musical tastes. Each profile prioritized a certain genre: pop, lofi, k-pop, and rock. What surprised me about the tests was that it was super confident for a lot of matches (above 80%) and struck a good balance between genre and mood recommendations. Sometimes I expected a song to rank higher because of its genre, but other songs having a better mood and other characteristics made it rank higher than the genre-consistent song. For example, take the "generic pop enjoyer" versus "asian music enjoyer" profiles. K-pop songs from BTS and NewJeans fell into both of those recommendations due to their mood and valence, even if the genre didn't necessarily match for the "generic pop enjoyer." 

---

## 8. Future Work  

I would expand the dataset to include a larger diversity of songs. Additionally, I would allow the user to indicate songs they have previously listened to. This would allow the system to automatically compute user preferences, especially for numerical features such as tempo and duration. Recommendation systems don't really ask for your favorite tempo or duration - so it would make sense for these to be learned features from a history of song listening. Furthermore, I would try to improve diversity by injecting randomness into the recommendation. Instead of being deterministic, add probability to make recommendations different every time. 

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned that recommender systems are oddly complex, in the sense of how they need to quantify musical features like energy or valence. While my system has a rating for these numerical feautres, real recommender systems often use machine learning to compute more abstract representations of songs. Additionally, these systems have to balance content recommendation as well as collaborative recommendation and I can see how its difficult to strike the perfect balance.