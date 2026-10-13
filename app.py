"""
Main Flask Server Application Entry Point
Handles routing, prediction inference, and automated sample generation.
"""
from flask import Flask, render_template, request, jsonify
from backend.preprocessing import clean_news_text
from backend.inference import predict_article
import random

app = Flask(__name__, 
            template_folder="frontend/templates", 
            static_folder="frontend/static")

# Sample generator bank categorized by category AND type (real / fake)
SAMPLE_BANK = {
    "science": {
        "real": [
            {
                "type": "real",
                "title": "Space Telescope Captures High-Resolution Images of Distant Star Formation",
                "text": "Astronomers operating the orbital space telescope have released newly processed imagery detailing the dense stellar nursery within the Carina Nebula. The captured infrared data provides researchers with deeper insights into how protostars accumulate gas and dust during their initial developmental phases."
            },
            {
                "type": "real",
                "title": "Researchers Develop High-Efficiency Solar Cell Utilizing Perovskite Crystals",
                "text": "A team of materials scientists has engineered a tandem solar cell achieving over thirty percent operational efficiency in laboratory conditions. The breakthrough utilizes stable perovskite crystal structures deposited onto standard silicon wafers."
            }
        ],
        "fake": [
            {
                "type": "fake",
                "title": "Scientists Confirm Earth's Core is Actually Made of Giant Sparkling Diamonds",
                "text": "In a shocking press conference held earlier this morning, researchers at a clandestine laboratory revealed that seismic waves indicate our planet's inner core consists entirely of compressed, pure diamonds worth trillions of dollars. Local governments are already planning underground mining expeditions."
            },
            {
                "type": "fake",
                "title": "Secret Alien Artifact Unearthed Under Martian Ice Cap by Autonomous Rover",
                "text": "Leaked communications from deep space command suggest that autonomous survey vehicles discovered a metallic pyramid structure under Martian glaciers. NASA officials allegedly classified all high-resolution imagery immediately following transmission."
            }
        ]
    },
    "politics": {
        "real": [
            {
                "type": "real",
                "title": "Global Central Banks Maintain Interest Rates Amid Steady Inflation Data",
                "text": "Financial authorities across major developed economies decided to hold benchmark interest rates steady during their latest policy meeting. Recent reports show consumer price index metrics cooling down toward target levels, prompting economists to project a stable economic outlook."
            },
            {
                "type": "real",
                "title": "Bipartisan Infrastructure Bill Passes Senate Following Extended Debate",
                "text": "Legislators concluded negotiations late Tuesday night to approve funding allocated toward highway reconstruction, bridge repairs, and municipal water system modernization across rural districts."
            }
        ],
        "fake": [
            {
                "type": "fake",
                "title": "Secret Government Memo Reveals Plans to Ban All Paper Currency Next Week",
                "text": "An anonymous whistleblower has leaked confidential documents proving that international leaders have secretly voted to completely eliminate physical money and replace it with mandatory microchip tracking by Friday midnight."
            },
            {
                "type": "fake",
                "title": "World Leaders Replaced by Synthetic Androids After Emergency Summit",
                "text": "Investigative bloggers claim that high-ranking political figures attending last month's economic summit were covertly replaced by bio-synthetic clones designed by underground tech corporations."
            }
        ]
    },
    "health": {
        "real": [
            {
                "type": "real",
                "title": "Clinical Trials Show Promising Results for New Cardiovascular Treatment",
                "text": "Medical researchers published a comprehensive multi-center study in the New England Journal of Medicine detailing a novel therapeutic approach that reduces arterial plaque buildup safely in adult patients over a twelve-month observation period."
            },
            {
                "type": "real",
                "title": "Global Health Agency Releases Updated Dietary Guidelines for Heart Longevity",
                "text": "Public health advisory boards issued revised nutritional recommendations emphasizing plant-based proteins, reduced sodium consumption, and routine cardiovascular exercise for long-term health."
            }
        ],
        "fake": [
            {
                "type": "fake",
                "title": "Miracle Cure Discovered: Drink This Kitchen Juice to Reverse Aging in 3 Days",
                "text": "Medical boards hate this simple secret! A retired physician living in a remote village has unlocked an ancient herbal remedy made from common household lemons and baking soda that completely melts away wrinkles overnight."
            },
            {
                "type": "fake",
                "title": "Single Ingredient Eliminates All Illnesses Permanently According to Underground Doctor",
                "text": "Pharmaceutical companies are scrambling to hide a breakthrough mineral compound harvested from deep ocean trenches that renders human immune systems completely immune to every virus in existence."
            }
        ]
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-sample", methods=["GET"])
def generate_sample():
    """Generates an automatic headline and body based on category and news type (real/fake)."""
    category = request.args.get("category", "science")
    news_type = request.args.get("type", "real")
    
    cat_data = SAMPLE_BANK.get(category, SAMPLE_BANK["science"])
    samples = cat_data.get(news_type, cat_data["real"])
    
    selected_sample = random.choice(samples)
    return jsonify(selected_sample)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    title = data.get("title", "")
    text = data.get("text", "")
    
    combined_input = clean_news_text(title, text)
    if not combined_input:
        return jsonify({"error": "Input text cannot be empty."}), 400
        
    result = predict_article(combined_input)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)