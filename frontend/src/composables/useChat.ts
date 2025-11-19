import { ref, watch } from 'vue';
import type { Message, ChatState } from '../types/chat';
import { sendMessage } from '../services/api';
import { v4 as uuidv4 } from 'uuid';

const STORAGE_KEY = 'zus-chat-history';
const SESSION_KEY = 'zus-session-id';

// Load from localStorage
function loadFromStorage(): ChatState {
  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    const sessionId = localStorage.getItem(SESSION_KEY) || uuidv4();
    
    if (stored) {
      const parsed = JSON.parse(stored);
      return {
        messages: parsed.messages || [],
        sessionId,
        isLoading: false,
        error: null,
      };
    }
  } catch (error) {
    console.error('Failed to load chat history:', error);
  }
  
  return {
    messages: [],
    sessionId: uuidv4(),
    isLoading: false,
    error: null,
  };
}

// Save to localStorage
function saveToStorage(messages: Message[], sessionId: string) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({ messages }));
    localStorage.setItem(SESSION_KEY, sessionId);
  } catch (error) {
    console.error('Failed to save chat history:', error);
  }
}

export function useChat() {
  const initialState = loadFromStorage();
  
  const messages = ref<Message[]>(initialState.messages);
  const sessionId = ref<string>(initialState.sessionId);
  const isLoading = ref<boolean>(false);
  const error = ref<string | null>(null);

  // Auto-save to localStorage when messages change
  watch(messages, (newMessages) => {
    saveToStorage(newMessages, sessionId.value);
  }, { deep: true });

  async function send(content: string) {
    if (!content.trim()) return;

    error.value = null;

    // Add user message
    const userMessage: Message = {
      id: uuidv4(),
      role: 'user',
      content: content.trim(),
      timestamp: Date.now(),
    };
    messages.value.push(userMessage);

    // Send to backend
    isLoading.value = true;
    try {
      const response = await sendMessage(content.trim(), sessionId.value);
      
      // Add agent response
      const agentMessage: Message = {
        id: uuidv4(),
        role: 'agent',
        content: response,
        timestamp: Date.now(),
      };
      messages.value.push(agentMessage);
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Failed to get response';
      
      // Add error message
      const errorMessage: Message = {
        id: uuidv4(),
        role: 'agent',
        content: `Sorry, I encountered an error: ${error.value}`,
        timestamp: Date.now(),
      };
      messages.value.push(errorMessage);
    } finally {
      isLoading.value = false;
    }
  }

  function clearHistory() {
    messages.value = [];
    sessionId.value = uuidv4();
    localStorage.removeItem(STORAGE_KEY);
    localStorage.removeItem(SESSION_KEY);
  }

  return {
    messages,
    sessionId,
    isLoading,
    error,
    send,
    clearHistory,
  };
}
