<script setup lang="ts">
import { useChat } from './composables/useChat';
import ChatWindow from './components/ChatWindow.vue';
import Composer from './components/Composer.vue';
import QuickActions from './components/QuickActions.vue';

const { messages, isLoading, send, clearHistory } = useChat();

function handleQuickAction(text: string) {
  send(text);
}
</script>

<template>
  <div class="app-container">
    <header class="app-header">
      <div class="header-content">
        <h1>☕ ZUS Coffee Assistant</h1>
        <button @click="clearHistory" class="clear-btn" title="Clear chat history">
          🗑️ Clear
        </button>
      </div>
    </header>

    <QuickActions @select="handleQuickAction" />
    
    <ChatWindow :messages="messages" :isLoading="isLoading" />
    
    <Composer :isLoading="isLoading" @send="send" />
  </div>
</template>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background: #ffffff;
}

.app-header {
  background: linear-gradient(135deg, #15317a 0%, #0d2257 100%);
  color: white;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(21, 49, 122, 0.15);
}

.header-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.app-header h1 {
  margin: 0;
  font-size: 24px;
  font-weight: 600;
}

.clear-btn {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.3);
  padding: 8px 16px;
  border-radius: 20px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
}

.clear-btn:hover {
  background: rgba(255, 255, 255, 0.3);
}

.clear-btn:active {
  transform: scale(0.95);
}
</style>
