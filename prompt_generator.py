def generate_prompt(name, gender, element, skill1, ultimate):
    return f"""/imagine prompt:
Generate a 3D anime-style character named {name}, a {gender.lower()} who controls {element}.
Their main skill is {skill1}. Their ultimate technique is {ultimate}.
Use cel-shading and dynamic lighting, inspired by anime like Genshin Impact and Naruto Storm."""
