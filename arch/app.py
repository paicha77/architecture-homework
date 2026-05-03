from flask import Flask, render_template

app = Flask(__name__)

buildings = [
    {
        "id": 1,
        "title": "Fallingwater",
        "image": "Fallingwater.jpg",
        "text": "A house built over a waterfall in Pennsylvania, designed by Frank Lloyd Wright.",
        "full_text": "Fallingwater, designed by Frank Lloyd Wright in 1935, is widely considered one of the greatest architectural masterpieces of the 20th century. Located in Pennsylvania, the house is built directly above a natural waterfall, creating a seamless connection between human design and the natural environment. Wright used cantilevered terraces made of reinforced concrete, allowing the structure to extend boldly over the water. The design follows his philosophy of organic architecture, where buildings should harmonize with their surroundings. The interior uses natural stone, open spaces, and large glass windows to bring the outside in. Fallingwater is not just a house—it is an experience of living within nature itself."
    },
    {
        "id": 2,
        "title": "Burj Khalifa",
        "image": "burj_khalifa..png",
        "text": "The tallest building in the world, located in Dubai.",
        "full_text": "The Burj Khalifa in Dubai is the tallest building in the world, standing at an incredible height of 828 meters with more than 160 floors. Completed in 2010, it was designed by the architectural firm Skidmore, Owings & Merrill. The tower’s design is inspired by Islamic architecture, particularly the shape of the Hymenocallis flower. It features a Y-shaped floor plan that maximizes views and stability. The building includes residential apartments, offices, luxury hotels, and observation decks offering breathtaking views of the city. Advanced engineering techniques were required to withstand strong winds and extreme temperatures. The Burj Khalifa has become a global icon of innovation, luxury, and modern urban development."
    },
    {
        "id": 3,
        "title": "Sydney Opera House",
        "image": "Sydney.jpg",
        "text": "Famous Australian building with sail-like architecture.",
        "full_text": "The Sydney Opera House, located in Sydney Harbour, Australia, is one of the most recognizable buildings in the world. Designed by Danish architect Jørn Utzon, it was completed in 1973 after years of complex construction. Its distinctive roof structure resembles a series of white sails or shells, making it a masterpiece of modern expressionist architecture. The building hosts over 1,500 performances each year, including opera, theater, and concerts. It is also a UNESCO World Heritage Site, recognized for its cultural and architectural significance. The Opera House combines artistic creativity with advanced engineering, making it a symbol of Australia’s identity and creativity."
    },
    {
        "id": 4,
        "title": "Eiffel Tower",
        "image": "eiffel_tower.jpg",
        "text": "Iconic iron tower located in Paris, France.",
        "full_text": "The Eiffel Tower, located in Paris, France, was designed by engineer Gustave Eiffel and completed in 1889 for the Exposition Universelle (World’s Fair). Standing at approximately 330 meters tall, it was the tallest man-made structure in the world at the time of its completion. Initially criticized by artists and intellectuals, it later became one of the most beloved landmarks globally. The tower is made of iron and consists of more than 18,000 individual pieces. Visitors can climb or take elevators to various observation levels for panoramic views of Paris. Today, it attracts millions of tourists annually and is a global symbol of romance, engineering, and French culture."
    },
    {
        "id": 5,
        "title": "Taj Mahal",
        "image": "taj_mahal.jpg",
        "text": "White marble mausoleum built as a symbol of love in India.",
        "full_text": "The Taj Mahal, located in Agra, India, is one of the most beautiful and iconic buildings in the world. It was commissioned by Mughal Emperor Shah Jahan in 1632 in memory of his beloved wife Mumtaz Mahal. Constructed from white marble, the structure features intricate carvings, inlaid gemstones, and symmetrical gardens. The central dome rises majestically above the tomb, surrounded by four minarets. The design combines elements of Islamic, Persian, and Indian architecture. The Taj Mahal changes color depending on the time of day, reflecting sunlight in unique ways. It is a UNESCO World Heritage Site and is often regarded as the ultimate symbol of eternal love."
    },
    {
        "id": 6,
        "title": "Guggenheim Museum",
        "image": "guggenheim.jpg",
        "text": "Modern art museum in New York with spiral design.",
        "full_text": "The Solomon R. Guggenheim Museum in New York City, designed by Frank Lloyd Wright, is a groundbreaking work of modern architecture. Completed in 1959, the building is famous for its unique spiral shape, which contrasts with the rectangular grid of Manhattan streets. Instead of traditional floors, visitors walk along a continuous ramp that gradually ascends around a central atrium. This design creates a fluid and immersive experience for viewing art. The museum houses an extensive collection of modern and contemporary works. Wright’s innovative vision challenged conventional museum design and continues to influence architects around the world."
    }
]

architects = [
    {
        "id": 1,
        "name": "Zaha Hadid",
        "text": "Futuristic fluid architecture.",
        "bio": """Zaha Hadid was an Iraqi-British architect and one of the most influential figures in modern architecture. She was the first woman to receive the Pritzker Architecture Prize. Her designs are famous for their futuristic, flowing, and dynamic shapes that often look like they are moving or melting. 

She rejected traditional straight lines and instead used curves, sharp angles, and organic forms inspired by nature and mathematics. Some of her most famous works include the Guangzhou Opera House in China, the Heydar Aliyev Center in Azerbaijan, and the London Aquatics Centre built for the Olympics.

Her work changed the way people think about architecture, pushing boundaries of what buildings could look like and how they interact with space. Even after her death in 2016, her influence continues to shape contemporary architecture around the world."""
    },

    {
        "id": 2,
        "name": "Frank Lloyd Wright",
        "text": "Organic architecture pioneer.",
        "bio": """Frank Lloyd Wright was an American architect who developed the philosophy of “organic architecture,” meaning buildings should blend naturally with their environment. He believed architecture should not dominate nature but exist in harmony with it.

One of his most famous works is Fallingwater, a house built directly over a waterfall, perfectly integrated into its natural surroundings. Another iconic project is the Guggenheim Museum in New York, known for its spiral ramp design.

Wright designed over 1,000 structures during his lifetime, including homes, churches, offices, and museums. His Prairie Style homes emphasized horizontal lines, open interior spaces, and natural materials. His ideas deeply influenced modern residential design and continue to inspire architects today."""
    },

    {
        "id": 3,
        "name": "Le Corbusier",
        "text": "Modernism master.",
        "bio": """Le Corbusier was a Swiss-French architect, designer, and urban planner who became one of the pioneers of modern architecture. He believed buildings should be functional, simple, and designed for modern life.

He introduced the concept of the “Five Points of Architecture,” which included pilotis (support columns), flat roofs, open floor plans, horizontal windows, and free façade design. These ideas shaped modernist architecture worldwide.

His famous works include Villa Savoye in France and the planning of the city of Chandigarh in India. He also influenced urban planning with his idea of organized, high-density cities.

Le Corbusier’s ideas were controversial but extremely influential, shaping the development of modern cities and skyscrapers throughout the 20th century."""
    },

    {
        "id": 4,
        "name": "Norman Foster",
        "text": "High-tech design expert.",
        "bio": """Norman Foster is a British architect known for pioneering high-tech architecture, which combines modern engineering, glass, steel, and advanced technology to create efficient and futuristic buildings.

He founded Foster + Partners, one of the most famous architecture firms in the world. His notable works include the Gherkin in London, the Apple Park headquarters in California, and the Millau Viaduct in France.

Foster’s designs often focus on sustainability, energy efficiency, and integration with modern technology. He believes buildings should be environmentally responsible while still being visually striking.

His work has shaped modern skylines across the world and set new standards for corporate and sustainable architecture."""
    },

    {
        "id": 5,
        "name": "Antoni Gaudí",
        "text": "Surreal organic architecture.",
        "bio": """Antoni Gaudí was a Spanish architect known for his highly unique, colorful, and nature-inspired architectural style. He is the most famous representative of Catalan Modernism.

His masterpiece is the Sagrada Família in Barcelona, a massive basilica still under construction after more than a century. Gaudí’s designs often feature organic shapes, flowing lines, mosaics, and structures inspired by nature such as trees, bones, and waves.

Other famous works include Park Güell, Casa Batlló, and Casa Milà. His buildings look almost like fantasy worlds rather than traditional architecture.

Gaudí’s work is deeply symbolic, blending religion, nature, and geometry. Today, he is considered one of the greatest creative minds in architectural history."""
    },

    {
        "id": 6,
        "name": "Tadao Ando",
        "text": "Minimalist concrete master.",
        "bio": """Tadao Ando is a Japanese architect known for his minimalist style, which uses concrete, natural light, and empty space to create calm and spiritual environments.

He is self-taught and originally worked as a boxer before becoming an architect. His designs focus on simplicity, silence, and the relationship between light and shadow.

One of his most famous works is the Church of the Light in Japan, where a simple cross-shaped opening allows natural light to enter the building. Another example is the Pulitzer Arts Foundation in the United States.

Ando’s architecture often feels meditative, removing unnecessary decoration and focusing on pure form and atmosphere. His work has had a major influence on minimalist design worldwide."""
    },

    {
        "id": 7,
        "name": "Bjarke Ingels",
        "text": "Innovative sustainable design.",
        "bio": """Bjarke Ingels is a Danish architect known for his innovative and playful approach to modern architecture. He founded the firm BIG (Bjarke Ingels Group), which creates buildings that combine sustainability, functionality, and creativity.

His designs often challenge traditional architecture by mixing practicality with bold, unusual shapes. Projects like 8 House in Copenhagen and VIA 57 West in New York show his experimental approach.

Ingels is known for the concept of “pragmatic utopian architecture,” meaning buildings should be both realistic and visionary at the same time. He also focuses heavily on environmental sustainability and urban living solutions.

His work represents a new generation of architects who think beyond traditional boundaries."""
    },

    {
        "id": 8,
        "name": "I. M. Pei",
        "text": "Geometric modern icon.",
        "bio": """I. M. Pei was a Chinese-American architect known for his elegant, geometric, and modernist designs. He combined simplicity with bold shapes, often using glass, stone, and precise angles.

His most famous work is the Louvre Pyramid in Paris, a glass structure that became one of the most iconic modern additions to a historic building. Other notable works include the Bank of China Tower in Hong Kong and the National Gallery of Art East Building in Washington, D.C.

Pei’s style balanced modern design with respect for historical context. He often worked with light, geometry, and symmetry to create visually striking yet harmonious buildings.

He received the Pritzker Prize in 1983 and is considered one of the most important architects of the 20th century."""
    }
]

georgian_buildings = [
    {
        "id": 1,
        "title": "Svetitskhoveli Cathedral",
        "image": "svetitskhoveli.jpg",
        "text": "One of Georgia’s most important religious buildings located in Mtskheta.",
        "full_text": "Svetitskhoveli Cathedral is a masterpiece of Georgian Orthodox architecture and one of the most sacred places in the country. Built in the 11th century, it is believed to be the burial site of Christ's robe. The cathedral is a UNESCO World Heritage Site and represents the spiritual heart of Georgia."
    },
    {
        "id": 2,
        "title": "Gergeti Trinity Church",
        "image": "gergeti.jpg",
        "text": "A 14th-century church located high in the Caucasus Mountains.",
        "full_text": "Gergeti Trinity Church sits dramatically at 2,170 meters above sea level near Stepantsminda. Built in the 14th century, it stands against the backdrop of Mount Kazbek and symbolizes Georgia’s strength, isolation, and spiritual devotion."
    },
    {
        "id": 3,
        "title": "Narikala Fortress",
        "image": "narikala.jpg",
        "text": "Ancient fortress overlooking Tbilisi with stunning views.",
        "full_text": "Narikala Fortress is one of the oldest defensive structures in Tbilisi, dating back to the 4th century. Overlooking the Mtkvari River, it has been rebuilt many times by different empires and remains a symbol of the city’s long and complex history."
    },
    {
        "id": 4,
        "title": "Batumi Alphabet Tower",
        "image": "alphabet.jpg",
        "text": "Modern architectural symbol representing the Georgian alphabet.",
        "full_text": "The Batumi Alphabet Tower is a modern landmark inspired by the unique Georgian script. Designed in a DNA-like spiral structure, it celebrates the identity and culture of the Georgian language and stands as a symbol of modern Batumi."
    },
    {
        "id": 5,
        "title": "Rabati Castle",
        "image": "rabati.jpg",
        "text": "Restored medieval castle complex in Akhaltsikhe.",
        "full_text": "Rabati Castle is a historic fortress complex combining medieval, Ottoman, and modern architectural styles. Recently restored, it includes churches, mosques, gardens, and museums, reflecting Georgia’s multicultural history."
    },
    {
        "id": 6,
        "title": "Peace Bridge",
        "image": "peace_bridge.jpg",
        "text": "A modern glass bridge in Tbilisi connecting old and new districts.",
        "full_text": "The Bridge of Peace is a futuristic glass-and-steel pedestrian bridge designed by Michele De Lucchi. Opened in 2010, it connects Old Tbilisi with the modern Rike Park and symbolizes unity and progress."
    }
]
@app.route("/")
def home():
    return render_template("index.html", buildings=buildings, architects=architects, georgian_buildings=georgian_buildings)

@app.route("/architects/<int:architect_id>")
def architect_detail(architect_id):
    for a in architects:
        if a["id"] == architect_id:
            return render_template("architects.html", architect=a)
    return "Architect Not Found"

@app.route("/best-buildings/<int:buildings_id>")
def building(buildings_id):
    for b in buildings:
        if b["id"] == buildings_id:
            return render_template("best_buildings.html", building=b)
    return "Building Not Found"

@app.route("/login")
def login():
    return render_template("login.html",)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/georgian-buildings/<int:georgian_id>")
def georgian_building_detail(georgian_id):
    for g in georgian_buildings:
        if g["id"] == georgian_id:
            return render_template("georgian_building.html", georgian=g)

    return "Georgian Building Not Found"




app.run(debug=True)