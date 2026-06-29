import { useState } from "react"
import { searchPlayers } from "../api/players"
import PlayerCard from "../components/PlayerCard"

function HomePage() {
    const [query, setQuery] = useState("")
    const [players, setPlayers] = useState([])
    const [error, setError] = useState(null)

    const handleSearch = async () => {
        try {
            const results = await searchPlayers(query)
            console.log("Search results:", results) // Log the search results for debugging
            setPlayers(results)
            setError(null)
        } catch (err) {
            console.log("Error searching players:", err) // Log the error for debugging
            setError("No players found.")
            setPlayers([])
        }
    }

    return (
        <div>
            <h1>NBA AI Analyst</h1>
            <input
                type="text"
                placeholder="Search for a player..."
                value={query}
                onChange={(e) => setQuery(e.target.value)}
            />
            <button onClick={handleSearch}>Search</button>
            {error && <p>{error}</p>}
            <div>
                {players.map((player) => (
                    <PlayerCard key={player.id} player={player} />
                ))}
            </div>
        </div>
    )
}

export default HomePage