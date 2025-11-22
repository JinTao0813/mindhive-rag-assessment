<template>
  <div class="composer">
    <textarea
      v-model="input"
      @keydown="handleKeyDown"
      placeholder="Type your message... (Shift+Enter for new line)"
      rows="1"
      ref="textareaRef"
      :disabled="isLoading"
    />
    <button
      @click="handleSend"
      :disabled="!input.trim() || isLoading"
      class="send-btn"
      title="Send message (Enter)"
    >
      <span v-if="isLoading" class="spinner">⏳</span>
      <span v-else>➤</span>
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref, watch, nextTick } from 'vue';

const props = defineProps<{
  isLoading: boolean;
}>();

const emit = defineEmits<{
  send: [message: string];
}>();

const input = ref('');
const textareaRef = ref<HTMLTextAreaElement | null>(null);

function handleKeyDown(event: KeyboardEvent) {
  if (event.key === 'Enter' && !event.shiftKey) {
    event.preventDefault();
    handleSend();
  }
}

function handleSend() {
  if (input.value.trim() && !props.isLoading) {
    emit('send', input.value);
    input.value = '';
    resetTextareaHeight();
  }
}

function resetTextareaHeight() {
  if (textareaRef.value) {
    textareaRef.value.style.height = 'auto';
  }
}

// Auto-resize textarea
watch(input, async () => {
  await nextTick();
  if (textareaRef.value) {
    textareaRef.value.style.height = 'auto';
    textareaRef.value.style.height = textareaRef.value.scrollHeight + 'px';
  }
});
</script>

<style scoped>
.composer {
  display: flex;
  gap: 12px;
  padding: 16px;
  background: white;
  border-top: 1px solid #e5e7eb;
  align-items: flex-end;
}

textarea {
  flex: 1;
  padding: 12px 16px;
  border: 1px solid #d1d5db;
  border-radius: 24px;
  font-family: inherit;
  font-size: 15px;
  resize: none;
  max-height: 120px;
  overflow-y: auto;
  line-height: 1.5;
  transition: border-color 0.2s;
}

textarea:focus {
  outline: none;
  border-color: #15317a;
  box-shadow: 0 0 0 3px rgba(21, 49, 122, 0.1);
}

textarea:disabled {
  background: #f9fafb;
  cursor: not-allowed;
}

textarea::placeholder {
  color: #9ca3af;
}

.send-btn {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: linear-gradient(135deg, #15317a 0%, #1a3d8f 100%);
  color: white;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  transition: all 0.2s;
  flex-shrink: 0;
  box-shadow: 0 2px 8px rgba(21, 49, 122, 0.3);
}

.send-btn:hover:not(:disabled) {
  background: linear-gradient(135deg, #0d2257 0%, #15317a 100%);
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(21, 49, 122, 0.4);
}

.send-btn:active:not(:disabled) {
  transform: scale(0.95);
}

.send-btn:disabled {
  background: #d1d5db;
  cursor: not-allowed;
  transform: none;
}

.spinner {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

/* Scrollbar styling for textarea */
textarea::-webkit-scrollbar {
  width: 6px;
}

textarea::-webkit-scrollbar-track {
  background: transparent;
}

textarea::-webkit-scrollbar-thumb {
  background: #d1d5db;
  border-radius: 3px;
}
</style>
