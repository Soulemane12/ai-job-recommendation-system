const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);

    try {
        // Upload the file to the backend
        const response = await axios.post('http://127.0.0.1:8000/upload', formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });

        // Check if the upload was successful
        if (response.data.message.includes("uploaded successfully")) {
            // Fetch the recommendations from the file
            const recommendationsResponse = await axios.get('http://127.0.0.1:8000/recommendations.json');
            setRecommendations(recommendationsResponse.data.recommendations || []);
            setKeywords(recommendationsResponse.data.keywords_found || []);
        }
    } catch (error) {
        console.error('Error uploading file:', error);
        setRecommendations(null);
        setKeywords([]);
    }
};
