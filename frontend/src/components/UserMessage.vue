<template>
  <div class="user-message">
    <div class="message-bubble">
      {{ message.content }}
    </div>
    <div class="message-time">{{ formatTime(message.timestamp) }}</div>
  </div>
</template>

<script setup lang="ts">
import type { Message } from '../types/chat';

defineProps<{
  message: Message;
}>();

function formatTime(timestamp: number): string {
  const date = new Date(timestamp);
  return date.toLocaleTimeString('en-US', { 
    hour: '2-digit', 
    minute: '2-digit' 
  });
}
</script>

<style scoped>
.user-message {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  margin-bottom: 16px;
  animation: slideIn 0.3s ease-out;
}

.message-bubble {
  background: #2563eb;
  color: white;
  padding: 12px 16px;
  border-radius: 18px 18px 4px 18px;
  max-width: 70%;
  word-wrap: break-word;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.message-time {
  font-size: 12px;
  color: #6b7280;
  margin-top: 4px;
  margin-right: 8px;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
