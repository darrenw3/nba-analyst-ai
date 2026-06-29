import { useNavigate } from "react-router-dom"

function PlayerCard({ player }) {
    const navigate = useNavigate()

    return (
        <div onClick={() => navigate(`/players/${player.id}`)}>
            <h3>{player.name}</h3>
            <p>{player.team}</p>
            <p>{player.position}</p>
        </div>
    )
}

export default PlayerCard