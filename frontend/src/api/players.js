import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000'

const api = axios.create({
    baseURL: API_BASE_URL,
})

export const searchPlayers = async (name) => {
    const response = await api.get(`/players/search/query?name=${encodeURIComponent(name)}`)
    return response.data
}

export const getPlayer = async (playerId) => {
    const response = await api.get(`/players/${playerId}`)
    return response.data
}

export const getAllPlayers = async () => {
    const response = await api.get('/players')
    return response.data
}

export const getPlayerStats = async (playerId) => {
    const response = await api.get(`/players/${playerId}/stats`)
    return response.data
}
