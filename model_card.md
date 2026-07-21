# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

The system biases towards genre and mood over other musical qualities, overfitting to generic music genres such as pop and rock. This causes adjacent genres to be missed despite having similar musical qualities (ex: rock vs j-rock or lofi vs ambient). Additionally, the system breaks down if a user specifies multiple genres or moods they enjoy. If a user's musical preferences spans all genres present in the dataset, then the recommendation system has a harder time finding stronger matches. 

---

## 7. Evaluation  

I evaluated the system by creating multiple user profiles spanning different musical tastes. Each profile prioritized a certain genre: pop, lofi, k-pop, and rock. What surprised me about the tests was that it was super confident for a lot of matches (above 80%) and struck a good balance between genre and mood recommendations. Sometimes I expected a song to rank higher because of its genre, but other songs having a better mood and other characteristics made it rank higher than the genre-consistent song. For example, take the "generic pop enjoyer" versus "asian music enjoyer" profiles. K-pop songs from BTS and NewJeans fell into both of those recommendations due to their mood and valence, even if the genre didn't necessarily match for the "generic pop enjoyer." 

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
