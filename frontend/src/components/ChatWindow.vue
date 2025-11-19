<template>
  <div class="chat-window" ref="chatContainer">
    <div v-if="messages.length === 0" class="empty-state">
      <h2>👋 Welcome to ZUS Coffee Assistant</h2>
      <p>Ask me about products, find outlets, or calculate prices!</p>
      <p class="hint">Try: "Show me tumblers under $30" or "/calc 200 * 0.8"</p>
    </div>

    <div v-else class="messages">
      <template v-for="message in messages" :key="message.id">
        <UserMessage v-if="message.role === 'user'" :message="message" />
        <AgentMessage v-else :message="message" />
      </template>
    </div>

    <div v-if="isLoading" class="typing-indicator">
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, nextTick } from 'vue';
import type { Message } from '../types/chat';
import UserMessage from './UserMessage.vue';
import AgentMessage from './AgentMessage.vue';

const props = defineProps<{
  messages: Message[];
  isLoading: boolean;
}>();

const chatContainer = ref<HTMLElement | null>(null);

// Auto-scroll to bottom when new messages arrive
watch(() => [props.messages.length, props.isLoading], async () => {
  await nextTick();
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
  }
});
</script>

<style scoped>
.chat-window {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
  display: flex;
  flex-direction: column;
  scroll-behavior: smooth;
}

.empty-state {
  text-align: center;
  color: #6b7280;
  margin-top: 60px;
}

.empty-state h2 {
  color: #111827;
  margin-bottom: 12px;
  font-size: 24px;
}

.empty-state p {
  margin: 8px 0;
  font-size: 16px;
}

.empty-state .hint {
  font-size: 14px;
  color: #9ca3af;
  margin-top: 20px;
}

.messages {
  display: flex;
  flex-direction: column;
}

.typing-indicator {
  display: flex;
  gap: 6px;
  padding: 12px 16px;
  background: #f3f4f6;
  border-radius: 18px 18px 18px 4px;
  width: fit-content;
  margin-bottom: 16px;
}

.dot {
  width: 8px;
  height: 8px;
  background: #9ca3af;
  border-radius: 50%;
  animation: bounce 1.4s infinite ease-in-out;
}

.dot:nth-child(1) {
  animation-delay: -0.32s;
}

.dot:nth-child(2) {
  animation-delay: -0.16s;
}

@keyframes bounce {
  0%, 80%, 100% {
    transform: scale(0);
  }
  40% {
    transform: scale(1);
  }
}

/* Scrollbar styling */
.chat-window::-webkit-scrollbar {
  width: 6px;
}

.chat-window::-webkit-scrollbar-track {
  background: #f9fafb;
}

.chat-window::-webkit-scrollbar-thumb {
  background: #d1d5db;
  border-radius: 3px;
}

.chat-window::-webkit-scrollbar-thumb:hover {
  background: #9ca3af;
}
</style>
