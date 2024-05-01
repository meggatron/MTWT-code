# Define the cards and their meanings with a dictionary called MajorArcanacards
MajorArcanacards = {
    "The Fool": "Beginnings, Risks, Spontaneity",
    "The Magician": "Manifestation, Resourcefulness, Power",
    "The High Priestess": "Intuition, Secrets, Unconscious",
    "The Empress": "Abundance, Mothering, Nature",
    "The Emperor": "Authority, Fathering, Control",
    "The Hierophant": "Tradition, Conformity, Spirituality",
    "The Lovers": "Love, Harmony, Trust",
    "The Chariot": "Determination, Willpower, Victory",
    "Strength": "Courage, Inner Strength, Self-Control",
    "The Hermit": "Soul-Searching, Solitude, Inner Guidance",
    "Wheel of Fortune": "Change, Cycles, Fate",
    "Justice": "Fairness, Justice, Balance",
    "The Hanged Man": "Surrender, Letting Go, Perspective",
    "Death": "Endings, Transformation, Change",
    "Temperance": "Balance, Harmony, Moderation",
    "The Devil": "Materialism, Egoism, Ignorance",
    "The Tower": "Destruction, Upheaval, Revelation",
    "The Star": "Hope, Inspiration, Serenity",
    "The Moon": "Illusion, Fear, Subconscious",
    "The Sun": "Happiness, Vitality, Confidence",
    "Judgement": "Rebirth, Renewal, Awakening",
    "The World": "Completion, Integration, Accomplishment"
}
'''
The For Loop iterates over each key-value pair in the MajorArcanacards
dictionary, assigning the tarot card name to the variable card and its
associated meaning to the variable meaning. It then prints each card and
its meaning using formatted string literals, separating them with
a colon and space.
'''
#Print each line using a for loop
for card, meaning in MajorArcanacards.items():
    print(f"{card}: {meaning}")  


