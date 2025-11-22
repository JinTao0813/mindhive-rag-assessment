<template>
  <div class="agent-message">
    <div class="message-wrapper">
      <div class="avatar-container">
        <img src="../assets/logo.png" alt="ZUS" class="avatar" />
      </div>
      <div class="message-content-wrapper">
        <div class="message-bubble">
          <div class="message-content">{{ message.content }}</div>
        </div>
        <div class="message-time">{{ formatTime(message.timestamp) }}</div>
      </div>
    </div>
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
.agent-message {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-bottom: 20px;
  animation: slideIn 0.3s ease-out;
}

.message-wrapper {
  display: flex;
  gap: 12px;
  max-width: 75%;
}

.avatar-container {
  flex-shrink: 0;
  width: 36px;
  height: 36px;
  background: white;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 4px;
  box-shadow: 0 2px 6px rgba(21, 49, 122, 0.15);
  border: 1.5px solid #e8ecf4;
}

.avatar {
  width: 100%;
  height: 100%;
  scale: 3;
  object-fit: contain;
}

.message-content-wrapper {
  display: flex;
  flex-direction: column;
  flex: 1;
}

.message-bubble {
  background: #ffffff;
  color: #1f2937;
  padding: 14px 18px;
  border-radius: 4px 18px 18px 18px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.08);
  border: 1px solid #e8ecf4;
}

.message-content {
  white-space: pre-wrap;
  word-wrap: break-word;
  line-height: 1.5;
}

.message-time {
  font-size: 11px;
  color: #9ca3af;
  margin-top: 6px;
  margin-left: 4px;
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
