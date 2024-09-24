import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [file, setFile] = useState(null);
    const [analysis, setAnalysis] = useState(null);

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
    };

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('http://127.0.0.1:8000/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            setAnalysis(response.data.analysis);
        } catch (error) {
            console.error('Error uploading file:', error);
        }
    };

    return (
        <div className="App">
            <h1>Document Upload and Analysis</h1>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload and Analyze</button>
            {analysis && (
                <div>
                    <h2>Analysis Results:</h2>
                    <p>Word Count: {analysis.word_count}</p>
                    <p>Unique Words: {analysis.unique_words}</p>
                    <h3>Most Common Words:</h3>
                    <ul>
                        {analysis.most_common_words.map(([word, count]) => (
                            <li key={word}>{word}: {count}</li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
}

export default App;