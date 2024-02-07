// Assuming you are using fetch for API communication
const API_BASE_URL = 'http://localhost:5000/api';

export async function fetchGifts() {
  const response = await fetch(`${API_BASE_URL}/gifts`);
  if (!response.ok) {
    throw new Error('Failed to fetch gifts');
  }
  return response.json();
}
