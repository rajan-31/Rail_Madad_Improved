import React, { useState } from 'react';

function ComplaintForm() {
    const [description, setDescription] = useState('');
    const [image, setImage] = useState(null);
    const [response, setResponse] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = {
            description,
            image
        };

        // Send to backend
        const res = await fetch('http://localhost:5000/process_complaint', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        const data = await res.json();
        setResponse(data);
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>Description:</label>
                <input
                    type="text"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                />
                <label>Upload Image:</label>
                <input
                    type="file"
                    onChange={(e) => setImage(e.target.files[0])}
                />
                <button type="submit">Submit Complaint</button>
            </form>

            {response && (
                <div>
                    <h2>Response from Server:</h2>
                    <p>Category: {response.category}</p>
                    <p>Priority: {response.priority}</p>
                    <p>Keywords: {response.keywords}</p>
                    <p>Metadata: {response.metadata}</p>
                </div>
            )}
        </div>
    );
}

export default ComplaintForm;
