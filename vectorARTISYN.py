from random import *
"""
Craft Etsy-like art: Infuse whimsical hues into a dream, conjuring feelings of nostalgia. Create enchanted scenes
with vibrant creatures and ethereal light. Imagine a world of endless possibilities where imagination roam. Blend
delicate details for cozy allure. Let twinkling tales unfold through intricate pathways. Capture essence frozen in
art. Express the Etsy spirit in AI art!"
"""
adjective_groups = {
    "Psychedelic": [
        "Kaleidoscopic", "Hypnotic", "Trippy", "Mind-Bending", "Groovy",
        "Vibrant", "Psychedelic", "Surreal", "Ethereal", "Whimsical",
        "Eccentric", "Radiant", "Mesmerizing", "Colorful", "Abstract"
    ],
    "Comforting": [
        "Cozy", "Warm", "Familiar", "Nurturing", "Cuddly",
        "Soothing", "Relaxing", "Homely", "Embracing", "Tender",
        "Gentle", "Inviting", "Heartwarming", "Tranquil", "Peaceful"
    ],
    "Serene": [
        "Tranquil", "Peaceful", "Calming", "Soothing", "Harmonious",
        "Still", "Quiet", "Serenading", "Calm", "Balancing",
        "Reflective", "Graceful", "Blissful", "Contemplative", "Elegant"
    ],
    "Energetic": [
        "Dynamic", "Vital", "Lively", "Electric", "Vigorous",
        "Energetic", "Pulsating", "Exhilarating", "Vibrant", "Active",
        "Zesty", "Animated", "Robust", "Ebullient", "Stimulating"
    ],
    "Natural": [
        "Organic", "Earthy", "Botanical", "Rustic", "Wild",
        "Natural", "Wholesome", "Eco-Friendly", "Harmonious", "Untamed",
        "Green", "Fresh", "Vivid", "Pristine", "Bountiful"
    ],
    "Silly": [
        "Playful", "Whimsical", "Amusing", "Quirky", "Cheerful",
        "Zany", "Witty", "Absurd", "Lighthearted", "Goofy",
        "Comical", "Foolish", "Jovial", "Mischievous", "Spirited"
    ]
}
noun_groups = {
    "Psychedelic": [
        "Kaleidoscope", "Lava Lamp", "Prism", "Disco Ball", "Rainbow Flag",
        "Blacklight Poster", "Mandala Tapestry", "UV Paints", "Colorful Wig", "Groovy Glasses"
    ],
    "Comforting": [
        "Blanket", "Teacup", "Book", "Fireplace", "Pillow",
        "Warm Socks", "Aromatherapy Candle", "Soft Robe", "Hot Cocoa", "Cozy Chair"
    ],
    "Serene": [
        "Zen Garden", "Wind Chimes", "Candle", "Water Fountain", "Nature Sounds",
        "Yoga Mat", "Chime Bells", "Buddha Statue", "Incense Holder", "Meditation Cushion"
    ],
    "Energetic": [
        "Dance Floor", "Boombox", "Jump Rope", "Soccer Ball", "Skateboard",
        "Basketball Hoop", "Frisbee", "Trampoline", "Kite", "Radio-Controlled Car"
    ],
    "Natural": [
        "Hiking Trail", "River Rock", "Wildflower", "Mountain Peak", "Tree Swing",
        "Binoculars", "Nature Journal", "Hammock", "Compass", "Bird Feeder"
    ],
    "Silly": [
        "Whoopie Cushion", "Rubber Duck", "Silly String", "Gag Glasses", "Circus Horn",
        "Funny Hat", "Bouncy Ball", "Wacky Wig", "Nose Glasses", "Fake Mustache"
    ]
}
adverb_groups = {
    "Psychedelic": [
        "Visually", "Vividly", "Mesmerizingly", "Unconventionally", "Enchantingly",
        "Surreally", "Dreamily", "Eclectically", "Imaginatively", "Eccentrically",
        "Intricately", "Radiantly", "Intensely", "Unpredictably", "Fantastically"
    ],
    "Comforting": [
        "Warmly", "Gently", "Softly", "Soothingly", "Tenderly",
        "Cozily", "Familiarly", "Nurturingly", "Lovingly", "Reassuringly",
        "Calmingly", "Comfortingly", "Emotionally", "Heartwarmingly", "Tranquilly"
    ],
    "Serene": [
        "Peacefully", "Calmly", "Serenely", "Quietly", "Harmoniously",
        "Gracefully", "Reflectively", "Gently", "Balancedly", "Tranquil",
        "Still", "Zenfully", "Yogically", "Blissfully", "Gracefully"
    ],
    "Energetic": [
        "Vigorously", "Energetically", "Dynamically", "Lively", "Vibrantly",
        "Excitingly", "Zestfully", "Enthusiastically", "Exuberantly", "Vividly",
        "Robustly", "Ebulliently", "Stimulatingly", "Electrifyingly", "Rapidly"
    ],
    "Natural": [
        "Organically", "Naturally", "Harmoniously", "Wildly", "Freely",
        "Greenly", "Bountifully", "Freshly", "Pristinely", "Earthily",
        "Sustainably", "Blossomingly", "Uniquely", "Untamedly", "Vividly"
    ],
    "Silly": [
        "Playfully", "Whimsically", "Amusingly", "Quirkily", "Cheerfully",
        "Zanily", "Wittily", "Absurdly", "Lightheartedly", "Foolishly",
        "Mischievously", "Jovially", "Spiritedly", "Comically", "Irreverently"
    ]
}


class Prompt():
    def __init__(self, category):
        self.category = category
        self.adjective = ""
        self.noun = ""
        self.adverb = ""
        self.prompt = """Craft Etsy-like art: Implement [adjective] hues into a [noun] , conjuring feelings of [noun] 
        . Create [adjective] scenes with [adjective]  [noun]  and  [adjective]  [noun ]. Imagine a [noun] of [
        adjective] [noun] where imagination roams. Blend delicate details for [adjective] allure. Let [adjective] [
        noun] unfold through intricate [noun]. Express the Etsy spirit in AI art!"""
    def choose_word_from_dict(self, dict_of_words):
         return dict_of_words[self.category][randint(0, len(dict_of_words) - 1)]

    def generate_adj(self):
        self.adjective = self.choose_word_from_dict(adjective_groups)

    def generate_noun(self):
        self.noun = self.choose_word_from_dict(noun_groups)

    def generate_adv(self):
        self.adverb = self.choose_word_from_dict(adverb_groups)

    def substitute_word(self):
        prompt = self.prompt.split()
        for index, word in enumerate(prompt):
            if word == "[noun]":
                self.generate_noun()
                word = self.noun
                prompt[index] = word
                self.prompt = ' '.join(prompt)
            if word == "[adjective]":
                self.generate_adj()
                word = self.adjective
                prompt[index] = word
                self.prompt = ' '.join(prompt)
            if word == "[adverb]":
                self.generate_adv()
                word = self.adverb
                prompt[index] = word
                self.prompt = ' '.join(prompt)
        print(self.prompt)


