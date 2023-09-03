import random
from random import *
"""
Craft Etsy-like art: Infuse whimsical hues into a dream, conjuring feelings of nostalgia. Create enchanted scenes
with vibrant creatures and ethereal light. Imagine a world of endless possibilities where imagination roam. Blend
delicate details for cozy allure. Let twinkling tales unfold through intricate pathways. Capture essence frozen in
art. Express the Etsy spirit in AI art!"
"""

vd_adjectives = {
    "Psychedelic": [
        "Vibrant", "Dazzling", "Luminous", "Radiant", "Glistening",
        "Sparkling", "Vivid", "Surreal", "Spectacular", "Awe-inspiring",
        "Colorful", "Sublime", "Dramatic", "Nocturnal", "Breathtaking",
        "Jaw-dropping", "Dynamic", "Ethereal", "Mesmerizing", "Phosphorescent"
    ],
    "Comforting": [
        "Soothing", "Serene", "Calm", "Tranquil", "Harmonious",
        "Pristine", "Charming", "Elegant", "Dreamy", "Picturesque",
        "Idyllic", "Airy", "Enchanting", "Bucolic", "Velvety",
        "Lush", "Cozy", "Cushioned", "Blissful", "Embracing"
    ],
    "Silly": [
        "Playful", "Amusing", "Whimsical", "Comical", "Goofy",
        "Lighthearted", "Zany", "Quirky", "Fanciful", "Jovial",
        "Witty", "Entertaining", "Surreal", "Bizarre", "Offbeat",
        "Laughable", "Absurd", "Ridiculous", "Nonsensical", "Unconventional"
    ],
    "Natural": [
        "Gloomy", "Foggy", "Bustling", "Rustic", "Sunny",
        "Wild", "Stormy", "Pastel", "Airy", "Misty",
        "Lively", "Mysterious", "Dramatic", "Peaceful", "Serene",
        "Ethereal", "Dynamic", "Sublime", "Verdant", "Rippling"
    ],
    "Serene": [
        "Serene", "Calm", "Peaceful", "Tranquil", "Harmonious",
        "Majestic", "Breathtaking", "Gentle", "Soothing", "Sublime",
        "Dreamy", "Luminous", "Elegant", "Picturesque", "Radiant",
        "Idyllic", "Crisp", "Pastel", "Airy", "Whimsical"]
}
setting_nouns = {
    "Psychedelic": [
        "Dance Club", "Concert Venue", "Party Scene", "Light Display", "Art Exhibition",
        "Techno Party", "Neon Lights", "Visuals Show", "Aurora Sky", "Dreamy Atmosphere",
        "Funky Colors", "Laser Display", "Kaleidoscope Room", "Vibrant Spectacle", "Psychedelic Art",
        "Retro Dancefloor", "Electric Energy", "Groovy Vibes", "Colorful Patterns", "Trippy Decor"
    ],
    "Comforting": [
        "Cozy Cabin", "Country Retreat", "Peaceful Haven", "Warm Fireplace", "Quiet Nook",
        "Tea Room", "Meadow Retreat", "Relaxing Getaway", "Countryside Escape", "Heavenly Abode",
        "Homely Hearth", "Comfy Blanket", "Library Corner", "Tranquil Spot", "Serenity Cove",
        "Fireside Lounge", "Comfortable Lounge", "Elegant Setting", "Simple Pleasures", "Charming Space"
    ],
    "Silly": [
        "Circus Tent", "Amusement Park", "Playful Playground", "Laughter Zone", "Silliness Central",
        "Funny Farm", "Surreal Carnival", "Whimsical Fair", "Goofy Get-Together", "Zany World",
        "Comedy Club", "Joke Night", "Lighthearted Party", "Clown Show", "Hilarity House",
        "Absurd Adventure", "Ridiculous Spot", "Nonsensical Zone", "Funnyland", "Quirky Hangout"
    ],
    "Natural": [
        "Green Forest", "Sandy Beach", "Meadow Scenery", "Mountain View", "Riverside",
        "Woodland Area", "Desert Landscape", "Lakeside Serenity", "Golden Sunset", "Waterfall Setting",
        "Countryside Beauty", "Wilderness Escape", "Misty Woods", "Valley View", "Rainforest Serenade",
        "Island Paradise", "Fields of Green", "Tropical Oasis", "Savanna Vista", "Oasis Retreat"
    ],
    "Serene": [
        "Zen Garden", "Tranquil Retreat", "Serenity Spa", "Peaceful Lake", "Meditation Haven",
        "Harmony Oasis", "Idyllic Island", "Elegant Chateau", "Beachfront Bliss", "Quiet Sanctuary",
        "Gentle Stream", "Luminous Lagoon", "Radiant Oasis", "Crisp Morning", "Awe-inspiring Summit",
        "Pastoral Farm", "Soothing Sanctuary", "Northern Lights", "Nature's Beauty", "Whimsical Woods"
    ]
}
emotional_nouns = {
    "Psychedelic": [
        "Euphoria", "Ecstasy", "Bliss", "Excitement", "Awe",
        "Wonder", "Happiness", "Exhilaration", "Rapture", "Thrill",
        "Elation", "Delight", "Fascination", "Enchantment", "Amazement",
        "Intoxication", "Sensationalism", "Frenzy", "Hysteria", "Eccentricity"
    ],
    "Comforting": [
        "Warmth", "Coziness", "Serenity", "Peace", "Contentment",
        "Tranquility", "Security", "Reassurance", "Ease", "Comfort",
        "Well-being", "Harmony", "Calmness", "Relaxation", "Embrace",
        "Safety", "Gentleness", "Joy", "Nurturing", "Affection"
    ],
    "Silly": [
        "Laughter", "Amusement", "Giggles", "Mirth", "Whimsy",
        "Foolery", "Silliness", "Absurdity", "Nonsense", "Hilarity",
        "Jokes", "Entertainment", "Clowning", "Playfulness", "Glee",
        "Merriment", "Lightheartedness", "Comic Relief", "Joyfulness", "Buffoonery"
    ],
    "Natural": [
        "Beauty", "Tranquility", "Wonder", "Peace", "Serene",
        "Harmony", "Simplicity", "Balance", "Wholeness", "Grace",
        "Elegance", "Splendor", "Wilderness", "Renewal", "Connection",
        "Vitality", "Calmness", "Vividness", "Reflection", "Rejuvenation"
    ],
    "Serene": [
        "Calm", "Peace", "Tranquility", "Serenity", "Contentment",
        "Gentleness", "Harmony", "Stillness", "Balance", "Elegance",
        "Grace", "Beauty", "Repose", "Zen", "Meditation",
        "Reflection", "Purity", "Inner Peace", "Calmness", "Euphony"
    ]
}
feeling_adjectives = {
    "Psychedelic": [
        "Hypnotic", "Transcendent", "Mystical", "Electrifying", "Euphoric",
        "Mind-Bending", "Captivating", "Enigmatic", "Sensory", "Astonishing",
        "Dazzling", "Vivid", "Trippy", "Surreal", "Awe-Inspiring",
        "Phenomenal", "Futuristic", "Iridescent", "Dynamic", "Mesmerizing"
    ],
    "Comforting": [
        "Cuddly", "Nurturing", "Soothing", "Reassuring", "Healing",
        "Embracing", "Familiar", "Cozy", "Caring", "Tender",
        "Tranquil", "Restorative", "Gentle", "Relaxing", "Comfortable",
        "Serenading", "Harmonious", "Peaceful", "Inviting", "Rejuvenating"
    ],
    "Silly": [
        "Playful", "Whimsical", "Lighthearted", "Amusing", "Jovial",
        "Zany", "Quirky", "Hilarious", "Absurd", "Frolicsome",
        "Giggly", "Entertaining", "Laughable", "Jolly", "Merry",
        "Comical", "Goofy", "Mirthful", "Ticklish", "Witty"
    ],
    "Natural": [
        "Connected", "Refreshed", "Renewed", "Energized", "Awakened",
        "Revitalized", "Grounded", "Invigorated", "Living", "Inspired",
        "Serene", "Balanced", "Harmonious", "Simplicity", "Vital",
        "Restored", "Rejuvenated", "Free", "Aligned", "Abundant"
    ],
    "Serene": [
        "Calm", "Tranquil", "Peaceful", "Serene", "Balanced",
        "Elegant", "Graceful", "Beautiful", "Reposed", "Meditative",
        "Zen-like", "Quiet", "Purified", "Elevated", "Satisfying",
        "Blissful", "Contented", "Joyful", "Seraphic", "Elysian"
    ]
}
idea_nouns = {
    "Psychedelic": [
        "Innovation", "Exploration", "Revelation", "Metamorphosis", "Breakthrough",
        "Revolution", "Escapism", "Expansion", "Awakening", "Enlightenment",
        "Fantasia", "Transcendence", "Paradigm Shift", "Eureka Moment", "Psyche Dive",
        "Mystique", "Perception Shift", "Neurodazzle", "Virtual Reality", "Esoterica"
    ],
    "Comforting": [
        "Coziness", "Simplicity", "Harmony", "Relaxation", "Solace",
        "Nurturing", "Familiarity", "Calmness", "Reassurance", "Contentment",
        "Sanctuary", "Embrace", "Tranquility", "Affection", "Rejuvenation",
        "Wholesomeness", "Gentleness", "Serendipity", "Empathy", "Gratitude"
    ],
    "Silly": [
        "Amusement", "Humor", "Laughter", "Absurdity", "Whimsy",
        "Lightheartedness", "Playfulness", "Zaniness", "Quirkiness", "Folly",
        "Nonsensicality", "Comic Relief", "Entertainment", "Farcicality", "Tomfoolery",
        "Jest", "Merriment", "Ridiculousness", "Hilarity", "Satire"
    ],
    "Natural": [
          "Ecosystem", "Diversity", "Preservation", "Harmony", "Sustainability",
    "Resilience", "Guardians", "Ethics", "Interconnectedness", "Bounty",
    "Environment", "Equilibrium", "Habitat", "Bio-diversity", "Wildlife",
    "Conservancy", "Landscape", "Holism", "Vitality", "Heritage"
    ],
    "Serene": [
        "Meditation", "Mindfulness", "Tranquility", "Serenity", "Reflection",
        "Balance", "Inner Peace", "Harmony", "Zen", "Elegance",
        "Purity", "Grace", "Calmness", "Equanimity", "Spirituality",
        "Contemplation", "Stillness", "Enlightenment", "Transcendence", "Catharsis"
    ]
}
visual_pattern_nouns = {
    "Psychedelic": [
        "mandala", "kaleidoscope", "fractal", "tracery", "symmetry",
        "abstraction", "pattern", "illusion", "mosaic", "tessellation",
        "labyrinth", "complexity", "vortex", "geometric", "optical",
        "spectacle", "design", "intricacy", "ornament", "dazzle"
    ],
    "Comforting": [
        "quilting", "lacework", "weaving", "texture", "pattern",
        "elegance", "coziness", "relaxation", "serenity", "tranquility",
        "gentleness", "harmony", "calm", "comfort", "softness",
        "soothing", "embracing", "homely", "tenderness", "plush"
    ],
    "Silly": [
        "doodles", "cartoon", "whirligig", "antics", "playfulness",
        "nonsense", "fun", "giggles", "comedy", "zany",
        "lightheartedness", "mirth", "laughter", "hilarity", "quirkiness",
        "absurdity", "foolery", "joviality", "clowning", "merriment"
    ],
    "Natural": [
        "texture", "formations", "patterns", "veins", "ripples",
        "ridges", "growth", "grain", "corals", "petals",
        "waves", "mosaic", "stones", "moss", "branches",
        "leaves", "bark", "lily", "sand", "boulders"
    ],
    "Serene": [
        "layout", "shapes", "designs", "contours", "impressions",
        "figures", "outlines", "symbols", "sketches", "abstractions",
        "configurations", "traceries", "intricateness", "drawings", "compositions",
        "renderings", "depictions", "renderings", "depictions", "intricacy"
    ]
}






class Prompt():
    def __init__(self, category):
        self.category = category
        self.vda = ""
        self.s_noun = ""
        self.e_noun = ""
        self.f_adj = ""
        self.i_noun = ""
        self.vpn = ""
        self.prompt = """Craft Etsy-like art: Implement [vda] hues into a [s.noun] , conjuring feelings of [e.noun] . 
        Create [vda] scenes with [f.adj]  [i.noun]  and  [f.adj]  [i.noun] . Imagine a [i.noun] of [f.adj] [i.noun] 
        where imagination roams. Blend delicate details for [vda] allure. Let [f.adj] [i.noun] unfold through 
        intricate [vpn]. Express the Etsy spirit in AI art!"""
    # def choose_word_from_dict(self, dict_of_words):
    #      return dict_of_words[self.category][randint(0, len(dict_of_words) - 1)]
    #
    # def generate_vda(self):
    #     self.vda = self.choose_word_from_dict(vd_adjectives)
    #
    # def generate_s_noun(self):
    #     self.s_noun = self.choose_word_from_dict(setting_nouns)
    #
    # def generate_e_noun(self):
    #     self.e_noun = self.choose_word_from_dict(emotional_nouns)
    #
    # def generate_f_adj(self):
    #     self.f_adj = self.choose_word_from_dict(feeling_adjectives)
    #
    # def generate_i_nouns(self):
    #     self.i_noun = self.choose_word_from_dict(idea_nouns)
    #
    # def generate_vpn(self):
    #     self.vpn = self.choose_word_from_dict(visual_pattern_nouns)
    #
    # def substitute_word(self):
    #     prompt = self.prompt.split()
    #     for index, word in enumerate(prompt):
    #         if word == "[noun]":
    #             self.generate_noun()
    #             word = self.noun
    #             prompt[index] = word
    #             self.prompt = ' '.join(prompt)
    #         if word == "[adjective]":
    #             self.generate_adj()
    #             word = self.adjective
    #             prompt[index] = word
    #             self.prompt = ' '.join(prompt)
    #         if word == "[adverb]":
    #             self.generate_adv()
    #             word = self.adverb
    #             prompt[index] = word
    #             self.prompt = ' '.join(prompt)
    #     print(self.prompt)


    def generate_word(self, word_type):
        if word_type == "vda":
            return random.choice(vd_adjectives[self.category])  # You can choose a category here
        elif word_type == "f.adj":
            return random.choice(feeling_adjectives[self.category])  # You can choose a category here
        elif word_type == "i.noun":
            return random.choice(idea_nouns[self.category])  # You can choose a category here
        elif word_type == "vpn":
            return random.choice(visual_pattern_nouns[self.category])  # You can choose a category here
        elif word_type == "s.noun":
            return random.choice(setting_nouns[self.category])  # You can choose a category here
        elif word_type == "e.noun":
            return random.choice(emotional_nouns[self.category])  # You can choose a category here
        else:
            return "UNKNOWN"

    def substitute_word(self, word_type):
        prompt = self.prompt.split()
        for index, word in enumerate(prompt):
            if word == f"[{word_type}]":
                new_word = self.generate_word(word_type)
                prompt[index] = new_word
        self.prompt = ' '.join(prompt)



