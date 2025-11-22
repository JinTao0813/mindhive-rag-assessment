<template>
  <div class="quick-actions">
    <button
      v-for="action in actions"
      :key="action.command"
      @click="$emit('select', action.text)"
      class="action-btn"
      :title="action.description"
    >
      <span class="icon">{{ action.icon }}</span>
      <span class="label">{{ action.label }}</span>
    </button>
  </div>
</template>

<script setup lang="ts">
defineEmits<{
  select: [text: string];
}>();

const actions = [
  {
    command: '/calc',
    label: 'Calculate',
    icon: '🔢',
    text: '/calc ',
    description: 'Calculate mathematical expressions'
  },
  {
    command: '/products',
    label: 'Products',
    icon: '☕',
    text: 'Show me drinkware products',
    description: 'Search for products'
  },
  {
    command: '/outlets',
    label: 'Outlets',
    icon: '📍',
    text: 'Find ZUS Coffee outlets',
    description: 'Find outlet locations'
  },
  {
    command: '/help',
    label: 'Help',
    icon: '❓',
    text: 'What can you help me with?',
    description: 'Show available commands'
  }
];
</script>

<style scoped>
.quick-actions {
  display: flex;
  gap: 8px;
  padding: 12px 16px;
  background: #f9fafb;
  border-bottom: 1px solid #e5e7eb;
  overflow-x: auto;
  flex-wrap: wrap;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  background: white;
  border: 1px solid #d1d5db;
  border-radius: 20px;
  cursor: pointer;
  font-size: 14px;
  transition: all 0.2s;
  white-space: nowrap;
}

.action-btn:hover {
  background: #f8f9fa;
  border-color: #15317a;
  transform: translateY(-1px);
  box-shadow: 0 2px 8px rgba(21, 49, 122, 0.15);
  color: #15317a;
}

.action-btn:active {
  transform: translateY(0);
}

.icon {
  font-size: 16px;
}

.label {
  color: #374151;
  font-weight: 500;
}

/* Hide scrollbar but keep functionality */
.quick-actions::-webkit-scrollbar {
  height: 4px;
}

.quick-actions::-webkit-scrollbar-track {
  background: transparent;
}

.quick-actions::-webkit-scrollbar-thumb {
  background: #d1d5db;
  border-radius: 2px;
}
</style>
