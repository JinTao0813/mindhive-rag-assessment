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
  background: linear-gradient(135deg, #15317a 0%, #1a3d8f 100%);
  color: white;
  padding: 14px 18px;
  border-radius: 18px 18px 4px 18px;
  max-width: 75%;
  word-wrap: break-word;
  box-shadow: 0 2px 8px rgba(21, 49, 122, 0.2);
  line-height: 1.5;
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
