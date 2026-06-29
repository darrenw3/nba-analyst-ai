import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"
import { getPlayer } from "../api/players"
import { inchesToFeetAndInches } from "../utils/conversions"

function PlayerPage() {
    const { id } = useParams()
    const [player, setPlayer] = useState(null)
    const [error, setError] = useState(null)

    useEffect(() => {
        const fetchPlayer = async () => {
            try {
                const data = await getPlayer(id)
                setPlayer(data)
                setError(null)
            } catch (err) {
                console.log("Error fetching player:", err) // Log the error for debugging
                setError("Player not found.")
                setPlayer(null)
            }
        }

        fetchPlayer()
    }, [id])

    if (error) {
        return <p>{error}</p>
    }

    if (!player) {
        return <p>Loading...</p>
    }

    return (
        <div>
            <h1>{player.name}</h1>
            <p>Team: {player.team}</p>
            <p>Position: {player.position}</p>
            <p>Height: {inchesToFeetAndInches(player.height_inches)}</p>
            <p>Weight: {player.weight_lbs} lbs</p>
        </div>
    )
}

export default PlayerPage