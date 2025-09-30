import { useState } from "react";
import axios from "axios"

const apiUrl = import.meta.env.VITE_BASE_URL;

const BookSearch = () => {
    const [isbn, setIsbn] = useState("");
    const [book, setBook] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    const handleSearch = async () => {
        if (!isbn) return;
        setLoading(true);
        setError("");
        setBook(null);

        try {
            const response = await axios.get(`${apiUrl}/v1/books/`, {
                params: { isbn },
            });

            const data = Array.isArray(response.data) ? response.data[0] : response.data.data;

            if (!data) throw new Error("Book not found");
            setBook(data);
        } catch (err) {
            setError(err.response?.data?.message || err.message || "Error fetching book");
        } finally {
            setLoading(false);
        }
    };

    const handleKeyPress = (e) => {
        if (e.key === "Enter") handleSearch();
    };

    return (
        <div className="book-search-container">
            <h1>📚 Search Book by ISBN</h1>

            <div className="book-search-input-container">
                <input
                    type="text"
                    placeholder="Enter ISBN"
                    value={isbn}
                    onChange={(e) => setIsbn(e.target.value)}
                    onKeyDown={(e) => {
                        if (e.key === "Enter") handleSearch();
                    }}
                />
                <button onClick={handleSearch}>Search</button>
            </div>

            {loading && <p className="book-search-loading">Loading...</p>}
            {error && <p className="book-search-error">{error}</p>}

            {book && (
                <div className="book-search-result">
                    <h2>{book.title}</h2>
                    <p><strong>Author:</strong> {book.author || "N/A"}</p>
                    <p><strong>Publisher:</strong> {book.publisher || "N/A"}</p>
                    <p><strong>Pages:</strong> {book.pages || "N/A"}</p>
                    <p><strong>ISBN:</strong> {book.isbn}</p>
                    <p className="description">{book.short_description || "No description available."}</p>
                    <a href={book.source} target="_blank" rel="noopener noreferrer">View on Open Library</a>
                </div>
            )}
        </div>
    );
};

export default BookSearch;
