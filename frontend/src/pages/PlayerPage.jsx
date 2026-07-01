import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"
import { getPlayer, getPlayerStats } from "../api/players"
import { inchesToFeetAndInches } from "../utils/conversions"

function PlayerPage() {
    const { id } = useParams()
    const [player, setPlayer] = useState(null)
    const [stats, setStats] = useState([])
    const [error, setError] = useState(null)

    useEffect(() => {
        const fetchData = async () => {
            try {
                const playerData = await getPlayer(id)
                setPlayer(playerData)
                const statsData = await getPlayerStats(id)
                setStats(statsData)
                setError(null)
            } catch (err) {
                console.log("Error fetching player:", err) // Log the error for debugging
                setError("Player not found.")
                setPlayer(null)
            }
        }

        fetchData()
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

            <h2>Season Stats</h2>
            <table>
                <thead>
                    <tr>
                        <th>Season</th>
                        <th>GP</th>
                        <th>PTS</th>
                        <th>REB</th>
                        <th>AST</th>
                        <th>STL</th>
                        <th>BLK</th>
                        <th>FG%</th>
                        <th>3P%</th>
                        <th>FT%</th>
                    </tr>
                </thead>
                <tbody>
                    {stats.map(s => (
                        <tr key={s.id}>
                            <td>{s.season}</td>
                            <td>{s.games_played}</td>
                            <td>{s.points_per_game}</td>
                            <td>{s.rebounds_per_game}</td>
                            <td>{s.assists_per_game}</td>
                            <td>{s.steals_per_game}</td>
                            <td>{s.blocks_per_game}</td>
                            <td>{s.field_goal_percentage}</td>
                            <td>{s.three_point_percentage}</td>
                            <td>{s.free_throw_percentage}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

export default PlayerPage