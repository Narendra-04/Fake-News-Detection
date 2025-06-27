    import React, { useState } from 'react';
    import './App.css'; // Assuming you have a basic App.css

    function App() {
      const [newsContent, setNewsContent] = useState('');
      const [result, setResult] = useState(null);
      const [loading, setLoading] = useState(false);
      const [error, setError] = useState(null);

      const handleSubmit = async (e) => {
        e.preventDefault(); // Prevent default form submission behavior (page reload)
        setLoading(true);
        setResult(null);
        setError(null);

        try {
          // Make a POST request to the Flask backend's /api/verify endpoint
          const response = await fetch('http://localhost:5000/api/verify', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json', // Tell the server we're sending JSON
            },
            body: JSON.stringify({ content: newsContent }), // Convert JS object to JSON string
          });

          if (!response.ok) {
            // Handle HTTP errors (e.g., 400, 500 status codes)
            throw new Error(`HTTP error! status: ${response.status}`);
          }

          const data = await response.json(); // Parse the JSON response from the backend
          setResult(data.result); // Update state with the classification result
        } catch (err) {
          console.error("Error verifying news:", err);
          setError("Failed to connect to the backend or an error occurred.");
        } finally {
          setLoading(false); // Always stop loading, regardless of success or failure
        }
      };

      return (
        <div className="App">
          <header className="App-header">
            <h1>Fake News Detector</h1>
          </header>
          <main>
            <form onSubmit={handleSubmit}>
              <textarea
                placeholder="Paste news article content here..."
                value={newsContent}
                onChange={(e) => setNewsContent(e.target.value)}
                rows="10"
                cols="80"
              ></textarea>
              <br />
              <button type="submit" disabled={loading || !newsContent.trim()}>
                {loading ? 'Analyzing...' : 'Verify News'}
              </button>
            </form>

            {error && <p className="error-message">{error}</p>}

            {result && (
              <div className="result-box">
                <h2>Detection Result:</h2>
                <p><strong>Classification:</strong> <span className={`classification ${result.classification.toLowerCase().replace(' ', '-')}`}>{result.classification}</span></p>
                <p><strong>Confidence:</strong> {Math.round(result.confidence * 100)}%</p>
                {/* You can add more details here based on your ML model's output */}
              </div>
            )}
          </main>
        </div>
      );
    }

    export default App;
    