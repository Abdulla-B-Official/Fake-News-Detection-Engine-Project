let currentCategory = 'science';
let currentType = 'real';

function selectType(type) {
    currentType = type;
    
    // Toggle active state for Real/Fake buttons
    document.querySelectorAll('.pill-type').forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');
    
    fetchRandomSample();
}

function selectCategory(category) {
    currentCategory = category;
    
    // Toggle active state for category buttons
    document.querySelectorAll('.pill').forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');
    
    fetchRandomSample();
}

async function fetchRandomSample() {
    try {
        const response = await fetch(`/generate-sample?category=${currentCategory}&type=${currentType}`);
        const data = await response.json();
        
        document.getElementById("news-title").value = data.title;
        document.getElementById("news-text").value = data.text;
        
        // Store expected hint for UI display
        document.getElementById("expected-hint").dataset.expected = data.type;
    } catch (error) {
        console.error("Failed to load sample:", error);
    }
}

// Automatically load a sample on initial page render
window.onload = () => {
    fetchRandomSample();
};

async function analyzeNews() {
    const title = document.getElementById("news-title").value.trim();
    const text = document.getElementById("news-text").value.trim();
    
    if (!text) {
        alert("Please enter or generate article body content.");
        return;
    }

    const analyzeBtn = document.getElementById("analyze-btn");
    const loadingDiv = document.getElementById("loading");
    const resultContainer = document.getElementById("result-container");
    const predictionBadge = document.getElementById("prediction-badge");
    const confidenceBar = document.getElementById("confidence-bar");
    const confidenceScore = document.getElementById("confidence-score");
    const expectedHint = document.getElementById("expected-hint");

    analyzeBtn.disabled = true;
    loadingDiv.classList.remove("hidden");
    resultContainer.classList.add("hidden");

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ title: title, text: text })
        });

        const data = await response.json();

        if (response.ok) {
            predictionBadge.textContent = data.prediction;
            predictionBadge.className = `badge ${data.status}`;
            
            confidenceScore.textContent = data.confidence;
            confidenceBar.style.width = `${data.confidence}%`;
            
            const expectedType = expectedHint.dataset.expected;
            expectedHint.textContent = `Generated As: ${expectedType.toUpperCase()}`;
            
            resultContainer.classList.remove("hidden");
        } else {
            alert(data.error || "Prediction failed.");
        }
    } catch (error) {
        console.error("Error:", error);
        alert("Server connection error.");
    } finally {
        analyzeBtn.disabled = false;
        loadingDiv.classList.add("hidden");
    }
}