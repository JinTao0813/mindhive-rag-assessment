import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export interface ChatRequest {
  message: string;
  session_id: string;
}

export interface ChatResponse {
  response: string;
}

export async function sendMessage(message: string, sessionId: string): Promise<string> {
  try {
    const response = await axios.post<ChatResponse>(`${API_BASE_URL}/chat/`, {
      message,
      session_id: sessionId,
    });
    return response.data.response;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      throw new Error(error.response?.data?.detail || 'Failed to send message');
    }
    throw new Error('An unexpected error occurred');
  }
}
